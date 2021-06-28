from flask import Flask

helloWorldapp = Flask(__name__)

@helloWorldapp.route('/')
def hello_world():
    return 'Hello... World.'

@helloWorldapp.route('/dojo')
def success():
    return "Dojo"

@helloWorldapp.route('/say/<name>')
def hello(name):
    if type(name) == str:
        return "Hi " + name + "!"
    else:
        return "Strings Only"

@helloWorldapp.route('/repeat/<num>/<word>')
def show_user_profile(num, word):
    if num.isdigit() and type(word) == str:
        return word * int(num)

@helloWorldapp.route('/', defaults={'path': ''})
@helloWorldapp.route('/<path:path>')
def catch_all(path):
    return 'Sorry! No response. Try again.'










if __name__=="__main__":
    helloWorldapp.run(debug=True)
