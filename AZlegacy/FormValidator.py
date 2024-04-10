""" Define the classes to validate forms """

from wtforms import Form, StringField, validators, ValidationError
from werkzeug.security import check_password_hash
from .models import User
from .db import session

def uname_already_existe(form, field):
    user = session.query(User.User).filter_by(username=field.data).first()
    if user:
        raise ValidationError("username already taken!")

def uname_ok(form, field):
    user = session.query(User.User).filter_by(username=field.data).first()
    if not user:
        raise ValidationError("username not found!")


def password_ok(form, field):
    password = session.query(User.User).\
            filter_by(username=form.username.data).\
            first().passwd
    if not check_password_hash(password, field.data):
        raise ValidationError("invalide password!")

class RegistrationForm(Form):
    """class to validate the register form"""
    username = StringField('Username',
                          [
                            validators.Length(min=6, max=35),
                            validators.InputRequired(),
                            uname_already_existe
                          ])
    first_name = StringField('first_name', [validators.Length(min=4, max=25)])
    last_name = StringField('last_name', [validators.Length(min=4, max=25)])
    email= StringField('email',
                      [
                            validators.Length(min=6, max=35),
                            validators.InputRequired()
                      ])
    password = StringField('password',
                        [
                            validators.Length(min=6, max=35),
                            validators.InputRequired()
                        ])

class LoginForm(Form):
    """ Validate the login credentials """
    username = StringField("username", [uname_ok])
    password = StringField("password", [password_ok])
