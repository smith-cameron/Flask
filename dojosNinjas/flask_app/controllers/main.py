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
            "name" : request.form['name']
    }
	print(Dojo.save(data))
	return redirect('/dojos')

@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html', dojos = Dojo.getAll())

@app.route('/ninjas',methods=['POST'])
def createNinja():
    print(request.form)
    data = {
            "firstName" : request.form['firstName'].capitalize(),
            "lastName" : request.form['lastName'].capitalize(),
            "age" : request.form['age'],
            "dojoId" : request.form['dojoId']
    }
    Ninja.save(data)
    dojoId = data['dojoId']
    return redirect(f'/dojos/{dojoId}')

@app.route('/dojos/<int:id>')
def showDojo(id):
    data = {
        "id" : id
    }
    print(Dojo.getDojoJoinNinjas(data))
    print(Dojo.getDojoJoinNinjas(data).ninjas)
    return render_template('dojoInfo.html', dojo = Dojo.getDojoJoinNinjas(data), dtf = dateFormat)

