from flask import Flask, render_template, request, redirect, session
from mysqlconnection import connectToMySQL
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'secret_keyy'
createFormat = "%B-%d-%Y, %-I:%M %p"
updateFormat = "%B-%d-%Y at %-I:%M %p"

@app.route('/users')
def index():
    mysql = connectToMySQL('SemiRestfulUsers')
    query = mysql.query_db('SELECT * FROM users;')
    print(query)
    return render_template('index.html', allUsers = query, dtf = createFormat)

@app.route('/users/new')
def createPage():
    return render_template('create.html')

@app.route('/users/create', methods = ["POST"])
def createUser():
    print(request.form)
    mysql = connectToMySQL('SemiRestfulUsers')
    query = "INSERT INTO users (first_name, last_name, email, created_at) VALUES (%(fn)s, %(ln)s, %(e)s, NOW());"
    data = {
        "fn": request.form["firstName"],
        "ln": request.form["lastName"],
        "e": request.form["email"]
    }
    newUser = mysql.query_db(query, data)
    print(newUser)
    return redirect('/users')

@app.route('/users/<user_id>')
def show(user_id):
    query = ('SELECT * FROM users WHERE id = %(id)s;')
    data = {
        "id" : user_id
    }
    mysql = connectToMySQL('SemiRestfulUsers')
    thisUser = mysql.query_db(query, data)
    print(thisUser)
    return render_template('show.html', users = thisUser, ctf = createFormat, utf = updateFormat)

@app.route('/users/<user_id>/edit')
def delete(user_id):
    query = ('SELECT * FROM users WHERE id = %(id)s;')
    data = {
        "id" : user_id
    }
    mysql = connectToMySQL('SemiRestfulUsers')
    thisUser = mysql.query_db(query, data)
    print(thisUser)
    return render_template('show.html', users = thisUser, ctf = createFormat, utf = updateFormat)

@app.route('/users/<user_id>/delete')
def delete(user_id):
    query = ('DELETE * FROM users where id = %(id)s;')
    data = {
        'id': user_id
    }
    mysql = connectToMySQL('SemiRestfulUsers')
    toDelete = mysql.query_db(query, data)
    print(toDelete)
    return redirect('/users')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return 'Invalid URL.'
if __name__=="__main__":
    app.run(debug=True)