from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', row=int(8), col=int(8))

@app.route('/<x>')
def resizeRow(x):
    return render_template('index.html', row=int(x),col=int(8))

@app.route('/<x>/<y>')
def resizeRowCol(x, y):
    return render_template('index.html', row=int(x),col=int(y))

@app.route('/<x>/<y>/<c1>/<c2>')
def resize_with_color(x, y, c1, c2):
    return render_template('index.html', row=int(x), col=int(y), color1=c1, color2=c2)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return 'Invalid URL.'
if __name__=="__main__":
    app.run(debug=True)