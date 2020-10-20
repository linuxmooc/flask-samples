from flask import Flask, render_template, request, redirect, session
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length
from flask import Blueprint
import db

blueprint = Blueprint('users', __name__, url_prefix='/users')

class LoginForm(FlaskForm):
    name = StringField(
        label = '姓名',
        validators = [
            DataRequired(message = '姓名不能为空')
        ]
    )

    password = PasswordField(
        label = '密码',
        validators =[
            DataRequired(message = '密码不能为空'),
            Length(min = 3, message = '密码至少包括 3 个字符')
        ]
    )

    submit = SubmitField('登录')

@blueprint.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        form = LoginForm()
        return render_template('login.html', form = form)
    else:
        form = LoginForm()
        if form.validate_on_submit():
            name = form.name.data
            password = form.password.data
            user = db.login(name, password)
            if user:
                session['hasLogin'] = True
                session['userId'] = user.userId
                return redirect('/')
        return render_template('login.html', form = form)

class RegisterForm(FlaskForm):
    name = StringField(
        label = '姓名',
        validators = [
            DataRequired(message = '姓名不能为空')
        ]
    )

    password = PasswordField(
        label = '密码',
        validators =[
            DataRequired(message = '密码不能为空'),
            Length(min = 3, message = '密码至少包括 3 个字符')
        ]
    )

    submit = SubmitField('注册')

@blueprint.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'GET':
        form = RegisterForm()
        return render_template('register.html', form = form)
    else:
        form = RegisterForm()
        if form.validate_on_submit():
            name = form.name.data
            password = form.password.data
            if db.register(name, password):
                return redirect('/')
        return render_template('register.html', form = form)

@blueprint.route('/logout')
def logout():
    session['hasLogin'] = False
    return redirect('/')
