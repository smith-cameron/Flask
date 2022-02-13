from flask_app import app
from flask import Flask
from flask import render_template, request, redirect, session, flash
from flask_app.models.Dojo import Dojo
from flask_app.models.Ninja import Ninja
from datetime import datetime
dateFormat = "%m/%d/%Y %I:%M %p"

@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    return render_template('dojos.html', dojos = Dojo.getAll(), dtf = dateFormat)

@app.route('/dojos',methods=['POST'])
def createDojo():
	data = {
            "n" : request.form['name']
    }
	print(Dojo.save(data))
	return redirect('/')

@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html', dojos = Dojo.getAll())

@app.route('/ninjas',methods=['POST'])
def createNinja():
    data = {
            "fn" : request.form['firstName'],
            "ln" : request.form['lastName'],
            "a" : request.form['age'],
            "d" : request.form['dojoId']
    }
    Ninja.save(data)
    dojoId = data['d']
    return redirect(f'/dojos/{dojoId}')

@app.route('/dojos/<int:id>')
def showDojo(id):
    data = {
            "i" : id
    }
    return render_template('dojoInfo.html', dojo = Dojo.getById(data), ninjas = Dojo.getNinjas(data), dtf = dateFormat)


@app.route('/logout')
def sessionReset():
    session.clear()
    return redirect("/")
