from flask_app.config.mysqlDB import connect
myDB = "flaskbooks"

class Author:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['n']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM authors;'
        allAuth = connect(myDB).query_db(query)
        return allAuth

    @classmethod
    def save(cls, data):
        query = 'Insert INTO authors (name, createdAt) VALUES( %(n)s, NOW());'
        authId = connect(myDB).query_db(query, data)
        return authId

    @classmethod
    def findById(cls, data):
        query = 'SELECT * FROM authors WHERE id = %(i)s;'
        thisAuth = connect(myDB).query_db(query, data)
        return thisAuth

    @classmethod
    def saveFavs(cls, data):
        query = 'Insert INTO favorites (book_id, author_id) VALUES( %(bi)s, %(ai)s);'
        newFav = connect(myDB).query_db(query, data)
        return newFav

    @classmethod
    def getFav(cls, data):
        # Need to update query to return whole opjects
        query = 'SELECT b.title FROM favorites f JOIN books b ON book_id = b.id WHERE author_id = %(i)s GROUP BY title;'
        authorFavsFromDB = connect(myDB).query_db(query, data)
        favs = []
        for i in authorFavsFromDB:
            for val in i:
                favs.append(i[val])
        # print(favs)
        return favs