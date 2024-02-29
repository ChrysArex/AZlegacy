"""Define the Component model
"""
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from db import Base
from User import User
from Budjet import Budjet
from uuid import uuid4


class Component(Base):
    """component model to map the components table
    """
    __tablename__ = 'components'
    budjet_id_1 = Column(String(128), ForeignKey(Budjet.budjet_id), nullable=False)
    component_id = Column(String(128), primary_key=True, nullable=False)
    name = Column(String(50), nullable=False)
    price = Column(Float, nullable=False)

    def __init__(self, price, name, bid):
        """Initiate the model object with column values
        """
        self.component_id = uuid4()
        self.price = price
        self.name = name
        self.budjet_id_1 = bid

    def __repr__(self):
        """Return a string representation of a component
        """
        return "Component: {}".format(self.component_id)
