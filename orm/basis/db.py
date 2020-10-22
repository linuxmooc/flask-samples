from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

user = 'root'
password = '123456'
database = 'school'
uri = 'mysql+pymysql://%s:%s@localhost:3306/%s' % (user, password, database)
app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Student(db.Model):
    __tablename__ = 'students'
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    age = db.Column(db.Integer)

students = Student.query.all()
for student in students:
    print(student.sno, student.name, student.age)
