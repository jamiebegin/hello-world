from flask import Flask
from app.routes import main_bp

def create_app():
    """App factory function."""
    app = Flask(__name__)
    # Register blueprint
    app.register_blueprint(main_bp)
    return app

