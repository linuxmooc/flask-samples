#!/usr/bin/python3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sys

app = Flask(__name__)
user = 'root'
password = '123456' 
database = 'school'
uri = 'mysql+pymysql://%s:%s@localhost:3306/%s' % (user, password, database)
app.config['SQLALCHEMY_DATABASE_URI'] = uri 

db = SQLAlchemy(app)

class Student(db.Model):
    __tablename__ = 'students'
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    age = db.Column(db.Integer)

    def dump(self):
        print(self.sno, self.name, self.age)

def create_table():
    db.drop_all()
    db.create_all()

def insert_students():
    tom = Student(sno = 1, name = 'tom', age = 12)
    db.session.add(tom)
    db.session.commit()

    jerry = Student(sno = 2, name = 'jerry', age = 11)
    mike = Student(sno = 3, name = 'mike', age = 11)
    db.session.add_all([jerry, mike])
    db.session.commit()

def query_students():
    print('查询所有的学生')
    students = Student.query.all()
    for student in students: 
        student.dump()
    print()

    print('查询所有年龄是 11 岁的学生')
    students = Student.query.filter_by(age = 11)
    for student in students: 
        student.dump()
    print()

    print('查询第一个年龄是 11 岁的学生')
    students = Student.query.filter_by(age = 11)
    student = students.first()
    student.dump()
    print()

    print('查询姓名是 jerry 并且年龄是 11 岁的学生')
    students = Student.query.filter_by(age = 11, name = 'jerry')
    for student in students:
        student.dump()
    print()

def update_students():
    students = Student.query.filter_by(name = 'tom')
    students.update({'name':'TOM'})
    db.session.commit()

def delete_students():
    students = Student.query.filter_by(name = 'mike')
    students.delete()
    db.session.commit()

command = sys.argv[1]
if command == 'create':
    create_table()
elif command == 'insert':
    insert_students()
elif command == 'query':
    query_students()
elif command == 'update':
    update_students()
elif command == 'delete':
    delete_students()
