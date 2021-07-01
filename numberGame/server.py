from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'secret_keyy'

winningNum = random.randint(1, 100)
print(winningNum)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return 'Invalid URL.'
if __name__=="__main__":
    app.run(debug=True)