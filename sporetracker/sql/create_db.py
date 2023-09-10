import psycopg2
from sporetracker.util.db_conn import BaseConn
from psycopg2 import OperationalError

create_db = """
CREATE DATABASE mydb;
"""

if __name__ == "__main__":
    try:
        conn = BaseConn(user='postgres', password='mysecretpassword')
        conn.connect()
        conn.connection.autocommit = True

        cursor = conn.connection.cursor()

        cursor.execute(create_db)
        
        conn.connection.commit()

        print("Database created successfully!")

    except OperationalError as e:
        print(f"Error connecting to PostgreSQL: {e}")
    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if conn:
            conn.disconnect()
