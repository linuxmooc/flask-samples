from flask import Flask, request
app = Flask(__name__)

@app.route('/login', methods = ['GET'])
def login():
    return '''
<form action="/check_login" method="POST">
  <p><input type="text" name="name"/></p>
  <p><input type="password" name="password"/></p>
  <p><input type="submit" value="submit"/></p>
</form>
'''

@app.route('/check_login', methods = ['POST'])
def check_login():
    name = request.form['name']
    password = request.form['password']
    if name == 'guest' and password == '123':
        return 'Login succeed'
    else:
        return 'Login failed'

if __name__ == '__main__':
    app.run()
