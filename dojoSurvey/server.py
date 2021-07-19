from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'secret_keyy'

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/post', methods=['POST'])
# def postData():
#     print(request.form)
#     return render_template('result.html',
#     name = request.form['userName'],
#     location = request.form['location'],
#     language = request.form['language'],
#     comment = request.form['comment'])

@app.route('/post', methods=['POST'])
def postData():
    print(request.form)
    session['userName'] = request.form['userName']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/result')

@app.route('/result')
def results():
    return render_template('result.html',
    language = session['language'],
    comment = session['comment'])

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return 'Invalid URL.'
if __name__=="__main__":
    app.run(debug=True)