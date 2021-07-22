from flask import Flask, render_template, request, redirect, session, flash
from mysqlDB import connectToMySQL
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'secret_keyy'
dateFormat = "%m/%d/%Y"

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/', methods = ['POST'])
def postReg():
    print(request.form['password'])
    print(request.form['passConf'])
    if len(request.form['firstName']) < 1:
        flash("First Name Required")
    if len(request.form['lastName']) < 1:
        flash("Last Name Required")
    if len(request.form['password']) < 1:
        flash("Password Required")
    if len(request.form['password']) < 5:
        flash("Password Must Be Over 5 Characters")
    if len(request.form['passConf']) < 1:
        flash("Password Confirmation Required")
    if request.form['password'] != request.form['passConf']:
        flash("Password Inputs Must Match")
    if not '_flashes' in session.keys():
        mysql = connectToMySQL('basicReg')
        query = "INSERT INTO users (firstName, lastName, password, createdAt) VALUES (%(fn)s, %(ln)s, %(p)s, NOW());"
        input = {
            "fn" : request.form["firstName"],
            "ln" : request.form["lastName"],
            "p" : request.form["password"],
        }
        newUser = mysql.query_db(query, input)
        print(f"newUser: {newUser}")
        return redirect(f'/land/{newUser}')
    return redirect('/')

@app.route('/land/<int:id>')
def landing(id):
    mysql = connectToMySQL('basicReg')
    query = mysql.query_db('SELECT * FROM users WHERE id = %(n)s;')
    input = {
        "n" : id
    }
    thisUser = mysql.query_db(query, input)
    print(thisUser)
    return render_template('landing.html', user = thisUser)

@app.route('/logout')
def sessionReset():
    session.clear()
    return redirect("/")

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return 'Invalid URL.'
if __name__=="__main__":
    app.run(debug=True)