from wallApp import app
from wallApp.controllers import main, loginReg, posts



@app.route('/', defaults={'cookies': ''})
@app.route('/<path:cookies>')
def catch_all(cookies):
    return 'Invalid URL.'
if __name__=="__main__":
    app.run(debug=True)