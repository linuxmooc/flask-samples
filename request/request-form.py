from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def root():
    file = open('form.html', encoding = 'utf-8')
    return file.read()

@app.route('/addUser', methods = ['POST'])
def check_login():
    name = request.form['name']
    age = request.form['age']
    print('name = %s' % name)
    print('age = %s' % age)
    return 'addUser OK'

if __name__ == '__main__':
    app.run(debug = True)

