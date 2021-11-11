from flask import Flask, render_template, request, redirect, session, flash
from mysqlDB import connectToMySQL    # import the function that will return an instance of a connection
app = Flask(__name__)
app.secret_key = 'Dont take any wooden nickles.'
myDB = 'firstFlask'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/repeat')
def passingData():
    return render_template("helloWorld.html", phrase="Houston, we have a problem", times=5)

@app.route('/lists')
def renderLists():
    studentInfo = [
        {'name' : 'Michael', 'age' : 35},
        {'name' : 'John', 'age' : 30 },
        {'name' : 'Mark', 'age' : 25},
        {'name' : 'KB', 'age' : 27}
    ]
    return render_template("lists.html", randomNumbers = [3,1,5], students = studentInfo)

@app.route('/form')
def formGet():
    return render_template('form.html')

@app.route('/form', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    if request.form['action'] == 'register':
        session['username'] = request.form['name']
        session['useremail'] = request.form['email']
    elif request.form['action'] == 'login':
        session['loginEmail'] = request.form['email']
        session['loginPass'] = request.form['password']
    return redirect("/show")

@app.route('/show')
def showUser():
    print("Showing the User Info From the Form")
    print(request.form)
    return render_template('show.html')

@app.route("/friends")
def showFriends():
    mysql = connectToMySQL(myDB)   # call the function, passing in the name of our db
    friends = mysql.query_db('SELECT * FROM users;')  # call the query_db function, pass in the query as a string
    print(friends)
    return render_template("friends.html", allFriends = friends)

# @app.route("/createFriend", methods=["POST"])
# def addFriend():
#     print(request.form)
#     mysql = connectToMySQL(myDB)
#     query = "INSERT INTO users (first_name, last_name, email, occupation, created_at, updated_at) VALUES (%(fn)s, %(ln)s, %(em)s, %(occup)s, NOW(), NOW());"
#     input = {
#         "fn" : request.form["fname"],
#         "ln" : request.form["lname"],
#         "em" : request.form["email"],
#         "occup" : request.form["occ"],
#     }
#     newFriendID = mysql.query_db(query, input)
#     return redirect("/friends")

@app.route('/createFriend', methods=['POST'])
def addFriendValidated():
    #is_valid = True		# assume True
    if len(request.form['fname']) < 1:
        #is_valid = False
        flash("First Name Required")
    if len(request.form['lname']) < 1:
        #is_valid = False
        flash("Last Name Required")
    if len(request.form['email']) < 1:
        #is_valid = False
        flash("Email Required")
    if len(request.form['occ']) < 2:
        #is_valid = False
        flash("Occupation Required. Must be longer than 2 characters.")
    #if is_valid:
    if not '_flashes' in session.keys():
        print(request.form)
        mysql = connectToMySQL(myDB)
        query = "INSERT INTO users (first_name, last_name, email, occupation, created_at, updated_at) VALUES (%(fn)s, %(ln)s, %(em)s, %(occup)s, NOW(), NOW());"
        input = {
            "fn" : request.form["fname"],
            "ln" : request.form["lname"],
            "em" : request.form["email"],
            "occup" : request.form["occ"],
        }
        newFriendID = mysql.query_db(query, input)
        flash("Friend successfully added!")
        return redirect('/friends')
    return redirect('/')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return 'Invalid URL.'
if __name__=="__main__":
    app.run(debug=True)