from flask import Flask, render_template
playground = Flask(__name__)

@playground.route('/play')
def blue3():
    return render_template('index.html', times=3 )

@playground.route('/play/<num>')
def blueX(num):
    # if num.isdigit():
    return render_template('index.html', times=int(num) )

@playground.route('/play/<num>/<color>')
def colorX(num, color):
    if num.isdigit() and type(color) == str:
        return render_template('index.html', times=int(num), color=color )

@playground.route('/', defaults={'path': ''})
@playground.route('/<path:path>')
def catch_all(path):
    return 'Invalid URL.'
if __name__=="__main__":
    playground.run(debug=True)