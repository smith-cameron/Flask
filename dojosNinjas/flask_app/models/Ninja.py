from flask_app.config.mysqlDB import connect

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.firstName = data['fn']
        self.lastName = data['ln']
        self.age = data['e']
        self.dojoId = data['dId']
        self.createdAt = data['created_at']
        self.updatedAt = data['updated_at']

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM ninjas;'
        allNinjas = connect('dojosNinjas').query_db(query)
        ninjas = []
        for n in allNinjas:
            ninjas.append(cls(n))
        return ninjas

    @classmethod
    def save(cls, data):
        query = 'Insert INTO ninjas (firstName, lastName, age, dojoId, createdAt) VALUES(%(fn)s, %(ln)s, %(a)s, %(d)s, NOW());'
        ninjaId = connect('dojosNinjas').query_db(query, data)
        return ninjaId