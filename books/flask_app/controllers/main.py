from flask_app import app
from flask import Flask
from flask import render_template, request, redirect, session, flash
from flask_app.models.book import Book
from flask_app.models.author import Author
from datetime import datetime
dateFormat = "%m/%d/%Y"

@app.route('/')
def index():
    return redirect('/books')

@app.route('/authors')
def authors():
    allAuthors = Author.getAll()
    print(allAuthors)
    return render_template('authors.html', authors = allAuthors, dtf = dateFormat)

@app.route('/books')
def books():
    allBooks = Book.getAll()
    print(allBooks)
    return render_template('books.html', books = allBooks, dtf = dateFormat)

@app.route('/books', methods=['POST'])
def createBook():
	data = {
            "t" : request.form['title'],
            "pc" : request.form['pageCount']
    }
	print(Book.save(data))
	return redirect('/books')

@app.route('/authors', methods=['POST'])
def createAuthor():
    data = {
        "n" : request.form['name']
    }
    print(Author.save(data))
    return redirect('/authors')

@app.route('/authors/<int:id>')
def authorsShow(id):
    allAuthors = Author.getAll()
    print(allAuthors)
    return render_template('ShowAuthors.html', authors = allAuthors, dtf = dateFormat)

@app.route('/books/<int:id>')
def booksShow(id):
    allBooks = Book.getAll()
    print(allBooks)
    return render_template('showBooks.html', books = allBooks, dtf = dateFormat)

@app.route('/logout')
def sessionReset():
    session.clear()
    return redirect("/")
