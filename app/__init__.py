from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import os

# Initialize extensions
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # App configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'default_secret_key')  # Use env var or fallback

    # Initialize extensions
    db.init_app(app)

    # Register blueprints
    from app.api.routes import main
    app.register_blueprint(main)

    return app