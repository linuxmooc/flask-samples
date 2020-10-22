from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    print('execute request')
    return 'Hello World'

@app.errorhandler(404)
def errorhandler(e):
    print('error_handler(404)')
    print(e)
    return '404 Error'

if __name__ == '__main__':
    app.run()
