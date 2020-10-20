from flask import Flask, render_template, request, redirect, session, jsonify
from flask import Blueprint
import db

blueprint = Blueprint('todos', __name__, url_prefix='/todos')

@blueprint.route('/add', methods = ['POST'])
def addTodo():
    userId = session.get('userId')
    status = 'todo'
    title = request.json['title']
    db.addTodo(userId, status, title)
    return jsonify({'error': None});

@blueprint.route('/update', methods = ['POST'])
def updateTodo():
    todoId = request.json['todoId']
    status = 'done'
    db.updateTodo(todoId, status)
    return jsonify({'error': None});

@blueprint.route('/delete', methods = ['POST'])
def deleteTodo():
    todoId = request.json['todoId']
    db.deleteTodo(todoId)
    return jsonify({'error': None});
