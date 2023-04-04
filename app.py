import os

from flask import Flask
from flask import render_template
from flask import request

from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')

db = SQLAlchemy(app)


class Book(db.Model):
    title = db.Column(
        db.String(80), unique=True, nullable=False, primary_key=True
    )

    def __repr__(self):
        return f'<Title: {self.title}>'


@app.route('/', methods=['GET', 'POST'])
def home():
    form = request.form
    if form:
        book_title = form.get('title')
        book = Book(title=book_title)

        db.session.add(book)
        db.session.commit()

    return render_template('home.html')
