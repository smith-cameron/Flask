from flask_app.config.mysqlDB import connect
myDB = 'flaskburgersmvc'

class Restaurant:
    def __init__( self , db_data ):
        self.id = db_data['id']
        self.rName = db_data['rName']
        self.createdAt = db_data['createdAt']
        self.updatedAt = db_data['updatedAt']
        self.burgers = []
    
    @classmethod
    def save(cls ,data):
        query = "INSERT INTO restaurants (rName, createdAt) VALUES (%(rName)s,NOW());"
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
    def get_restaurant_with_burgers( cls , data ):
        query = "SELECT * FROM restaurants LEFT JOIN burgers ON burgers.restaurantId = restaurants.id WHERE restaurants.id = %(id)s;"
        results = connect(myDB).query_db( query , data )
        objects = cls( results[0] )
        for i in results:
            join_data = {
                "id" : i["burgers.id"],
                "name" : i["burgers.name"],
                "bun" : i["bun"],
                "meat" : i["meat"],
                "temp" : i["temp"],
                "created_at" : i["burgers.created_at"],
                "updated_at" : i["burgers.updated_at"]
            }
            objects.burgers.append( objects.Burger( join_data ) )
        return objects