from flask_app import app
from flask import Flask
from flask import render_template, request, redirect, session, flash
from flask_app.models.user import User
from datetime import datetime
dateFormat = "%m/%d/%Y"

@app.route('/register', methods=['POST'])
def register():
    if not User.validate_user(request.form):
        return redirect('/')
    # ... do other things
    return redirect('/dashboard')

@app.route('/')
def index():
    allUsers = User.getAll()
    print(allUsers)
    return render_template('index.html', users = allUsers)

@app.route('/create',methods=['POST'])
def createUser():
	data = {
            "fn" : request.form['firstName'],
            "ln" : request.form['lastName'],
            "e" : request.form['email'],
            "p" : request.form['password']
    }
	print(User.save(data))
	return redirect('/')

@app.route('/logout')
def sessionReset():
    session.clear()
    return redirect("/")
