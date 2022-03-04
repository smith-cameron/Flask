from recipeApp import app
from flask import Flask
from flask import render_template, request, redirect, session, flash
from recipeApp.controllers import loginReg
from recipeApp.models.user import User
from recipeApp.models.recipe import Recipe
from datetime import datetime
dateFormat = "%m/%d/%Y"

@app.route('/home')
def dashboard():
    if 'userId' in session:
        thisUserId = session['userId']
        data = {
                "i" : thisUserId
            }
        return render_template('dashboard.html', recipes = Recipe.getAll(), user = User.findById(data), dtf = dateFormat)
    return redirect('/')

@app.route('/create')
def renderCreate():
    if 'userId' in session:
        data = {
                "i" : session['userId']
            }
        return render_template('recipeNew.html', user =  User.findById(data))
    return redirect('/')

@app.route('/create',methods=['POST'])
def createRecipe():
    if 'userId' in session:
        if Recipe.validate(request.form):
            data = {
                "name" : request.form['name'].title(),
                "d" : request.form['desc'],
                "i" : request.form['inst'],
                "lm" : request.form['lastMade'],
                "tl" : request.form['timeLimit'],
                "c" : request.form['creator']
            }
            Recipe.save(data)
            return redirect('/home')
        return redirect('/create')
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

@app.route('/recipe/<int:id>/delete')
def deleteRecipe(id):
    if 'userId' in session:
        data = {
                "i" : id
            }
        Recipe.deleteById(data)
        return redirect("/home")
    return redirect('/')

@app.route('/recipe/<int:id>/edit')
def editRecipe(id):
    if 'userId' in session:
        thisUserId = session['userId']
        rdata = {
                "i" : id
            }
        data = {
                "i" : thisUserId
            }
        thisRecipe = Recipe.findById(rdata)
        thisUser = User.findById(data)
        return render_template('recipeEdit.html', recipe = thisRecipe, user = thisUser)
    return redirect('/')

@app.route('/recipe/<int:id>')
def showRecipe(id):
    if 'userId' in session:
        thisUserId = session['userId']
        rdata = {
                "i" : id
            }
        data = {
                "i" : thisUserId
            }
        Recipe.findById(rdata)
        thisUser = User.findById(data)
        thisRecipe = Recipe.findByIdJoinCreator(rdata)
        return render_template('recipeDisplay.html', recipe = thisRecipe, user = thisUser, dtf = dateFormat)
    return redirect('/')

@app.route('/logout')
def logOut():
    if 'userId' in session:
        session.clear()
        return redirect("/")
    return redirect('/')
