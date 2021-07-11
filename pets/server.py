from flask import Flask, render_template, request, redirect, session
from mysqlDB import connectToMySQL

app = Flask(__name__)
app.secret_key = 'secret_keyy'



@app.route('/')
def index():
    mysql = connectToMySQL('Pets')
    myPets = mysql.query_db('SELECT * FROM pets;')
    print(myPets)
    return render_template('index.html', allMyPets = myPets)

@app.route('/addPet', methods=["POST"])
def addPet():
    print(request.form)
    mysql = connectToMySQL('Pets')
    query = "INSERT INTO pets (name, type, created_at, updated_at) VALUES (%(n)s, %(t)s, NOW(), NOW());"
    input = {
        "n" : request.form["name"],
        "t" : request.form["type"]
    }
    newFriendID = mysql.query_db(query, input)
    return redirect("/")


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return 'Invalid URL.'
if __name__=="__main__":
    app.run(debug=True)