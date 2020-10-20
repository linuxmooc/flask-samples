from flask import Flask, request
from functools import wraps
app = Flask(__name__)

def check_login(original_function):
    @wraps(original_function)
    def decorated_function(*args,**kwargs):
        user = request.args.get("user")
        if user and user == 'zhangsan':
             return original_function(*args, **kwargs)
        else:
            return '请先登录'
    return decorated_function

@app.route('/page1')
@check_login
def page1():
    return 'page1'

@app.route('/page2')
@check_login
def page2():
    return 'page2'

app.run(debug = True)

