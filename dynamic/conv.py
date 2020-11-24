from flask import Flask
app = Flask(__name__)

@app.route('/user/<name>')
def show_user(name):
    return 'My name is %s' % name

@app.route('/age/<int:age>')
def show_age(age):
    return 'age is %d' % age

@app.route('/price/<float:price>')
def show_price(price):
    return 'price is %f' % price

@app.route('/path/<path:name>')
def show_path(name):
    return 'path is %s' % name

app.run()
