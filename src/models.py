import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __abstract__ = True
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id=Column(String(250), nullable=True)
    phone_number=Column(String(250),nullable=True)
    email_address=Column(String(250), nullable=True)
    password=Column(String(250), nullable=True)

class Personal_user(User):
    __tablename__ = 'personal user'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    gender=Column(String(2),nullable=True)
    personal_users_posts=relationship("Post")
    children1=relationship("Post",back_populates="parent1")
    children2=relationship("Follower",back_populates="user_from_id1")



class Business_user(User):
    __tablename__='business user'
    website=Column(String(250),nullable=True)
    bussiness_users_posts=relationship("Post")
    children1=relationship("Post",back_populates="parent2")
    children2=relationship("Follower",back_populates="user_from_id1")

class Post(Base):
    __tablename__='post'
    id=Column(Integer, primary_key=True)  
    description=Column(String(250),nullable=True)
    parent1=Column(Integer, ForeignKey('personal user.id'))
    parent2=Column(Integer,ForeignKey('business user.id'))
    children=relationship("Multimedia",back_populates="parent1")

class Follower(Base):
    __tablename__='follower'   
    id=Column(Integer, primary_key=True)   
    user_from_id1=Column(Integer, ForeignKey('personal user.id'))
    user_from_id2=(Integer,ForeignKey('business user.id'))
    user_to_id1=Column(Integer, ForeignKey('personal user.id'))
    user_to_id2=(Integer,ForeignKey('business user.id'))
    
class Multimedia(Base):
    __tablename__='multimedia'
    id=Column(Integer, primary_key=True)  
    typ=Column(Integer, nullable=True)
    url=Column(String(250), nullable=False)
    parent1=Column(Integer, ForeignKey('post.id'))

class Comment(Base):
    __tablename__='comment'
    id=Column(Integer, primary_key=True)  
    comment_text=Column(String(250), nullable=True)
    author_id1=Column(Integer, ForeignKey('personal user.id'))
    author_id2=Column(Integer, ForeignKey('business user.id'))
    post_id=Column(Integer, ForeignKey('post.id'))



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')