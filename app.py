import os
from flask import Flask
from extensions import db

def create_app():
    app = Flask(__name__)

    # Use environment variables for configurations
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

    db.init_app(app)

    # Register Blueprints, etc.
    return app
