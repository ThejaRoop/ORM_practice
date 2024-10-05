from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()


# Association Table for Many-to-Many relationship between User and Project
user_project_association = Table(
    'user_project_association', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id'), primary_key=True),
    Column('project_id', Integer, ForeignKey('projects.id'), primary_key=True)
)

# User class (One-to-One with Profile, One-to-Many with Task, Many-to-Many with Project)
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(100), nullable=False, unique=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # One-to-One relationship with Profile
    profile = relationship('Profile', uselist=False, back_populates='user')
    
    # One-to-Many relationship with Task
    tasks = relationship('Task', back_populates='user')
    
    # Many-to-Many relationship with Project
    projects = relationship('Project', secondary=user_project_association, back_populates='users')

# Profile class (One-to-One with User)
class Profile(Base):
    __tablename__ = 'profiles'
    
    id = Column(Integer, primary_key=True)
    full_name = Column(String(100), nullable=False)
    bio = Column(String(255))
    user_id = Column(Integer, ForeignKey('users.id'), unique=True)
    
    # Back reference to User
    user = relationship('User', back_populates='profile')

# Project class (Many-to-Many with User, One-to-Many with Task)
class Project(Base):
    __tablename__ = 'projects'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    description = Column(String(255))
    deadline = Column(DateTime, nullable=False)
    
    # Many-to-Many relationship with User
    users = relationship('User', secondary=user_project_association, back_populates='projects')
    
    # One-to-Many relationship with Task
    tasks = relationship('Task', back_populates='project')

# Task class (One-to-Many with User and Project)
class Task(Base):
    __tablename__ = 'tasks'
    
    id = Column(Integer, primary_key=True)
    description = Column(String(255), nullable=False)
    due_date = Column(DateTime, nullable=False)
    
    # Foreign keys for the relationships
    user_id = Column(Integer, ForeignKey('users.id'))
    project_id = Column(Integer, ForeignKey('projects.id'))
    
    # Back reference to User and Project
    user = relationship('User', back_populates='tasks')
    project = relationship('Project', back_populates='tasks')


# Create engine and session
engine = create_engine('postgresql://postgres:roop@localhost/mydb1')
Session = sessionmaker(bind=engine)
session = Session()

# Create all tables
Base.metadata.create_all(engine)


# Close session
session.close()
