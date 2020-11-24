from flask import Flask
app = Flask(__name__)

@app.route('/user/tom')
def show_user_tom():
    return 'My name is tom'

@app.route('/user/jerry')
def show_user_jerry():
    return 'My name is jerry'

@app.route('/user/mike')
def show_user_mike():
    return 'My name is mike'

app.run()
