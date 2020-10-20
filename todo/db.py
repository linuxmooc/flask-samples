from app import app
from flask_sqlalchemy import SQLAlchemy

user = 'root'
password = '123456'
database = 'todoDB'
uri = 'mysql+pymysql://%s:%s@localhost:3306/%s' % (user, password, database)
app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
orm = SQLAlchemy(app)

class User(orm.Model):
    __tablename__ = 'users'
    userId = orm.Column(orm.Integer, primary_key=True)
    name = orm.Column(orm.String(255))
    password = orm.Column(orm.String(255))

class Todo(orm.Model):
    __tablename__ = 'todos'
    todoId = orm.Column(orm.Integer, primary_key=True)
    userId = orm.Column(orm.Integer)
    status = orm.Column(orm.String(255))
    title = orm.Column(orm.String(255))

def login(name, password):
    users = User.query.filter_by(name = name, password = password)
    user = users.first()
    return user

def register(name, password):
    user = User(name = name, password = password)
    orm.session.add(user)
    orm.session.commit()
    return True

def getTodos(userId):
    todos = Todo.query.filter_by(userId = userId)
    return todos

def addTodo(userId, status, title):
    todo = Todo(userId = userId, status = status, title = title)
    orm.session.add(todo)
    orm.session.commit()
    return True

def updateTodo(todoId, status):
    todos = Todo.query.filter_by(todoId = todoId)
    todos.update({'status': status})
    orm.session.commit()
    return True

def deleteTodo(todoId):
    todos = Todo.query.filter_by(todoId = todoId)
    todos.delete()
    orm.session.commit()
    return True

