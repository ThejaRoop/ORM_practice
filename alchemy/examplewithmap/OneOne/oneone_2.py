from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# User class (One-to-One with Profile)
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    
    # One-to-One relationship with Profile
    profile = relationship("Profile", uselist=False, back_populates="user")

# Profile class (One-to-One with User)
class Profile(Base):
    __tablename__ = 'profiles'
    
    id = Column(Integer, primary_key=True)
    bio = Column(String(255))
    user_id = Column(Integer, ForeignKey('users.id'), unique=True)  # Ensure One-to-One
    
    # Back reference to User
    user = relationship("User", back_populates="profile")

# # Setting up the engine and session
engine = create_engine('postgresql://postgres:roop@localhost/mydb2')#, echo=True)  # You can use Postgres here instead of SQLite
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
