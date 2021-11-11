from flask_app.config.mysqlDB import connect
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
myDB = 'flaskEmailValidations'

class User:
    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']

    @staticmethod
    def validateUser(request):
        is_valid = True
        if not EMAIL_REGEX.match(request['email']):
            flash("Invalid email address!")
            is_valid = False
        if len(request['email']) < 1:
            flash("Email Required")
            is_valid = False
        return is_valid

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM users;'
        allUsers = connect(myDB).query_db(query)
        users = []
        for u in allUsers:
            users.append(cls(u))
        return users

    @classmethod
    def save(cls, data):
        query = 'Insert INTO users (email, createdAt) VALUES(%(e)s, NOW());'
        user_id = connect(myDB).query_db(query, data)
        return user_id

    @classmethod
    def findById(cls, data):
        query = 'SELECT * FROM users WHERE id = %(i)s;'
        thisUser = connect(myDB).query_db(query, data)
        print(thisUser)
        return thisUser