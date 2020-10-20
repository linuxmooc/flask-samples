#!/usr/bin/python3
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    1/0
    return '<b>hello world</b>'

if __name__ == '__main__':
    app.run()
