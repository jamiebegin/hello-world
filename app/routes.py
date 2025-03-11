from flask import Blueprint

main_bp = Blueprint("main_bp", __name__)

@main_bp.route("/")
def hello_world():
    return "Hello World!"

@main_bp.route("/health-check")
def health_check():
    return "<h1>It's all good, man!</h1>"

@main_bp.route("/login")
def login():
    return "The login form goes here."
