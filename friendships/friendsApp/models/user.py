from friendsApp.config.mysqlDB import connect
myDB = 'flaskFriends'

class User:
    def __init__(self, data):
        self.id = data['id']
        self.firstName = data['firstName']
        self.lastName = data['lastName']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM users;'
        allUsers = connect(myDB).query_db(query)
        users = []
        for u in allUsers:
            users.append(cls(u))
        return users

    @classmethod
    def save(cls, data):
        query = 'Insert INTO users (firstName, lastName, createdAt) VALUES(%(fn)s, %(ln)s, NOW());'
        return connect(myDB).query_db(query, data)

