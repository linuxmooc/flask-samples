from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    print('execute request')
    return 'Hello World'

@app.before_first_request
def before_first_request():
    print('before_first_request')

@app.before_request
def before_request():
    print('before_request')

@app.after_request
def after_request(response):
    print('after_request')
    return response

if __name__ == '__main__':
    app.run()
