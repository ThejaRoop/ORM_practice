from sqlalchemy import Column, Integer, String, ForeignKey, Table, create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship

class Base(DeclarativeBase):
    pass


# Association table for the many-to-many relationship between Post and Tag
post_tags = Table('post_tags', Base.metadata,
    Column('post_id', ForeignKey('posts.id'), primary_key=True),
    Column('tag_id', ForeignKey('tags.id'), primary_key=True)
)

# 1. User Table (One-to-One with Profile, One-to-Many with Post)
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(100))
    
    # One-to-One relationship with Profile
    profile = relationship("Profile", back_populates="user", uselist=False)
    
    # One-to-Many relationship with Post
    posts = relationship("Post", back_populates="user")

# 2. Profile Table (One-to-One with User)
class Profile(Base):
    __tablename__ = 'profiles'
    id = Column(Integer, primary_key=True)
    bio = Column(String(255))
    user_id = Column(Integer, ForeignKey('users.id'))
    
    # One-to-One back reference to User
    user = relationship("User", back_populates="profile")

# 3. Post Table (Many-to-One with User, Many-to-Many with Tag)
class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    content = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    
    # Many-to-One relationship with User
    user = relationship("User", back_populates="posts")
    
    # Many-to-Many relationship with Tag
    tags = relationship("Tag", secondary=post_tags, back_populates="posts")

# 4. Tag Table (Many-to-Many with Post)
class Tag(Base):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    description = Column(String)
    
    # Many-to-Many relationship with Post
    posts = relationship("Post", secondary=post_tags, back_populates="tags")

engine = create_engine('postgresql://postgres:roop@localhost/mydb2')

try:
    Base.metadata.create_all(engine)
except Exception as e:
    print(f"Error while creating tables: {e}")

# Session setup to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# # Example data insertion
# # Create a user and a profile (One-to-One)
# user1 = User(name="John Doe", email="john@example.com")
# profile1 = Profile(bio="This is John's bio", user=user1)

# # Create posts for the user (One-to-Many)
# post1 = Post(title="Post 1", content="Content of Post 1", user=user1)
# post2 = Post(title="Post 2", content="Content of Post 2", user=user1)

# # Create tags (Many-to-Many)
# tag1 = Tag(name="Tag 1", description="Tag description 1")
# tag2 = Tag(name="Tag 2", description="Tag description 2")

# # Associate posts with tags (Many-to-Many)
# post1.tags.append(tag1)
# post1.tags.append(tag2)
# post2.tags.append(tag1)

# # Add and commit all to the session
# session.add(user1)
# session.commit()

# # Query the user, profile, and posts
# user = session.query(User).filter_by(name="John Doe").first()
# print(f"User: {user.name}, Email: {user.email}")
# print(f"Profile: {user.profile.bio}")
# for post in user.posts:
#     print(f"Post: {post.title}, Tags: {[tag.name for tag in post.tags]}")
