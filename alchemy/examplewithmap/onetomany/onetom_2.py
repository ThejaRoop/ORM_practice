from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date, Boolean
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.orm import declarative_base
import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship
from sqlalchemy import UniqueConstraint

class Base(DeclarativeBase):
    pass
# Define the Parent class

class Parent(Base):
    __tablename__ = 'parent_table'
    id = Column(Integer, primary_key=True)
    parentname = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)  # Integer (Age)
    date_of_birth = Column(Date, nullable=False)  # Date (Date of Birth)
    is_employed = Column(Boolean, default=True)  # Boolean (Employment status)
    address = Column(String(255), nullable=True) 

# This defines that a parent can have many children
    children = relationship('Child', back_populates='parent')

# Define the Child class
class Child(Base):
    __tablename__ = 'child_table'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)  # String (First Name)
    grade = Column(Integer, nullable=False)  # Integer (Grade in school)
    birth_date = Column(Date, nullable=False)  # Date (Birth Date)
    is_enrolled = Column(Boolean, default=True) 
     # This links each child to a single parent
    parent_id = Column(Integer, ForeignKey('parent_table.id'))  # Foreign key linking to Parent
    parent = relationship('Parent', back_populates='children')
    
    __table_args__ = (
        UniqueConstraint('first_name', 'birth_date', name='unique_child_constraint'),
    )

# Create a SQLite database in memory for demonstration
# engine = create_engine('sqlite:///:memory:')
engine = create_engine('postgresql://postgres:roop@localhost/mydb2')
Base.metadata.create_all(engine)

# Create a new session
# Session = sessionmaker(bind=engine)
# session = Session()

# # Example of adding an Parent and Childs
# new_parent = Parent(name='J.K. Rowling')
# new_parent.books = [
#     Child(title='Harry Potter and the Philosopher\'s Stone'),
#     Child(title='Harry Potter and the Chamber of Secrets')
# ]

# # Add the parent (and associated books) to the session and commit
# session.add(new_parent)
# session.commit()

# # Query the database
# parents = session.query(Parent).all()
# for parent in parents:
#     print(f'Parent: {parent.name}')
#     for book in parent.books:
#         print(f'  Child: {book.title}')

# # Close the session
# session.close()
