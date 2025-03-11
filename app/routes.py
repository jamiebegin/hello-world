from flask import Blueprint

main_bp = Blueprint("main_bp", __name__)

@main_bp.route("/")
def hello_world():
    return "Hello World!"

@main_bp.route("/health-check")
def health_check():
    return "It's all good, man!"

@main_bp.route("/login")
def login():
    return "The login form goes here."
