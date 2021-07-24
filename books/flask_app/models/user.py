from flask_app.config.mysqlDB import connect

class User:
    def __init__(self, data):
        self.id = data['id']
        self.firstName = data['fn']
        self.lastName = data['ln']
        self.email = data['e']
        self.password = data['p']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM users;'
        allUsers = connect('initflask').query_db(query)
        users = []
        for u in allUsers:
            users.append(cls(u))
        return users

    @classmethod
    def save(cls, data):
        query = 'Insert INTO burgers (firstName, lastName, email, password, created_at) VALUES(%(fn)s, %(ln)s, %(e)s, %(p)s, NOW());'
        user_id = connect('initflask').query_db(query, data)
        return user_id