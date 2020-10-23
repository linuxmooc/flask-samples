#!/usr/bin/python3
from flask import Flask, render_template, request, jsonify
from datetime import timedelta

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1) 

class User:
    nextId = 0 

    def __init__(self, name, phone):
        self.id = User.nextId
        User.nextId += 1
        self.name = name
        self.phone = phone

tom = User('tom', '10086')
jerry = User('jerry', '12306')
users = [tom, jerry]

@app.route('/')
def index():
    return render_template('index.html', users = users)

@app.route('/users', methods=['POST'])
def addUser():
    name = request.json['name']
    phone = request.json['phone']

    user = User(name, phone)
    users.append(user)

    return jsonify({'error': None});

@app.route('/users/<int:userId>', methods=['PUT'])
def updateUser(userId):
    name = request.json['name']
    phone = request.json['phone']

    for user in users:
        if user.id == userId:
            user.name = name
            user.phone = phone
            break

    return jsonify({'error': None}); 

@app.route('/users/<int:userId>', methods=['DELETE'])
def deleteUser(userId):
    index = 0
    for user in users:
        if user.id == userId:
            del users[index]
            break
        index += 1

    return jsonify({'error': None});

if __name__ == '__main__':
    app.run(debug = True)    
