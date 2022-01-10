from flask_app import app
from flask import Flask
from flask import render_template, request, redirect, session, flash
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from datetime import datetime
dateFormat = "%m/%d/%Y %I:%M %p"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register',methods=['POST'])
def register():
    if User.validateRegistration(request.form):
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        data = {
            "fn" : request.form['firstName'].capitalize(),
            "ln" : request.form['lastName'].capitalize(),
            "e" : request.form['email'],
            "p" : pw_hash
        }
        
        userId = User.save(data)
        session['userId'] = userId
        print(session['userId'])
        return redirect('/home')
    return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    data = { "email" : request.form["email"] }
    user = User.getByEmail(data)
    if not user:
        flash("Invalid Email/Password Input", 'loginError')
        return redirect("/")
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid Email/Password Input", 'loginError')
        return redirect('/')
    session['userId'] = user.id
    return redirect("/home")

@app.route('/home')
def dashboard():
    if 'userId' in session:
        thisUserId = session['userId']
        data = {
                "i" : thisUserId
            }
        thisUser = User.findById(data)
        allUsers = User.getAll()
        print(thisUser)
        return render_template('dashboard.html', users = allUsers, user = thisUser, dtf = dateFormat)
    return redirect('/')

@app.route('/user/<int:id>/delete')
def deleteUser(id):
    if 'userId' in session:
        data = {
                "i" : id
            }
        User.deleteById(data)
        return redirect("/home")
    return redirect('/')

@app.route('/logout')
def sessionReset():
    if 'userId' in session:
        session.clear()
        return redirect("/")
    return redirect('/')
