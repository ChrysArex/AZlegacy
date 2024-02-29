"""This file contain the app factory wich will return our main flask app
"""
from flask import Flask
import os

def create_app(test_config=None):
    """configure and return our main app"""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY='dev')

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    from .models import User
    db.init_db()
    app.teardown_appcontext(db.shutdown_session)

    @app.route('/hello')
    def hello():
        first = User.User("doudou", "Adoumasse", "adoumasseo@gmail.com", "passwd")
        db.session.add(first)
        db.session.commit()
        return first.__repr__()

    return app
