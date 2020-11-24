#!/usr/bin/python3
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Email, ValidationError

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

class LoginForm(FlaskForm):
    email = StringField(
        label = '邮箱',
        validators = [
            DataRequired(message = '邮箱不能为空'),
            Email(message = '请输入正确的邮箱')
        ]
    )

    password = PasswordField(
        label = '密码',
        validators =[
            DataRequired(message = '密码不能为空'),
            Length(min = 6, message = '密码至少包括 6 个字符')
        ]
    )

    submit = SubmitField('登录')

@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    print('form.validate_on_submit() =', form.validate_on_submit())
    print('form.email.label =', form.email.label)
    print('form.email() = ', form.email)
    print('form.email.errors =', form.email.errors)
    return render_template('login.html', form=form)

app.run(debug=True)    
