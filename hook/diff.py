from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    print('execute request without error')
    return 'Hello World'

@app.route('/error')
def error():
    print('execute request with error')
    1 / 0
    return 'Hello World'

@app.after_request
def after_request(response):
    print('after_request')
    return response

@app.teardown_request
def teardown_request(response):
    print('teardown_request')
    return response

if __name__ == '__main__':
    app.run()
