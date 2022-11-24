from flask import Flask
from flask_bootstrap import Bootstrap
from app.routes.book import book_router
from app.config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    Bootstrap(app)
    
    app.register_blueprint(book_router)
    
    return app
