from oneone_2 import User, Profile
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass
# Create a user and a profile
user1 = User(username='Man_doe')
profile1 = Profile(bio="Software Engineer at TechCorp")

# Link profile to user (One-to-One)
# user1.profile = profile1

engine = create_engine('postgresql://postgres:roop@localhost/mydb2',echo=True)  # You can use Postgres here instead of SQLite
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Add and commit to the database
session.add(user1)
session.commit()

# Trying to add a second profile to the same user should raise an error
try:
    profile2 = Profile(bio="Trying to assign second profile")
    user1.profile = profile2  # This should raise an error due to One-to-One constraint
    session.commit()
except Exception as e:
    print(f"Error: {e}")
    session.rollback()

