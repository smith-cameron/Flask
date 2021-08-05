from flask_app import app
from flask import Flask
from flask import render_template, request, redirect, session, flash
from flask_app.models.user import User
from datetime import datetime
dateFormat = "%m/%d/%Y"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/',methods=['POST'])
def createUser():
    if User.validateUser(request.form):
        data = {
        "e" : request.form['email']
        }
        userId = User.save(data)
        print(userId)
        return redirect(f'/home/{userId}')
    return redirect('/')


@app.route('/home/<int:id>')
def landing(id):
    data = {
        "i" : id
    }
    currentUser = User.findById(data)
    allUsers = User.getAll()
    print(allUsers)
    return render_template('landing.html', allUsers = allUsers, user = currentUser, dtf = dateFormat    )