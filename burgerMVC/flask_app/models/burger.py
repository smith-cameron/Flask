from flask_app.config.mysqlDB import connect
from flask_app.models import topping
myDB = 'flaskburgersmvc'

class Burger:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.bun = data['bun']
        self.meat = data['meat']
        self.temp = data['temp']
        self.restaurantId = data['restaurantId']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']
        self.toppings = []
    
    @classmethod
    def getAll(cls):
        query = "SELECT * FROM burgers"
        results = connect(myDB).query_db(query)
        objects = []
        for i in results:
            objects.append(cls(i))
        return objects

    @classmethod
    def save(cls, data):
        query = "Insert INTO burgers (name, bun, meat, temp, restaurantId, createdAt) VALUES(%(name)s, %(bun)s, %(meat)s, %(temp)s, %(restaurantId)s, NOW());"
        objectId = connect(myDB).query_db(query,data)
        return objectId

    @classmethod
    def getByIdJoinToppings(cls, data ):
        query = "SELECT * FROM burgers LEFT JOIN add_ons ON add_ons.burger_id = burgers.id LEFT JOIN toppings ON add_ons.topping_id = toppings.id WHERE burgers.id = %(id)s;"
        results = connect(myDB).query_db( query , data )
        object = cls( results[0] )
        for row_from_db in results:
            topping_data = {
                "id" : row_from_db["toppings.id"],
                "topping_name" : row_from_db["toppings.name"],
                "createdAt" : row_from_db["toppings.createdAt"],
                "updatedAt" : row_from_db["toppings.updatedAt"]
            }
            object.toppings.append( topping.Topping( topping_data ) )
        return object