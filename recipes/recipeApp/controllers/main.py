from recipeApp import app
from flask import Flask
from flask import render_template, request, redirect, session, flash
from recipeApp.controllers import loginReg
from recipeApp.models.user import User
from recipeApp.models.recipe import Recipe
from datetime import datetime
dateFormat = "%m/%d/%Y %-I:%M %p"

@app.route('/home')
def dashboard():
    if 'userId' in session:
        thisUserId = session['userId']
        data = {
                "i" : thisUserId
            }
        thisUser = User.findById(data)
        allRecipes = Recipe.getAll()
        print(thisUser)
        return render_template('dashboard.html', recipes = allRecipes, user = thisUser, dtf = dateFormat)
    return redirect('/')

@app.route('/create')
def renderCreate():
    if 'userId' in session:
        thisUserId = session['userId']
        data = {
                "i" : thisUserId
            }
        thisUser = User.findById(data)
        return render_template('recipeNew.html', user = thisUser)
    return redirect('/')

@app.route('/create',methods=['POST'])
def createRecipe():
    print(request.form)
    if Recipe.validate(request.form):
        data = {
            "n" : request.form['name'].title(),
            "d" : request.form['desc'],
            "i" : request.form['inst'],
            "lm" : request.form['lastMade'],
            "tl" : request.form['timeLimit'],
            "c" : request.form['creator']
        }
        recipeId = Recipe.save(data)
        print(recipeId)
        return redirect('/home')
    return redirect('/create')

@app.route('/user/<int:id>/delete')
def deleteUser(id):
    if 'userId' in session:
        data = {
                "i" : id
            }
        User.deleteById(data)
        return redirect("/home")
    return redirect('/')

@app.route('/recipe/<int:id>/delete')
def deleteRecipe(id):
    if 'userId' in session:
        data = {
                "i" : id
            }
        Recipe.deleteById(data)
        return redirect("/home")
    return redirect('/')

@app.route('/logout')
def logOut():
    if 'userId' in session:
        session.clear()
        return redirect("/")
    return redirect('/')
