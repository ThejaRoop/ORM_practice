from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# Create the base class for ORM
Base = declarative_base()

# Define the Author class
class Author(Base):
    __tablename__ = 'authors'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # Relationship to the Book class
    books = relationship('Book', back_populates='author')

# Define the Book class
class Book(Base):
    __tablename__ = 'books'
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'))  # Foreign key linking to Author

    # Relationship to the Author class
    author = relationship('Author', back_populates='books')

# Create a SQLite database in memory for demonstration
# engine = create_engine('sqlite:///:memory:')
engine = create_engine('postgresql://postgres:roop@localhost/mydb2')
Base.metadata.create_all(engine)

# Create a new session
Session = sessionmaker(bind=engine)
session = Session()

# Example of adding an Author and Books
new_author = Author(name='J.K. Rowling')
new_author.books = [
    Book(title='Harry Potter and the Philosopher\'s Stone'),
    Book(title='Harry Potter and the Chamber of Secrets')
]

# Add the author (and associated books) to the session and commit
session.add(new_author)
session.commit()

# Query the database
authors = session.query(Author).all()
for author in authors:
    print(f'Author: {author.name}')
    for book in author.books:
        print(f'  Book: {book.title}')

# Close the session
session.close()
