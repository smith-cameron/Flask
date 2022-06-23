from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'secret_keyy'

@app.route('/')
def index():
    if 'count' not in session:
        session['count'] = 1
        # session['dd'] = 1
        # print("count: {}".format(session['count']))
        # print("dd: {}".format(session['dd']))
    else:
        session['count'] += 1
        # session['dd'] = session['count']
        # print("count: {}".format(session['count']))
        # print("dd: {}".format(session['dd']))
    return render_template('index.html')

@app.route('/reset')
def reset():
    session.clear()
    return redirect("/")

@app.route('/twice')
def doubleDown():
    if session['dd'] == session['count']:
        session['count'] += 2
        # session['dd'] = session['count']
        print("count: {}".format(session['count']))
        print("dd: {}".format(session['dd']))
        return render_template('index.html')
    return redirect("/")

# @app.route('/form', methods=['POST'])
# def buttons():
#     if request.form['action'] == 'reset':
#         session.clear()
#         return redirect("/")
#     elif request.form['action'] == 'twice':
#         session['count'] += 2
#         print(session['count'])
#         return render_template('index.html')


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return 'Invalid URL.'
if __name__=="__main__":
    app.run(debug=True)