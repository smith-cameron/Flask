from friendsApp.config.mysqlDB import connect
myDB = 'flaskFriends'

class Friendship:
    def __init__(self, data):
        self.id = data['id']
        self.userId = data['userId']
        self.friendId = data['friendId']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']

    @classmethod
    def getAll(cls):
        query = 'SELECT u.firstName AS "uFirstName", u.lastName AS "uLastName",u2.firstName AS "fFirstName", u2.lastName AS "fLastName" FROM friendships f JOIN users u ON userId = u.id JOIN users u2 ON friendId = u2.id;'
        return connect('friends').query_db(query)

    @classmethod
    def save(cls, data):
        query = 'Insert INTO friendships (userId, friendId, createdAt) VALUES(%(ui)s, %(fi)s, NOW());'
        return connect('friends').query_db(query, data)