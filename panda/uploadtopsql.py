import pandas as pd
from sqlalchemy import create_engine, Column, Float, String, Integer, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from csvclean import cleaneddf
import logging

# Set up logging configuration
logging.basicConfig(filename='sql_upload.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Create the base class for ORM
Base = declarative_base()

# Define the ORM class
class IrisData(Base):
    __tablename__ = 'iris_data'
    id = Column(Integer, primary_key=True, autoincrement=True)
    sepal_length = Column(Float)
    sepal_width = Column(Float)
    petal_length = Column(Float)
    petal_width = Column(Integer)
    variety = Column(String)
    date = Column(Date)


# Establish connection to the PostgreSQL database
engine = create_engine('postgresql://postgres:roop@localhost/mydb')
Session = sessionmaker(bind=engine)

# Create the table if it doesn't exist
Base.metadata.create_all(engine)

# Function to upload DataFrame in batches
def upload_data_in_batches(df, batch_size=10):
    # Start a session
    session = Session()
    try:
        # Convert DataFrame to a list of dictionaries for batch processing
        records = df.to_dict(orient='records')
       
        # Process records in batches
        for i in range(0, len(records), batch_size):
            batch = records[i:i + batch_size]
            session.bulk_insert_mappings(IrisData, batch)
            print(f"Inserted batch {i // batch_size + 1}")
        
        # Commit the session after all batches are processed
        session.commit()
    except Exception as e:
        session.rollback()
        print(f"Error: {e}")
        logging.error(f"Error occurred while inserting batch: {e}")
    finally:
        session.close()



# Call the function to upload data
upload_data_in_batches(cleaneddf)
