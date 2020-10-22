#!/usr/bin/python3
from flask import Flask, render_template, request
import redis

app = Flask(__name__)
db = redis.Redis(host='localhost', decode_responses=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query', methods = ['post'])
def query():
    keys = db.keys()
    dict = {}
    for key in keys:
        value = db.get(key)
        dict[key] = value
    return render_template('query.html', dict = dict)

@app.route('/insert', methods = ['post'])
@app.route('/update', methods = ['post'])
def insert():
    key = request.form['key']
    value = request.form['value']
    db.set(key, value)
    return query()

@app.route('/insertMulti', methods = ['post'])
def insertMulti():
    keyA = request.form['keyA']
    valueA = request.form['valueA']
    keyB = request.form['keyB']
    valueB = request.form['valueB']
    db.mset({keyA:valueA, keyB:valueB})
    return query()

@app.route('/delete', methods = ['post'])
def delete():
    key = request.form['key']
    db.delete(key)
    return query()

@app.route('/deleteAll', methods = ['post'])
def deleteAll():
    db.flushall()
    return query()

app.run()
