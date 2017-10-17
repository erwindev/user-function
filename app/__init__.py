import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()


def create_app():
    config_name = os.environ.get('ENV_CONFIG') or 'default'
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app, config_name)
    db.init_app(app)
    with app.test_request_context():
        db.create_all()
    return app
