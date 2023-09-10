import psycopg2
from sporetracker.util.db_conn import DBConn
from psycopg2 import OperationalError


# Database connection parameters
db_params = {
    'dbname': 'mydb',      # Replace with your database name
    'user': 'myuser',      # Replace with your database username
    'password': 'mypassword',  # Replace with your database password
    'host': 'localhost',   # Replace with your database host
    'port': '5432'         # Replace with your database port
}

# SQL statements to create tables

create_table_grow = """
CREATE TABLE IF NOT EXISTS grow (
    grow_id SERIAL PRIMARY KEY,
    start_date DATE NOT NULL,
    strain VARCHAR(255) NOT NULL,
    media_number INT NOT NULL,
    method VARCHAR(255) NOT NULL
);
"""

create_table_flush = """
CREATE TABLE IF NOT EXISTS flush (
    flush_id SERIAL PRIMARY KEY,
    harvest_date DATE NOT NULL,
    yield DECIMAL(10, 2) NOT NULL,
    grow_id INT REFERENCES grow(grow_id)
);
"""

create_table_spore = """
CREATE TABLE IF NOT EXISTS spore (
    spore_id SERIAL PRIMARY KEY,
    flush_number INT NOT NULL,
    catalog_number INT NOT NULL,
    origin VARCHAR(255) NOT NULL,
    grow_id INT REFERENCES grow(grow_id),
    flush_id INT REFERENCES flush(flush_id)
);
"""

if __name__ == "__main__":
    try:
        conn = DBConn(dbname='mydb', user='postgres', password='mysecretpassword')
        conn.connect()

        cursor = conn.connection.cursor()

        cursor.execute(create_table_grow)
        cursor.execute(create_table_flush)
        cursor.execute(create_table_spore)

        conn.connection.commit()

        print("Tables created successfully!")

    except OperationalError as e:
        print(f"Error connecting to PostgreSQL: {e}")
    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if conn:
            conn.disconnect()
