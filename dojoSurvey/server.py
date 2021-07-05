from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'secret_keyy'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def results():
    print(request.form)
    return render_template('result.html',
    name = request.form['userName'],
    location = request.form['location'],
    language = request.form['language'],
    comment = request.form['comment'])

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return 'Invalid URL.'
if __name__=="__main__":
    app.run(debug=True)