from sqlalchemy import Column, Integer, String, Date, ForeignKey, Table, create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import UniqueConstraint
import os
from dotenv import load_dotenv

load_dotenv()
class Base(DeclarativeBase):
    pass

post_tags = Table('post_tags', Base.metadata,
                  Column('post_id', ForeignKey('posts.id'),primary_key= True),
                  Column('tags_id', ForeignKey('tags.id'), primary_key= True)
                  )


class Users(Base):
    __tablename__= 'users'
    id=Column(Integer, primary_key=True)
    name=Column(String)
    email= Column(String)
    #one to one with profile
    profile = relationship('Profiles', back_populates= 'user', uselist= False)
#one to many with users--posts
    posts = relationship("Posts", back_populates= 'user')

class Profiles(Base):
    __tablename__= 'profiles'
    id=Column(Integer, primary_key=True)
    bio=Column(String)
    user_id= Column(Integer, ForeignKey('users.id'), unique= True)
    #one to one with users
    user = relationship('Users', back_populates= 'profile', single_parent= True)
    __table_args__ = (UniqueConstraint("user_id"),)

class Posts(Base):
    __tablename__= 'posts'
    id=Column(Integer, primary_key=True)
    title=Column(String)
    content= Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
#many to many with tags
    tag = relationship("Tags",secondary= post_tags, back_populates= 'posts')
#one to many with users--posts
    user = relationship("Users", back_populates= 'posts')


class Tags(Base):
    __tablename__ = 'tags'
    id=Column(Integer, primary_key= True)
    name= Column(String)
    description = Column(String)
    #many to many with posts
    post= relationship("Posts", secondary = post_tags, back_populates='tag')

# Use environment variables for database connection
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")

# Create the database URL using the environment variables
DATABASE_URL = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'
engine = create_engine(DATABASE_URL)

# engine = create_engine('postgresql://postgres:roop@localhost/mydb2')

try:
    Base.metadata.create_all(engine)
except Exception as e:
    print(f"Error while creating tables:{e}")

