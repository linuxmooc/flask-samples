from flask import Blueprint

blueprint = Blueprint('products', __name__, url_prefix='/products')

@blueprint.route("/car")
def car_products():
    return "汽车产品版块"

@blueprint.route("/baby")
def baby_products():
    return "婴儿产品版块"    