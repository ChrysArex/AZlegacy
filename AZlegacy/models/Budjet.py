"""Define the Budjet model
"""
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from db import Base
from User import User
from uuid import uuid4


class Budjet(Base):
    """Budjet model to map the budjets table
    """
    __tablename__ = 'budjets'
    budjet_id = Column(String(128), primary_key=True, nullable=False)
    timeline = Column(Integer(), nullable=False)
    user_id = Column(String(128), ForeignKey(User.user_id), nullable=False)
    total_amount = Column(Float, nullable=False)

    def __init__(self, timeline, user_id, total=0):
        """Initiate the model object with column values
        """
        self.budjet_id = uuid4()
        self.timeline = timeline
        self.user_id = user_id
        self.total_amount = total

    def __repr__(self):
        """Return a string representation of a budjet
        """
        return "Budjet: {}".format(self.budjet_id)
