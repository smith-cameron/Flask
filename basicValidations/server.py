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
    # print(request.form)
    if len(request.form['userName']) < 1:
        flash("Name Required")
    if len(request.form['locId']) < 1:
        flash("Location Required")
    if len(request.form['langId']) < 1:
        flash("Language Required")
    if request.form['comment']:
        if len(request.form['comment']) < 5 and len(request.form['comment']) > 0:
            flash("Comment Must Be Over 5 Characters")
    if not '_flashes' in session.keys():
        mysql = connectToMySQL('basicValidations')
        query = "INSERT INTO ninjas (UserName, locId, langId, comment, createdAt) VALUES (%(n)s, %(lo)s, %(la)s, %(com)s, NOW());"
        input = {
            "n" : request.form["userName"],
            "lo" : request.form["locId"],
            "la" : request.form["langId"],
            "com" : request.form["comment"],
        }
        ninja = mysql.query_db(query, input)
        # print(f"ninjaID: {ninja}")
        return redirect(f'/success/{ninja}')
    return redirect('/')

@app.route('/success/<int:id>')
def resultsRender(id):
    mysql = connectToMySQL('basicValidations')
    query = ('SELECT n.userName, n.comment, lo.name, la.name FROM ninjas n JOIN locations lo ON n.id = lo.id JOIN languages la ON n.id = la.id WHERE n.id = %(n)s;')
    input = {
        "n" : id
    }
    thisNinja = mysql.query_db(query, input)
    print(f"This Ninja: {thisNinja}")
    return render_template('show.html', ninja = thisNinja)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return 'Invalid URL.'
if __name__=="__main__":
    app.run(debug=True)