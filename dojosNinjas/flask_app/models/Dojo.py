from flask_app.config.mysqlDB import connect

class Dojo:
    def __iniy__(self, data):
        self.id = data['id']
        self.name = data['n']
        self.createdAt = data['created_at']
        self.updatedAt = data['updated_at']

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM dojos;'
        allDojos = connect('dojosNinjas').query_db(query)
        return allDojos

    @classmethod
    def save(cls, data):
        query = 'Insert INTO dojos (name, createdAt) VALUES(%(n)s, NOW());'
        user_id = connect('dojosNinjas').query_db(query, data)
        return user_id

    @classmethod
    def getById(cls, data):
        query = 'SELECT * FROM dojos WHERE id= %(i)s;'
        thisDojo = connect('dojosNinjas').query_db(query, data)
        return thisDojo

    @classmethod
    def getNinjas(cls, data):
        query = 'SELECT * FROM ninjas WHERE dojoId= %(i)s;'
        thisDojosNinjas = connect('dojosNinjas').query_db(query, data)
        return thisDojosNinjas