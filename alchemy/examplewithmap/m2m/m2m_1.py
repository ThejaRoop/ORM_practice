from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date, Boolean
from sqlalchemy.orm import relationship, sessionmaker
import datetime
from sqlalchemy import Table
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship
from sqlalchemy import UniqueConstraint

class Base(DeclarativeBase):
    pass

from sqlalchemy import Column, Integer, String, DateTime

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    created_at = Column(DateTime, default=datetime.datetime)

    categories = relationship('Category', secondary='post_categories', back_populates='posts')

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    posts = relationship('Post', secondary='post_categories', back_populates='categories')

# Association table for Post and Category
post_categories = Table('post_categories', Base.metadata,
    Column('post_id', ForeignKey('posts.id'), primary_key=True),
    Column('category_id', ForeignKey('categories.id'), primary_key=True),
)
# Create a SQLite database in memory for demonstration
# engine = create_engine('sqlite:///:memory:')
engine = create_engine('postgresql://postgres:roop@localhost/mydb2')

try:
    Base.metadata.create_all(engine)
except Exception as e:
    print(f"Error while creating tables: {e}")
