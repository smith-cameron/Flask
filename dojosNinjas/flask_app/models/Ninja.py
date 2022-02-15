from flask_app.config.mysqlDB import connect
myDB = 'flaskDojosNinjas'

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.firstName = data['firstName']
        self.lastName = data['lastName']
        self.age = data['age']
        self.dojoId = data['dojoId']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM ninjas;'
        allNinjas = connect(myDB).query_db(query)
        ninjas = []
        for n in allNinjas:
            ninjas.append(cls(n))
        return ninjas

    @classmethod
    def save(cls, data):
        query = 'Insert INTO ninjas (firstName, lastName, age, dojoId, createdAt) VALUES(%(firstName)s, %(lastName)s, %(age)s, %(dojoId)s, NOW());'
        return connect(myDB).query_db(query, data)