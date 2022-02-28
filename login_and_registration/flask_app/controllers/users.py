from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User
from flask_app.models.recipe import Recipe

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/create',methods=['POST'])
def create():
    if not User.validate_user(request.form):
        return redirect('/')
    password_hash = bcrypt.generate_password_hash(request.form['password'])
    print(password_hash)
    confirm_password_hash = bcrypt.generate_password_hash(request.form['confirm_password'])
    data = {
        "first_name":request.form['first_name'],
        "last_name":request.form['last_name'],
        "email":request.form['email'],
        "password":password_hash,
        "confirm_password":confirm_password_hash
    }
    id = User.save(data)
    session['user_id'] = id
    return redirect('/dashboard')

@app.route('/login',methods=['POST'])
def login():
    data = { "email": request.form["email"] }
    user_in_db = User.get_by_email(data)
    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.password,request.form['password']):
        flash("Invalid Email/Password")
        return redirect('/')
    session['user_id'] = user_in_db.id
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/logout')
    data = { 'id':session['user_id'] }
    return render_template("dashboard.html",user=User.get_by_id(data),recipes=Recipe.get_all_recipes())

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')