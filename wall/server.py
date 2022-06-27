from wallApp import app
from wallApp.controllers import main, loginReg, posts



@app.route('/', defaults={'pizza': ''})
@app.route('/<path:pizza>')
def catch_all(pizza):
    return 'Invalid URL.'


if __name__=="__main__":
    app.run(debug=True)