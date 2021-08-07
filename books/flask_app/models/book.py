from flask_app.config.mysqlDB import connect
from flask_app.models.author import Author

class Book:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['t']
        self.pageCount = data['pc']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM books;'
        allBooks = connect('booksAuthors').query_db(query)
        return allBooks

    @classmethod
    def save(cls, data):
        query = 'Insert INTO books (title, pageCount, createdAt) VALUES( %(t)s, %(pc)s, NOW());'
        bookId = connect('booksAuthors').query_db(query, data)
        return bookId

    @classmethod
    def findById(cls, data):
        query = 'SELECT * FROM books WHERE id = %(i)s;'
        thisBook = connect('booksAuthors').query_db(query, data)
        return thisBook

    @classmethod
    def saveFavs(cls, data):
        query = 'Insert INTO favorites (book_id, author_id) VALUES( %(bi)s, %(ai)s);'
        newFav = connect('booksAuthors').query_db(query, data)
        return newFav

    @classmethod
    def getFav(cls, data):
        query = 'SELECT * FROM favorites f JOIN authors a ON author_id = a.id WHERE book_id = %(i)s;'
        bookFavsFromDB = connect('booksAuthors').query_db(query, data)
        return bookFavsFromDB

    @classmethod
    def getNotFav(cls, data):
        query = 'SELECT a.name FROM favorites f JOIN authors a ON author_id = a.id WHERE book_id != %(i)s GROUP BY a.name;'
        notFavs = connect('booksAuthors').query_db(query, data)
        return notFavs
