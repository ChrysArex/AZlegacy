"""This file contain the app factory wich will return our main flask app
"""
from flask import Flask, render_template
from flask_login import LoginManager, login_required
from .API_auth import app_auth
import requests
import json
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

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    from . import db
    from .models import User
    db.init_db()

    @login_manager.user_loader
    def load_user(user_id):
        return db.session.query(User.User).filter_by(id=user_id).first()

    app.teardown_appcontext(db.shutdown_session)
    """set the landing page"""
    @app.route("/", methods=["GET"])
    def landing_page():
        return render_template("index.html")

    """add the authentication blueprint"""
    from .auth import auth_bp
    app.register_blueprint(auth_bp)

    @app.route("/feed", methods=["GET"])
    @login_required
    def feed():
        """Feed the postes page with data fetch from third-party API(reddit)
        """
        fetched_data = {}
        headers_1 = app_auth()
        url = "https://oauth.reddit.com/r/FinancialPlanning/hot.json?limit=100"
        try:
            r = requests.get(url, headers=headers_1)
            print(r)
            print(r.text)
            print(r.json())
            fetched_data = json.loads(r.text).get('data').get('children')
        except:
            print("authentication error")
        finally:
            hot = fetched_data
        return render_template("postes.html", hot=hot)

    return app
