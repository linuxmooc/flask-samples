#!/usr/bin/python3
from flask import Flask, request, Response, render_template
app = Flask(__name__)

@app.route('/get_cookie')
def get_cookie():
    cookie = request.cookies.get('mooc')
    return render_template('get_cookie.html', cookie = cookie)

@app.route('/set_cookie')
def set_cookie():
    html = render_template('js_cookie.html')
    response = Response(html) 
    response.set_cookie('mooc', 'www.imooc.com')
    return response

@app.route('/del_cookie')
def del_cookie():
    html = render_template('js_cookie.html')
    response = Response(html) 
    response.delete_cookie('mooc')
    return response

if __name__ == '__main__':
    app.run(debug = True)    
