from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash

class Recipe:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.under_30 = data['under_30']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_created = data['date_created']
        self.date_updated = data['date_updated']
        self.date_made = data['date_made']
        self.user_id = data['user_id']

    @staticmethod
    def validate_recipe(recipe):
        is_valid = True
        if len(recipe['name']) < 3:
            flash("Recipe name must be at least 3 characters.")
            is_valid = False
        if len(recipe['description']) < 3:
            flash("Description must be at least 3 characters.")
            is_valid = False
        if len(recipe['instructions']) < 3:
            flash("Instructions must be at least 3 characters.")
            is_valid = False
        return is_valid

    @classmethod
    def save_recipe(cls,data):
        query = "INSERT INTO recipes (name,under_30,description,instructions,date_created,date_updated,date_made,user_id) VALUES (%(name)s,%(under_30)s,%(description)s,%(instructions)s,NOW(),NOW(),%(date_made)s,%(user_id)s);"
        return connectToMySQL('users_schema').query_db(query,data)
    
    @classmethod
    def update_recipe(cls,data):
        query = "UPDATE recipes SET name=%(name)s,under_30=%(under_30)s,description=%(description)s,instructions=%(instructions)s,date_updated=NOW(),date_made=%(date_made)s WHERE id=%(id)s;"
        return connectToMySQL('users_schema').query_db(query,data)

    @classmethod
    def get_all_recipes(cls):
        query = "SELECT * FROM recipes;"
        recipes_from_db = connectToMySQL('users_schema').query_db(query)
        recipes = []
        for recipe in recipes_from_db:
            recipes.append(cls(recipe))
        return recipes
    
    @classmethod
    def get_one_recipe(cls,data):
        query = "SELECT * FROM recipes WHERE recipes.id = %(id)s;"
        results = connectToMySQL('users_schema').query_db(query,data)
        return cls(results[0])

    @classmethod
    def destroy_recipe(cls,data):
        query = "DELETE FROM recipes WHERE recipes.id = %(id)s;"
        return connectToMySQL('users_schema').query_db(query,data)