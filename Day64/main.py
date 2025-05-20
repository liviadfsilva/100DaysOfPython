from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, validators
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("APP_SECRET_KEY")
Bootstrap5(app)

# CREATING DB
class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////Users/liviasilva/Documents/Projects/100DaysOfPython/Day64/instance/movies-list.db"
db.init_app(app)

# DEFINING MODEL
class Movies(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True)
    year: Mapped[int] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    rating: Mapped[float] = mapped_column(nullable=False)
    ranking: Mapped[int] = mapped_column(nullable=False)
    review: Mapped[str] = mapped_column(nullable=False)
    img_url: Mapped[str] = mapped_column(nullable=False)

# CREATING TABLE
with app.app_context():
    db.create_all()
    
# with app.app_context():
#     second_movie = Movies(
#     title="Teste",
#     year=2023,
#     description="Blablabla",
#     rating=7.5,
#     ranking=9,
#     review="I liked the blablabla.",
#     img_url="https://m.media-amazon.com/images/M/MV5BMjE3MDU1MjkyMV5BMl5BanBnXkFtZTgwNjkyMDMwNTE@._V1_.jpg"
# )

#     db.session.add(second_movie)
#     db.session.commit()

# CREATING UPDATE FORM
class RateMovieForm(FlaskForm):
    rating = FloatField('Your Rating Out of 10 e.g. 7.5', [validators.DataRequired()])
    review = StringField('Your Review', [validators.Length(min=6, max=35)])
    submit = SubmitField('Done')
    
# CREATING ADD FORM
class NewMovieForm(FlaskForm):
    title = FloatField('Movie Title', [validators.DataRequired()])
    submit = SubmitField('Add Movie')

@app.route("/")
def home():
    result = db.session.execute(db.select(Movies))
    all_movies = result.scalars().all()
    return render_template("index.html", movies=all_movies)

@app.route("/edit", methods=["GET", "POST"])
def edit_page():
    form = RateMovieForm()
    book_id = request.args.get('id')
    movie = db.get_or_404(Movies, book_id)
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", form=form, movie=movie)

@app.route("/delete")
def delete_movie():
    movie_id = request.args.get('id')
    movie_to_delete = db.get_or_404(Movies, movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/add")
def add_movie():
    form = NewMovieForm()
    return render_template("add.html", form=form)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
