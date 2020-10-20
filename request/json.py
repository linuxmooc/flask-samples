from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def root():
    file = open('api.html', encoding = 'utf-8')
    return file.read()

@app.route('/api/addUser', methods = ['POST'])
def addUser():
    json = request.json
    print('JSON', json)
    print('name = %s' % json['name'])
    print('age = %s' % json['age'])
    return 'addUser OK'

if __name__ == '__main__':
    app.run(debug = True)

