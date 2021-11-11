from recipeApp.config.mysqlDB import connect
from flask import flash
myDB = 'flaskRecipes'

class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.desc = data['description']
        self.instructions = data['instructions']
        self.lastMade = data['lastMade']
        self.lastMade = data['timeLimit']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']

    @staticmethod
    def validate(request):
        valid = True
        if len(request['name']) < 1:
            flash("Name Required", "recipeError")
            valid = False
        if request['desc']:
            if len(request['desc']) >= 1 and len(request['desc']) < 10:
                flash("Description Must Be 10 Caracters or more", "recipeError")
                valid = False
        if len(request['inst']) < 1:
            flash("Instructions Required", "recipeError")
            valid = False
        if len(request['lastMade']) < 1:
            flash("Last Date Made Required", "recipeError")
            valid = False
        # if request['lastMade'] > today:
        #     flash("You Cannot Time Travel", "recipeError")
        #     valid = False
        if not request['timeLimit']:
            flash("Field Required", "recipeError")
            valid = False
        return valid

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM recipes;'
        return connect(myDB).query_db(query)

    @classmethod
    def save(cls, data):
        query = 'Insert INTO recipes (name, description, instructions, lastMade, timeLimit, creatorId, createdAt) VALUES(%(n)s, %(d)s, %(i)s, %(lm)s, %(tl)s, %(c)s, NOW());'
        return connect(myDB).query_db(query, data)

    @classmethod
    def findById(cls, data):
        query = 'SELECT * FROM recipes WHERE id = %(i)s;'
        return connect(myDB).query_db(query, data)

    @classmethod
    def deleteById(cls, data):
        query = 'DELETE FROM recipes WHERE id = %(i)s;'
        thisRecipe = connect(myDB).query_db(query, data)