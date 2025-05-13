from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

app = Flask(__name__)

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////Users/liviasilva/Documents/Projects/100DaysOfPython/SQLAlchemy/new-books-collection.db"
db.init_app(app)

class Books(db.Model):
    __tablename__ = "Reviews"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True)
    author: Mapped[str] = mapped_column(nullable=False)
    rating: Mapped[str] = mapped_column(nullable=False)
    
with app.app_context():
    db.create_all()

# Create a new record
with app.app_context():
    new_book = Books(title="Hide and Seek", author="Lily Everglot", rating="★★★")
    db.session.add(new_book)
    db.session.commit()

# Read all records
with app.app_context():
    result = db.session.execute(db.select(Books).order_by(Books.title))
    all_books = result.scalars()
    
    for book in all_books:
        print(book.title)
        
# Read a particular record by query
with app.app_context():
    book = db.session.execute(db.select(Books).where(Books.title == "Hide and Seek")).scalar()
    
# Update A Particular Record By Query
with app.app_context():
    book_to_update = db.session.execute(db.select(Books).where(Books.title == "Hide and Seek")).scalar()
    book_to_update.title = "Harry Potter and the Chamber of Secrets"
    db.session.commit() 

# Update A Record By PRIMARY KEY
book_id = 1
with app.app_context():
    book_to_update = db.session.execute(db.select(Books).where(Books.id == book_id)).scalar()
    # or book_to_update = db.get_or_404(Book, book_id)  
    book_to_update.title = "Harry Potter and the Goblet of Fire"
    db.session.commit()  

# Delete A Particular Record By PRIMARY KEY
book_id = 3
with app.app_context():
    book_to_delete = db.session.execute(db.select(Books).where(Books.id == book_id)).scalar()
    # or book_to_delete = db.get_or_404(Book, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()