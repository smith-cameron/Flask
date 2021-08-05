from friendsApp import app
from flask import Flask
from flask import render_template, request, redirect, session, flash
from friendsApp.models.user import User
from friendsApp.models.friendship import Friendship
from datetime import datetime
dateFormat = "%m/%d/%Y"



@app.route('/')
def index():
    allUsers = User.getAll()
    allfriends = Friendship.getAll()
    # print(allUsers)
    print(allfriends)
    return render_template('index.html', users = allUsers, allFriends = allfriends)

@app.route('/create',methods=['POST'])
def createUser():
	data = {
            "fn" : request.form['firstName'],
            "ln" : request.form['lastName']
    }
	print(User.save(data))
	return redirect('/')

@app.route('/',methods=['POST'])
def createFriendship():
    data = {
            "ui" : request.form['userId'],
            "fi" : request.form['friendId']
    }
    print(Friendship.save(data))
    return redirect('/')


@app.route('/logout')
def sessionReset():
    session.clear()
    return redirect("/")
