from flask import Blueprint, render_template

blueprint = Blueprint('news', __name__, url_prefix='/news', template_folder='templates', static_folder='static')

@blueprint.route("/society/")
def society_news():
    return render_template('society.html')

@blueprint.route("/tech/")
def tech_news():
    return "IT 新闻板块"
