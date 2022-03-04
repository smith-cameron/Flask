from flask_app.config.mysqlDB import connect
from flask_app.models.Ninja import Ninja
myDB = 'flaskDojosNinjas'

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']
        self.ninjas = []

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM dojos;'
        results = connect(myDB).query_db(query)
        dojos = []
        for d in results:
            dojos.append( cls(d) )
        return dojos

    @classmethod
    def save(cls, data):
        query = 'Insert INTO dojos (name, createdAt) VALUES(%(name)s, NOW());'
        return connect(myDB).query_db(query, data)

    @classmethod
    def getById(cls, data):
        query = 'SELECT * FROM dojos WHERE id= %(i)s;'
        return connect(myDB).query_db(query, data)

    # @classmethod
    # def getNinjas(cls, data):
    #     query = 'SELECT * FROM ninjas WHERE dojoId= %(i)s;'
    #     thisDojosNinjas = connect(myDB).query_db(query, data)
    #     return thisDojosNinjas

    @classmethod
    def getDojoJoinNinjas(cls, data ):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojoId WHERE dojos.id = %(id)s;"
        results = connect(myDB).query_db(query,data)
        print(results)
        dojo = cls(results[0])
        for row in results:
            n = {
                'id': row['ninjas.id'],
                'firstName': row['firstName'],
                'lastName': row['lastName'],
                'age': row['age'],
                'dojoId' : row['dojoId'],
                'createdAt': row['ninjas.createdAt'],
                'updatedAt': row['ninjas.updatedAt']
            }
            dojo.ninjas.append( Ninja(n))
        return dojo
