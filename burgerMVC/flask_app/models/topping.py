from flask_app.config.mysqlDB import connect
from flask_app.models import burger
myDB = 'flaskburgersmvc'

class Topping:
    def __init__(self, db_data ):
        self.id = db_data['id']
        self.name = db_data['name']
        self.createdAt = db_data['createdAt']
        self.updatedAt = db_data['updatedAt']
        self.addOns = []
    
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO toppings ( topping_name, createdAt , updatedAt ) VALUES (%(topping_name)s,NOW(),NOW());"
        return connect(myDB).query_db(query, data)

    @classmethod
    def getAll(cls):
        query = "SELECT * FROM toppings;"
        results = connect(myDB).query_db(query)
        objects = []
        for i in results:
            objects.append(cls(i))
        return objects

    @classmethod
    def getByIdJoinBurgers(cls, data ):
        query = "SELECT * FROM toppings LEFT JOIN add_ons ON add_ons.topping_id = toppings.id LEFT JOIN burgers ON add_ons.burger_id = burgers.id WHERE toppings.id = %(id)s;"
        results = connect(myDB).query_db( query , data )
        object = cls( results[0] )
        for i in results:
            burger_data = {
                "id" : i["burgers.id"],
                "name" : i["burgers.name"],
                "bun" : i["bun"],
                "calories" : i["temp"],
                "createdAt" : i["burgers.createdAt"],
                "updatedAt" : i["burgers.updatedAt"]
            }
            object.addOns.append( burger.Burger( burger_data ) )
        return object

