"""Define the SideHustle model
"""
from sqlalchemy import Column, Integer, String, Text, Date
from datetime import datetime
from db import Base
from User import User
from uuid import uuid4


class SideHustle(Base):
    """SideHustle model to map the side_hustles table
    """
    __tablename__ = 'side_hustles'
    sh_id = Column(String(128), primary_key=True, nullable=False)
    title= Column(String(100), nullable=False)
    steps = Column(Text, nullable=False)
    deadline = Column(Date, nullable=False)
    initial_investement = Column(Float, nullable=False)
    estimated_return = Column(Float, nullable=False)
    user_id = Column(String(128), ForeignKey(User.user_id), nullable=False)

    def __init__(self, title, steps, deadline, ii, er, user_id):
        """Initiate the model object with column values
        """
        self.sh_id = uuid4()
        self.title = title
        self.steps = steps
        self.deadline = deadline
        self.initial_investement = ii
        self.estimated_return = er
        self.user_id = user_id

    def __repr__(self):
        """Return a string representation of a side hustle
        """
        return "Side_h: {}".format(self.sh_id)
