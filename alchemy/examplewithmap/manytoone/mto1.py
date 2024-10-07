from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date, Boolean
from sqlalchemy.orm import relationship, sessionmaker
import datetime
from sqlalchemy import Table
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship

class Base(DeclarativeBase):
    pass

from sqlalchemy import Column, Integer, String, DateTime

class User(Base):
    __tablename__ = 'users'
    name = Column(String)
    address = Column(String)
    id = Column(Integer, primary_key=True)
    post = relationship('Posts', back_populates='user')

class Posts(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    users_id = Column(Integer,ForeignKey('users.id'))
    user = relationship('User', back_populates='post')

# Create a SQLite database in memory for demonstration
# engine = create_engine('sqlite:///:memory:')
engine = create_engine('postgresql://postgres:roop@localhost/mydb2')

try:
    Base.metadata.create_all(engine)
except Exception as e:
    print(f"Error while creating tables: {e}")
