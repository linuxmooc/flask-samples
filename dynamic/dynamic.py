from flask import Flask
app = Flask(__name__)

@app.route('/user/<name>')
def show_user(name):
    return 'My name is %s' % name

app.run()
