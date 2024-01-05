from flask import render_template, request, Blueprint

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    return "hi there"


@main.route("/about")
def about():
    return "about page"