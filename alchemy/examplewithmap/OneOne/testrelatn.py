from sqlalchemy import create_engine, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, mapped_column

# Define the base class
Base = declarative_base()

# Define Parent model
class Parent(Base):
    __tablename__ = "parent_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    child: Mapped["Child"] = relationship(back_populates="parent", uselist=False)

# Define Child model
class Child(Base):
    __tablename__ = "child_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    parent_id: Mapped[int] = mapped_column(ForeignKey("parent_table.id"))
    parent: Mapped["Parent"] = relationship(back_populates="child", single_parent=True)
    __table_args__ = (UniqueConstraint("parent_id"),)

# Create a database engine
engine = create_engine('postgresql://postgres:roop@localhost/mydb1')
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# # Insert data into Parent and Child tables
# for i in range(5):
#     parent = Parent()
#     child = Child()

#     # Establish the relationship
#     parent.child = child

#     # Add Parent and Child instances to the session
#     session.add(parent)
#     session.add(child)

# # Commit the transaction
# session.commit()

# # Query to check Parent and Child relationships
# result = session.query(Parent).all()

# # Print the relationships
# for parent in result:
#     print(f"Parent ID: {parent.id}, Child ID: {parent.child.id if parent.child else 'No child'}")

# # Close the session
# session.close()

# Attempt to add a second child to an existing parent (e.g., Parent with id=1)
existing_parent = session.query(Parent).filter_by(id=1).first()

if existing_parent:
    new_child = Child(parent=existing_parent)
    
    try:
        # Add new child
        session.add(new_child)
        session.commit()
    except Exception as e:
        # Handle exception (likely due to uniqueness constraint violation)
        print(f"Error: {e}")
        session.rollback()

# Close session
session.close()
