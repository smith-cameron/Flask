from wallApp.config.mysqlDB import connect
from flask import flash
myDB = 'flaskWall'

class Post:
    def __init__(self, data):
        self.id = data['id']
        self.content = data['content']
        self.creatorId = data['creatorId']
        self.recipientId = data['recipientId']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']

    @staticmethod
    def validatePost(request):
        valid = True
        if len(request['content']) < 1:
            flash("**Post Content Required**", "postError")
            valid = False
        if len(request['content']) > 255:
            flash("**Post Too Long**", "postError")
            valid = False
        return valid

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM posts;'
        allPosts = connect(myDB).query_db(query)
        return allPosts

    @classmethod
    def save(cls, data):
        query = 'Insert INTO posts (content, creatorId, recipientId, createdAt) VALUES(%(c)s, %(ci)s, %(ri)s, NOW());'
        return connect(myDB).query_db(query, data)

    @classmethod
    def findByUserId(cls, data):
        query = 'SELECT * FROM posts m JOIN users u ON m.creatorId = u.id WHERE recipientId = %(i)s;'
        return connect(myDB).query_db(query, data)

    @classmethod
    def findById(cls, data):
        query = 'SELECT * FROM posts WHERE id = %(i)s;'
        thisMessage = connect(myDB).query_db(query, data)
        return cls(thisMessage[0])

    @classmethod
    def deleteById(cls, data):
        query = 'DELETE FROM posts WHERE id = %(i)s;'
        connect(myDB).query_db(query, data)

    @classmethod
    def sentPostsCount(cls, data):
        query = 'SELECT COUNT(id) FROM posts WHERE creatorId = %(i)s;'
        count = connect(myDB).query_db(query, data)
        val = 0
        for c in count:
            for v in c:
                val = c[v]
        return val

    @classmethod
    def recievedPostCount(cls, data):
        query = 'SELECT COUNT(id) FROM posts WHERE recipientId = %(i)s;'
        count = connect(myDB).query_db(query, data)
        val = 0
        for c in count:
            for v in c:
                val = c[v]
        return val