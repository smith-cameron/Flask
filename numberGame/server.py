from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'secret_keyy'

@app.route('/')
def index():
    # winningNum = random.randint(1, 100)
    # print(winningNum)
    if 'turns' not in session:
        session['turns'] = 0
        session['correct_guesses'] = 0
        session['wrong_guesses'] = 0
        session['prev_guesses'] = []
        session['num'] = random.randint(1, 100)
    # session['num'] = winningNum
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def processForm():
    #This Method always returns false
    session['prev_guesses'].append(request.form['guess'])
    session['turns']+=1
    print(request.form['guess'])
    print(session['num'])
    if request.form['guess'] == session['num']:
        session['result'] = True
        session['correct_guesses']+=1
        print(session['result'])
        # return redirect("/results")
    else:
        session['result'] = False
        session['wrong_guesses']+=1
        print(session['result'])
    return redirect("/results")


@app.route('/results')
def results():
    win_percentage = session['correct_guesses']// session['turns']
    return render_template('results.html', percent = win_percentage)

@app.route('/reset')
def resetGame():
    session.clear()
    return redirect("/")

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return 'Invalid URL.'
if __name__=="__main__":
    app.run(debug=True)