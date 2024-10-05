import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="127.0.0.1",
    database="mydb",
    user="postgres",
    password="roop"
)

# Create a cursor object
cur = conn.cursor()

# Create a new table
cur.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        salary NUMERIC
    );
""")

# Insert data into the table
cur.execute("""
    INSERT INTO employees (name, salary)
    VALUES ('John Doe', 50000), ('Jane Smith', 60000);
""")

# Commit the transaction
conn.commit()

# Retrieve data from the table
cur.execute("SELECT * FROM employees;")
rows = cur.fetchall()
for row in rows:
    print(row)

# Close the connection
cur.close()
conn.close()
