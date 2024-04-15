"""Define function views for login and register
"""
from flask import (
        Blueprint, url_for, redirect, request, render_template
        )
from flask_login import login_user, logout_user, login_required
from werkzeug.security import check_password_hash
from sqlalchemy import select
from .models import User
from .db import session
from .FormValidator import RegistrationForm, LoginForm

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

@auth_bp.route("/register", methods=("GET", "POST"))
def register():
    """Validate and register a new user's data in the database"""
    form = RegistrationForm(request.form)
    r_or_l = "Register"
    if request.method == "POST":
        if not form.validate():
            return render_template("auth/register_login.html", form=form, r_or_l=r_or_l)

        user = User.User(username=request.form.get("username"),
                        email=request.form.get("email"),
                        passwd=request.form.get("password"),
                        first_name=request.form.get("first_name"),
                        last_name=request.form.get("last_name")
                        )
        session.add(user)
        session.commit()
        return redirect(url_for("auth.login"))

    return render_template("auth/register_login.html", form=form, r_or_l=r_or_l)

@auth_bp.route("/login", methods=("GET", "POST"))
def login():
    """authenticate and log a user in the system
    """
    r_or_l = "Login"
    form = LoginForm(request.form)
    if request.method == "POST":
        user = session.query(User.User).filter_by(username=request.form.get("username")).first()
        if not form.validate():
            return render_template("auth/register_login.html", form=form, r_or_l=r_or_l)
        login_user(user)
        return redirect(url_for("feed"))

    return render_template("auth/register_login.html", form=form, r_or_l=r_or_l)

@auth_bp.route("/logout")
@login_required
def logout():
    """ logout the user"""
    logout_user()
    return "logout"
