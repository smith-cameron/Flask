from wallApp import app
from flask import Flask
from flask import render_template, request, redirect, session, flash
from wallApp.models.user import User
from wallApp.models.post import Post
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from datetime import datetime
dateFormat = "%m/%d/%Y %-I:%M %p"

@app.route('/posts')
def messageDashboard():
    if 'userId' in session:
        thisUserId = session['userId']
        data = {
                "i" : thisUserId
            }
        thisUser = User.findById(data)
        allButMe = User.getAllButOne(data)
        allUsers = User.getAll()
        thisUsersPosts = Post.findByUserId(data)
        sentCount = Post.sentPostsCount(data)
        recievedCount = Post.recievedPostCount(data)
        return render_template('dashboard.html', users = allButMe, user = thisUser, myPosts = thisUsersPosts, sent = sentCount, recieved = recievedCount, dtf = dateFormat)
    return redirect('/')

@app.route('/send', methods=['POST'])
def post():
    if 'userId' in session:
        if Post.validatePost(request.form):
            creator = session['userId']
            data = {
                    "c" : request.form['content'],
                    "ci" : creator,
                    "ri" : request.form['recipientId']
                }
            Post.save(data)
            return redirect('/posts')
        return redirect('/posts')
    return redirect('/')

@app.route('/deletepost/<int:id>')
def deletePost(id):
    if 'userId' in session:
        data = {
                "i" : id
            }
        thisMessage = Post.findById(data)
        if session['userId'] == thisMessage.recipientId:
            Post.deleteById(data)
            return redirect('/posts')
        return redirect('/')
    return redirect('/')