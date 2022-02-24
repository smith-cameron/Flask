from flask_app.config.mysqlDB import connect
from flask_app.models import burger
myDB = 'flaskburgersmvc'

class Restaurant:
    def __init__(self, db_data ):
        self.id = db_data['id']
        self.name = db_data['name']
        self.createdAt = db_data['createdAt']
        self.updatedAt = db_data['updatedAt']
        self.burgers = []
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO restaurants (name, createdAt) VALUES (%(name)s,NOW());"
        return connect('myDB').query_db(query,data)

    @classmethod
    def getAll(cls):
        query = "SELECT * FROM restaurants"
        results = connect(myDB).query_db(query)
        objects = []
        for i in results:
            objects.append(cls(i))
        return objects
    
    @classmethod
    def getByIdJoinBurgers(cls, data):
        query = "SELECT * FROM restaurants LEFT JOIN burgers ON burgers.restaurantId = restaurants.id WHERE restaurants.id = %(id)s;"
        results = connect(myDB).query_db( query , data )
        print(results)
        object = cls( results[0] )
        print(object)
        for i in results:
            print(i['id'])
            join_data = {
                "id" : i["burgers.id"],
                "name" : i["burgers.name"],
                "bun" : i["bun"],
                "meat" : i["meat"],
                "temp" : i["temp"],
                "restaurantId" : i["restaurantId"],
                "createdAt" : i["burgers.createdAt"],
                "updatedAt" : i["burgers.updatedAt"]
            }
            object.burgers.append( burger.Burger( join_data ) )
        print(object)
        return object