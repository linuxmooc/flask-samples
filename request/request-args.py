from flask import Flask, request
app = Flask(__name__)

@app.route('/query')
def query():
    print('name =', request.args['name'])
    print('age =', request.args['age'])
    return 'hello'

if __name__ == '__main__':
    app.run(debug = True)

