"""Define the Comment model
"""
from sqlalchemy import Column, Integer, String, Text, Date
from datetime import datetime
from Post import Post
from User import User
from uuid import uuid4


class Comment(Post):
    __tablename__ = "comments"
    comment_id = uuid4()
    post_id = Column(String(128), ForeignKey(Post.post_id), nullable=False)

    def __init__(self, title, contents, post_id, user_id="no_user"):
        super.__init__(title, contents, user_id)
        self.comment_id = uuid4()
        self.post_id = post_id

    def __repr__(self):
        """return a string representation of a comment"""
        return "Comment: {}".format(self.comment_id)
