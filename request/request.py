from flask import Flask
from flask import request
app = Flask(__name__)

def echo(key, value):
    print('%-10s = %s' % (key, value))

@app.route('/query')
def query():
    echo('url', request.url)
    echo('base_url', request.base_url)    
    echo('host', request.host)
    echo('host_url', request.host_url)
    echo('path', request.path)
    echo('full_path', request.full_path)
    return 'hello'

if __name__ == '__main__':
    app.run(port = 80)
