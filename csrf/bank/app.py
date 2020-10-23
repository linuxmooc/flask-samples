#!/usr/bin/python3
from flask import Flask, request, session, render_template, redirect
import os, base64
import sys

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

class User:
    def __init__(self, name, password, amount):
        self.name = name
        self.password = password
        self.amount = amount

users = [
    User('victim', '123', 100),
    User('hacker', '123', 100)
]

def findUser(name):
    for user in users:
        if user.name == name:
            return user
    return None

def checkUser(name, password):
    for user in users:
        if user.name == name and user.password == password:
            return user
    return None

@app.route('/')
def index():
    hasLogin = session.get('hasLogin')
    name = session.get('name')
    user = findUser(name)
    csrfToken = getCsrfToken()
    session['csrfToken'] = csrfToken
    return render_template('index.html', hasLogin = hasLogin, user = user, csrfToken = csrfToken)

@app.route('/login', methods = ['POST'])
def login():
    name = request.form['name']
    password = request.form['password']
    user = checkUser(name, password)
    if user != None:
        session['hasLogin'] = True
        session['name'] = name
        return redirect('/')
    else:
        return '登录失败'

@app.route('/logout', methods = ['POST'])
def logout():
    session['hasLogin'] = False
    session['name'] = None
    return redirect('/')        

def getCsrfToken():
    return bytes.decode(base64.b64encode(os.urandom(16)))

def checkCsrfAttack():
    csrfTokenFromRequest = request.form.get('csrfToken')
    csrfTokenFromSession = session.get('csrfToken')
    return csrfTokenFromRequest != csrfTokenFromSession    

@app.route('/transfer', methods = ['POST'])
def transfer():
    if not session.get('hasLogin'):
        return '请先登录'

    if checkFlag and checkCsrfAttack():
        print('警告：检测到 CSRF 攻击!')
        return '转账失败'

    sourceName = session['name']
    sourceUser = findUser(sourceName)

    targetName = request.form['name']
    amount = int(request.form['amount'])
    targetUser = findUser(targetName)

    if targetUser != None:
        sourceUser.amount -= amount
        targetUser.amount += amount
        return redirect('/')
    else:
        return '转账失败'

checkFlag = False
if len(sys.argv) == 2 and sys.argv[1] == 'check':
    checkFlag = True

app.run(debug = True, port = 8888)
