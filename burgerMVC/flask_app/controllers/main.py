from flask_app import app
from flask import Flask
from flask import render_template, request, redirect, session, flash
from flask_app.models.burger import Burger
from flask_app.models.restaurant import Restaurant
from datetime import datetime

from flask_app.models.topping import Topping
dateFormat = "%a %d/%m/%Y @ %I:%M %p"

@app.route('/')
def index():
    return redirect('/burgers')

@app.route('/burgers')
def burgers():
	return render_template('index.html',burgers=Burger.getAll(), restaurants=Restaurant.getAll(), dtf=dateFormat, toppings=Topping.getAll())

@app.route('/create/burger',methods=['POST'])
def create_burger():
	data = {
            "name" : request.form['name'],
            "bun" : request.form['bun'],
            "meat" : request.form['meat'],
            "temp" : request.form['temp'],
            "restaurantId" : request.form['restaurantId']
	}
	Burger.save(data)
	return redirect('/burgers')

@app.route('/restaurant/<int:id>')
def restaurantJoinBurgerWithToppings(id):
    data = {
        "id" : id
	}
    return render_template('show.html', restaurant=Restaurant.getByIdJoinBurgers(data), dtf=dateFormat)
