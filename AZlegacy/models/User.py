"""Define the user model
"""
from sqlalchemy import Column, Integer, String
from werkzeug.security import generate_password_hash
from ..db import Base
from uuid import uuid4


class User(Base):
    """User model to map the users table
    """
    __tablename__ = 'users'
    user_id = Column(String(128), primary_key=True, nullable=False)
    first_name = Column(String(45), nullable=False)
    last_name = Column(String(45), nullable=False)
    email = Column(String(100), nullable=False)
    passwd = Column(String(200), nullable=False)

    def __init__(self, first_name, last_name, email, passwd):
        """Initiate the model object with column values
        """
        self.user_id = uuid4()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.passwd = generate_password_hash(passwd)

    def __repr__(self):
        """Return a string representation of a user
        """
        return "User: {} {}".format(self.first_name, self.last_name)
