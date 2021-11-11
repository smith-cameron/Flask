from flask_app.config.mysqlDB import connect
myDB = 'flaskDojosNinjas'

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['n']
        self.createdAt = data['created_at']
        self.updatedAt = data['updated_at']

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM dojos;'
        allDojos = connect(myDB).query_db(query)
        return allDojos

    @classmethod
    def save(cls, data):
        query = 'Insert INTO dojos (name, createdAt) VALUES(%(n)s, NOW());'
        user_id = connect(myDB).query_db(query, data)
        return user_id

    @classmethod
    def getById(cls, data):
        query = 'SELECT * FROM dojos WHERE id= %(i)s;'
        thisDojo = connect(myDB).query_db(query, data)
        return thisDojo

    @classmethod
    def getNinjas(cls, data):
        query = 'SELECT * FROM ninjas WHERE dojoId= %(i)s;'
        thisDojosNinjas = connect(myDB).query_db(query, data)
        return thisDojosNinjas