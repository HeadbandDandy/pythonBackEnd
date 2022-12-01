# below contains imports needed for Post Model

from datetime import datetime
from .Vote import Vote
from app.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, select, func
from sqlalchemy.orm import relationship, column_property 

# below contains the Post class

class Post(Base):
    vote_count = column_property(
        select([func.count(Vote.id)]).where(Vote.post_id == id)
    )
    __tablename__ = 'posts'
    user = relationship('User')
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    post_url = Column(String(100), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    post_id = Column(Integer, ForeignKey('posts.id'))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    comments = relationship('Comment', cascade='all, delete')
    votes = relationship('Vote', cascade='all, delete')

    


