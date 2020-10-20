#!/usr/bin/python3
from app import app
from flask import render_template, session

import db
import users 
import todos
app.register_blueprint(users.blueprint)
app.register_blueprint(todos.blueprint)

@app.route('/')
def index():
    hasLogin = session.get('hasLogin')
    if hasLogin:
        userId = session.get('userId')
        items = db.getTodos(userId)
        todos = [item for item in items if item.status == 'todo']
        dones = [item for item in items if item.status == 'done']
    else:
        items = []
        todos = []
        dones = []
    return render_template('index.html', hasLogin = hasLogin, todos = todos, dones = dones)

app.run()


