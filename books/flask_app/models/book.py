from flask_app.config.mysqlDB import connect

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
    def getFav(cls, data):
        query = 'SELECT * FROM favorites WHERE book_id = %(i)s;'
        bookFavs = connect('booksAuthors').query_db(query, data)
        return bookFavs

    @classmethod
    def getNotFav(cls, data):
        query = 'SELECT n.userName, n.comment, lo.locName, la.langName FROM books b LeftJOIN locations lo ON locId = lo.id JOIN languages la ON langId = la.id WHERE n.id = %(n)s;'
        notFavs = connect('booksAuthors').query_db(query, data)
        return notFavs