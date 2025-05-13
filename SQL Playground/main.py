import sqlite3

db = sqlite3.connect("SQL Playground/books-collection.db")

cursor = db.cursor()

# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating varchar(250) NOT NULL)")

cursor.execute("INSERT INTO books VALUES(1, 'A Court of Silver Flames', 'Sarah J. Mass', '★★★★★')")
db.commit()