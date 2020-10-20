from flask import Flask, views
app = Flask(__name__)

class Index(views.View) :
    def dispatch_request(self):
        return 'hello world'

app.add_url_rule(rule='/', view_func = Index.as_view('Index'))
app.run(debug = True)
