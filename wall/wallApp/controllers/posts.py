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
def postDashboard():
    if 'userId' in session:
        thisUserId = session['userId']
        data = {
                "i" : thisUserId
            }
        return render_template('postDashboard.html', users = User.getAllButOne(data), user = User.findById(data), sentPosts = Post.findSentByUserId(data), recievedPosts = Post.findRecievedByUserId(data), sentCount = Post.sentPostsCount(data), recievedCount = Post.recievedPostCount(data), dtf = dateFormat)
    return redirect('/')

@app.route('/post/send', methods=['POST'])
def post():
    if 'userId' in session:
        if Post.validatePost(request.form):
            creator = session['userId']
            print(request.form)
            data = {
                    "c" : request.form['contnt'],
                    "ci" : creator,
                    "ri" : request.form['recipientId']
                }
            Post.save(data)
            return redirect('/posts')
        return redirect('/posts')
    return redirect('/')

@app.route('/post/delete/<int:id>')
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