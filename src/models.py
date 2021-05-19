import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    address = Column(String(250))
    birthdate = Column(DateTime, nullable=False)

class Account(Base):
    __tablename__ = 'account'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(String(250), ForeignKey('user.id'), nullable=False)
    name = Column(String(250))
    profile_image = Column(String(250), nullable=False)
    bio = Column(String(250))
    user = relationship(User)

    def to_dict(self):
        return {}

class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    account_id = Column(String(250), ForeignKey('account.id'), nullable=False)
    image = Column(String(250), nullable=False)
    description = Column(String(250))
    user = relationship(Account)

    def to_dict(self):
        return {}

class Comment(Base):
    __tablename__ = 'comment'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    post_id = Column(String(250), ForeignKey('post.id'), nullable=False)
    user_id = Column(String(250), ForeignKey('user.id'), nullable=False)
    comment = Column(String(250))
    user = relationship(Post)
    user = relationship(User)

    def to_dict(self):
        return {}

class Like(Base):
    __tablename__ = 'like'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    post_id = Column(String(250), ForeignKey('post.id'), nullable=False)
    user_id = Column(String(250), ForeignKey('user.id'), nullable=False)
    user = relationship(Post)
    user = relationship(User)

    def to_dict(self):
        return {}

class FollowedAccounts(Base):
    __tablename__ = 'followedaccounts'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    follower_account_id = Column(String(250), ForeignKey('account.id'), nullable=False)
    followed_account_id = Column(String(250), ForeignKey('account.id'), nullable=False)
    user = relationship(Account)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e