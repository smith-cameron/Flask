from recipeApp.config.mysqlDB import connect
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self, data):
        self.id = data['id']
        self.firstName = data['firstName']
        self.lastName = data['lastName']
        self.email = data['email']
        self.password = data['password']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']

    @staticmethod
    def validateRegistration(request):
        allowedSymbols =['$', '@', '#', '%', '!', '&', '*']
        valid = True
        if len(request['firstName']) < 1:
            flash("First Name Required", "regError")
            valid = False
        if len(request['lastName']) < 1:
            flash("Last Name Required", "regError")
            valid = False
        if not EMAIL_REGEX.match(request['email']):
            flash("Invalid Email Address", "regError")
            valid = False
        if len(request['email']) < 1:
            flash("Email Required", "regError")
            valid = False
        if len(request['password']) < 1:
            flash("Password Required", "regError")
            valid = False
        if len(request['password']) > 1 and len(request['password']) < 8:
            flash("Password Must Be 8 Characters Or More", "regError")
            valid = False
        if not any(char.isdigit() for char in request['password']):
            print('Password Requires Minimum Of One Number', "regError")
            valid = False
        if not any(char.isupper() for char in request['password']):
            print('Password Requires Minimum Of One Uppercase Letter', "regError")
            valid = False
        if not any(char.islower() for char in request['password']):
            print('Password Requires Minimum Of One Lowercase Letter', "regError")
            valid = False
        if not any(char in allowedSymbols for char in request['password']):
            print('Password Requires Minimum Of One Symbol $@#%!&*', "regError")
            valid = False
        if request['password'] != request['passConf']:
            flash("Passwords Do Not Match", "regError")
            valid = False
        return valid

    @classmethod
    def getByEmail(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        userEmail = connect("recipes").query_db(query,data)
        if len(userEmail) < 1:
            return False
        return cls(userEmail[0])

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM users;'
        allUsers = connect('recipes').query_db(query)
        return allUsers

    @classmethod
    def save(cls, data):
        query = 'Insert INTO users (firstName, lastName, email, password, createdAt) VALUES(%(fn)s, %(ln)s, %(e)s, %(p)s, NOW());'
        user_id = connect('recipes').query_db(query, data)
        return user_id

    @classmethod
    def findById(cls, data):
        query = 'SELECT * FROM users WHERE id = %(i)s;'
        thisUser = connect('recipes').query_db(query, data)
        return cls(thisUser[0])

    @classmethod
    def deleteById(cls, data):
        query = 'DELETE FROM users WHERE id = %(i)s;'
        thisUser = connect('recipes').query_db(query, data)