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
    data = {
        "i" : id
    }
    thisAuthor = Author.findById(data)
    allB = Book.getAll()
    authorFavs = Author.getFav(data)
    # Method should have all books not favorited by this author yet
    print(thisAuthor)
    print(authorFavs)
    return render_template('ShowAuthors.html', author = thisAuthor, dtf = dateFormat, books = allB, favoriteBooks = authorFavs)

@app.route('/books/<int:id>')
def booksShow(id):
    data = {
        "i" : id
    }
    thisBook = Book.findById(data)
    # Method should have all authors who have not liked this book yet
    # notFav = Book.getNotFav(data)
    bookLikers = Book.getFav(data)
    allA = Author.getAll()
    print(thisBook)
    return render_template('showBooks.html', book = thisBook, dtf = dateFormat, authors = allA, favoritedBy = bookLikers)

@app.route('/books/<int:id>/addAuthor', methods = ['POST'])
def addAuthor2Book(id):
    data = {
        "ai" : request.form['authId'],
        "bi" : id
    }
    print(Book.saveFavs(data))
    return redirect(f'/books/{id}')

@app.route('/authors/<int:id>/addBook', methods = ['POST'])
def addBook2Author(id):
    data = {
        "ai" : id,
        "bi" : request.form['bookId']
    }
    print(Author.saveFavs(data))
    return redirect(f'/authors/{id}')

@app.route('/logout')
def sessionReset():
    session.clear()
    return redirect("/")
