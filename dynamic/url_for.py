#!/usr/bin/python3
from flask import Flask,redirect,url_for
app = Flask(__name__)
 
@app.route('/')
def index():
    print(url_for('index'))
    print(url_for('login')) 
    print(url_for('login', user = 'tom'))
    print(url_for('profile', user = 'jerry'))
    print(url_for('static', filename = 'script.js'))
    return 'index'
 
@app.route('/login/')
def login():
    return 'login'

@app.route('/profile/<user>')
def profile():
    return 'profile'

app.run()
