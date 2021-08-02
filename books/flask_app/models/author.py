from flask_app.config.mysqlDB import connect

class Author:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['n']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM authors;'
        allAuth = connect('booksAuthors').query_db(query)
        return allAuth

    @classmethod
    def save(cls, data):
        query = 'Insert INTO authors (name, createdAt) VALUES( %(n)s, NOW());'
        authId = connect('booksAuthors').query_db(query, data)
        return authId

    @classmethod
    def findById(cls, data):
        query = 'SELECT * FROM authors WHERE id = %(i)s;'
        thisAuth = connect('booksAuthors').query_db(query, data)
        return thisAuth

    @classmethod
    def saveFavs(cls, data):
        query = 'Insert INTO favorites (book_id, author_id) VALUES( %(bi)s, %(ai)s);'
        newFav = connect('booksAuthors').query_db(query, data)
        return newFav