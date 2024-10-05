import psycopg2
from psycopg2 import sql

# Establish connection
conn = psycopg2.connect(
    host="127.0.0.1",     # Localhost
    database="mydb",      # Your database name
    user="myuser",        # Your PostgreSQL username
    password="mypassword" # Your PostgreSQL password
)

# Create a cursor object
cur = conn.cursor()

# Execute an SQL query
cur.execute("SELECT version();")

# Fetch and display the result
db_version = cur.fetchone()
print(f"PostgreSQL version: {db_version}")

# Close the cursor and connection
cur.close()
conn.close()
