import pandas as pd
from sqlalchemy import create_engine, Column, Float, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from csvclean import df

# Create the base class for ORM
Base = declarative_base()

# Define the ORM class
class IrisData(Base):
    __tablename__ = 'iris_data'
    id = Column(Integer, primary_key=True, autoincrement=True)
    sepal_length = Column(Float)
    sepal_width = Column(Float)
    petal_length = Column(Float)
    petal_width = Column(Float)
    variety = Column(String)

# Establish connection to the PostgreSQL database
engine = create_engine('postgresql://postgres:roop@localhost/mydb')
Session = sessionmaker(bind=engine)
session = Session()

# Create the table if it doesn't exist
Base.metadata.create_all(engine)

# Function to map DataFrame to ORM objects
def map_dataframe_to_orm(df):
    objects = []
    for _, row in df.iterrows():
        obj = IrisData(
            sepal_length=row['sepal.length'],
            sepal_width=row['sepal.width'],
            petal_length=row['petal.length'],
            petal_width=row['petal.width'],
            variety=row['variety']
        )
        objects.append(obj)
    return objects

# Example DataFrame
# data = {'sepal.length': [5.1, 4.9], 'sepal.width': [3.5, 3.0], 'petal.length': [1.4, 1.4], 'petal.width': [0.2, 0.2], 'variety': ['Setosa', 'Setosa']}
# df = pd.DataFrame(data)

# Map DataFrame to ORM objects and insert into the database using add_all()
try:
    objects = map_dataframe_to_orm(df)
    session.add_all(objects)
    session.commit()
except Exception as e:
    session.rollback()
    print(f"Error: {e}")