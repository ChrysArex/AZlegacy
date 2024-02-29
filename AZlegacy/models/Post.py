"""Define the user model
"""
from sqlalchemy import Column, Integer, String, Text, Date
from datetime import datetime
from db import Base
from User import User
from uuid import uuid4


class Post(Base):
    """Post model to map the posts table
    """
    __tablename__ = 'posts'
    post_id = Column(String(128), primary_key=True, nullable=False)
    created_at = Column(Date, nullable=False)
    title= Column(String(100), nullable=False)
    contents = Column(Text, nullable=False)
    likes = Column(Integer, nullable=False)
    dislikes = Column(Integer, nullable=False)
    views = Column(Integer, nullable=False)
    user_id = Column(String(128), ForeignKey(User.user_id), nullable=False)

    def __init__(self, title, contents, user_id):
        """Initiate the model object with column values
        """
        self.post_id = uuid4()
        self.created_at = datetime.now()
        self.title = title
        self.contents = contents
        self.likes = 0
        self.dislikes = 0
        self.views = 0
        self.user_id = user_id

    def __repr__(self):
        """Return a string representation of a post
        """
        return "Post: {}".format(self.post_id)
