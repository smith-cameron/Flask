from flask import Flask, render_template, request, redirect, session
from mysqlconnection import connectToMySQL

app = Flask(__name__)
app.secret_key = 'secret_keyy'
mysql = connectToMySQL('initflask')
users = mysql.query_db('SELECT * FROM users;')

@app.route('/')
def index():
    print(users)
    return render_template('index.html')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return 'Invalid URL.'
if __name__=="__main__":
    app.run(debug=True)