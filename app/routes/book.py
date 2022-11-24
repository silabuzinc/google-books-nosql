from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.forms import BookForm
from app.db import db
from app.models.book import Book

book_router = Blueprint('book_router', __name__)


@book_router.route('/')
def index():
    books = db.books.find()
    return render_template('index.html', books=books)


@book_router.route('/store-book', methods=['GET', 'POST'])
def store_book():
    book_form = BookForm()

    if request.method == 'POST':
        if book_form.validate_on_submit():
            new_book = Book(
                book_form.title.data,
                book_form.author.data,
                book_form.pages.data,
                book_form.publish_date.data,
                book_form.description.data,
                book_form.isbn.data

            )
            
            db.books.insert_one(new_book.to_json())
            
            flash('Book created successfully', 'success')

            return redirect(url_for('book_router.index'))

    return render_template('store-book.html', book_form=book_form)
