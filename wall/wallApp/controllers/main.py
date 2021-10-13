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
        thisUserId = session['userId']
        data = {
            "i" : thisUserId
            }
        thisUser = User.findById(data)
        followerIds = User.getFollowers(data)
        allButMe = User.getAllButOne(data)
        allUsers = User.getAll()
        thisUsersPosts = Post.findByUserId(data)
        sentCount = Post.sentPostsCount(data)
        recievedCount = Post.recievedPostCount(data)
        return render_template('landing.html', users = allButMe, user = thisUser, myPosts = thisUsersPosts, sent = sentCount, recieved = recievedCount, dtf = dateFormat, followers = followerIds)
    return redirect('/')

@app.route('/follow/<int:toFollow>')
def follow(toFollow):
    if 'userId' in session:
        loggedUserId = session['userId']
        data = {
            "i" : loggedUserId,
            "z" : toFollow
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
        loggedUserId = session['userId']
        data = {
            "i" : loggedUserId
            }



# landing.html
    # All users/ whos logged in 
        # Like/Unlike User/Make Friends
    # Recent posts(since last login)
        # to your wall
        # to other walls
    # Pictures??
    # links to 
        # Edit Your User Info - Validate
# Post dashboard.html 
    # Like/Unlike Post
    # Like/Unlike Comments
    # Edit Post - Validate
    # Comment on Posts - Validate
        # Edit Comments - Validate
        # Delete Comments

