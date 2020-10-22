from flask import Flask
import news
import products

app = Flask(__name__)

app.register_blueprint(news.blueprint)
app.register_blueprint(products.blueprint)

app.run(debug = True)