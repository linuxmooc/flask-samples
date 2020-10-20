from flask import Flask
from datetime import timedelta

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1) 
app.config['SECRET_KEY'] = 'hard to guess string'

