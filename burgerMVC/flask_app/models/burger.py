from flask_app.config.mysqlDB import connect
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
    
    @classmethod
    def getAll(cls):
        query = "SELECT * FROM burgers"
        results = connect(myDB).query_db(query)
        objects = []
        for i in results:
            objects.append(cls(i))
        return objects

    @classmethod
    def save(cls,data):
        query = "Insert INTO burgers (name, bun, meat, temp, restaurantId, createdAt) VALUES(%(name)s, %(bun)s, %(meat)s, %(temp)s, %(restaurantId)s, NOW());"
        objectId = connect(myDB).query_db(query,data)
        return objectId