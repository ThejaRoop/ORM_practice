from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
import datetime
from sqlalchemy import create_engine

# Base class for declarative models
Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(128), nullable=False)
    posts = relationship("Post", backref="user")
    comments = relationship("Comment", backref="user")
    likes = relationship("Like", backref="user")

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey("users.id"), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    comments = relationship("Comment", backref="post")
    likes = relationship("Like", backref="post")

class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True)
    post_id = Column(ForeignKey("posts.id"), nullable=False)
    user_id = Column(ForeignKey("users.id"), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

class Like(Base):
    __tablename__ = "likes"

    user_id = Column(ForeignKey("users.id"), primary_key=True)
    post_id = Column(ForeignKey("posts.id"), primary_key=True)


engine = create_engine('postgresql://postgres:roop@localhost/mydb') #, echo=True)

Base.metadata.create_all(engine)