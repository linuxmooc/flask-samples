from flask import Flask
app = Flask(__name__)

class Index:
    def dispatch_request(self):
        return 'hello world'

    @staticmethod
    def as_view(name):
        index = Index()
        return index.dispatch_request

app.add_url_rule(rule='/', view_func = Index.as_view('Index'))
app.run(debug = True)

