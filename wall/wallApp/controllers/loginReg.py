from wallApp import app
from flask import Flask
from flask import render_template, request, redirect, session, flash
from wallApp.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from datetime import datetime
dateFormat = "%m/%d/%Y %-I:%M %p"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register',methods=['POST'])
def register():
    if User.validateRegistration(request.form) and User.uniqueEmail({ "e" : request.form['email']}):
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
        return redirect('/landing')
    return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    data = { "e" : request.form["email"] }
    user = User.getByEmail(data)
    if user:
        if bcrypt.check_password_hash(user.password, request.form['password']):
            session['userId'] = user.id
            # Save email to session
            return redirect("/landing")
        flash("**Invalid Email/Password Input**", 'loginError')
        return redirect('/')
    flash("**Invalid Email/Password Input**", 'loginError')
    return redirect("/")

@app.route('/logout')
def sessionReset():
    session.clear()
    return redirect("/")