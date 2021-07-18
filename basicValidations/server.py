from flask import Flask, render_template, request, redirect, session, flash
from mysqlDB import connectToMySQL
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'secret_keyy'
dateFormat = "%m/%d/%Y"

@app.route('/')
def index():
    mysql = connectToMySQL('basicValidations')
    locs = mysql.query_db('SELECT * FROM locations;')
    mysql = connectToMySQL('basicValidations')
    langs = mysql.query_db('SELECT * FROM languages;')
    mysql = connectToMySQL('basicValidations')
    allNinjas = mysql.query_db('SELECT * FROM ninjas;')
    # print(locs)
    # print(langs)
    return render_template('index.html', locations = locs, languages = langs, ninjas = allNinjas)

@app.route('/postData', methods=['POST'])
def create():
    if len(request.form['userName']) < 1:
        flash("Name Required")
    if request.form['location'] == 0:
        flash("Location Required")
    if request.form['language'] == 0:
        flash("Language Required")
    if request.form['comment']:
        if len(request.form['comment']) < 5 and len(request.form['comment']) > 0:
            flash("Comment Must Be Over 10 Characters")
    if not '_flashes' in session.keys():
        # print(request.form)
        mysql = connectToMySQL('basicValidations')
        query = "INSERT INTO ninjas (UserName, locId, langId, comment, createdAt) VALUES (%(n)s, %(lo)s, %(la)s, %(com)s, NOW());"
        input = {
            "n" : request.form["userName"],
            "lo" : request.form["location"],
            "la" : request.form["language"],
            "com" : request.form["comment"],
        }
        ninja = mysql.query_db(query, input)
        return redirect(f'/success/{ninja}')
    return redirect('/')

@app.route('/success/<id>')
def resultsRender(id):
    mysql = connectToMySQL('basicValidations')
    query = ('SELECT * FROM ninjas WHERE id = %(n)s;')
    input = {
        "n" : id
    }
    thisNinja = mysql.query_db(query, input)
    print(thisNinja)
    mysql = connectToMySQL('basicValidations')
    query = ('SELECT locId FROM ninjas WHERE id = %(n)s;')
    thisLoc = mysql.query_db(query, input)
    print(thisLoc)
    mysql = connectToMySQL('basicValidations')
    query = ('SELECT name FROM locations WHERE id = %(n)s;')
    input = {
        "n" : thisLoc
    }
    locName = mysql.query_db(query, input)
    print(locName)
    mysql = connectToMySQL('basicValidations')
    thisLang = mysql.query_db('SELECT * FROM languages;')
    return render_template('result.html', ninja = thisNinja)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return 'Invalid URL.'
if __name__=="__main__":
    app.run(debug=True)