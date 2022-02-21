from wallApp import app
from flask import Flask
from flask import render_template, request, redirect, session, flash
from wallApp.models.user import User
from wallApp.models.post import Post
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from datetime import datetime
dateFormat = "%m/%d/%Y %-I:%M %p"

@app.route('/landing')
def landingDashboard():
    if 'userId' in session:
        data = {
            "i" : session['userId']
            }
        return render_template('landing.html', 
        users = User.getAllButOne(data), 
        user = User.findById(data), 
        myPosts = Post.findRecievedByUserId(data), 
        sent = Post.sentPostsCount(data), 
        recieved = Post.recievedPostCount(data), 
        dtf = dateFormat, 
        followers = User.getFollowers(data))
    return redirect('/')

@app.route('/follow/<int:followed>')
def follow(followed):
    if 'userId' in session:
        data = {
            "i" : session['userId'],
            "z" : followed
            }
        User.follow(data)
        return redirect('/landing')
    return redirect('/')

@app.route('/unfollow/<int:toUnFollow>')
def unFollow(toUnFollow):
    if 'userId' in session:
        data = {      
                "z" : toUnFollow
            }
        User.unfollow(data)
        return redirect('/landing')
    return redirect('/')

@app.route('/user/edit')
def edidUser():
    if 'userId' in session:
        data = {
            "i" : session['userId']
            }
        return render_template('editUser.html', 
        user = User.findById(data) )
    return redirect('/')

@app.route('/user/edit', methods=['POST'])
def edidUserPOST():
    if 'userId' in session:
        if request.form['email'] != User.findById({"i" : session['userId']}).email:
            if not User.uniqueEmail({ "e" : request.form['email']}):
                return redirect('/user/edit')
        if User.validateUserUpdate(request.form) :
            data = {
                "fn" : request.form['firstName'].capitalize(),
                "ln" : request.form['lastName'].capitalize(),
                "e" : request.form['email'],
                "i" : session['userId']
            }
            User.findById({"i" : session['userId']}).updateUser(data)
            return redirect('/user/edit')
        return redirect('/user/edit')
    return redirect('/')

# landing.html
    # All users/ whos logged in 
        # Like/Unlike User/Make Friends
    # Select a user to see their wall
    # Private messaging
    # Recent posts(since last login)
        # to your wall
        # to other walls
    # Pictures??
    # links to 
        # Edit Your Password - Validate
# Post dashboard.html 
    # Like/Unlike Post
    # Like/Unlike Comments
    # Edit Post - Validate
    # Comment on Posts - Validate
        # Edit Comments - Validate
        # Delete Comments

