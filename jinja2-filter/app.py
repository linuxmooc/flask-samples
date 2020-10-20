from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', input = 123)

def increase(input):
    output = input + 1
    return output
app.add_template_filter(increase, 'increase') 

@app.template_filter('decrease')
def decrease(input):
    output = input - 1
    return output

app.run(debug = True)
