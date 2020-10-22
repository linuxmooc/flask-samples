from flask import Blueprint

blueprint = Blueprint('news', __name__, url_prefix='/news')

@blueprint.route("/society/")
def society_news():
    return "社会新闻版块"

@blueprint.route("/tech/")
def tech_news():
    return "IT 新闻板块"