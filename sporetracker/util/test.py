import psycopg2

# Database connection parameters for the PostgreSQL server (without specifying a database name)
db_params = {
    'user': 'postgres',    # Replace with your PostgreSQL username
    'password': 'mysecretpassword',  # Replace with your PostgreSQL password
    'host': 'localhost',        # Replace with your PostgreSQL host
    'port': '5432'              # Replace with your PostgreSQL port
}

try:
    # Establish a connection to the PostgreSQL server (without specifying a database name)
    conn = psycopg2.connect(**db_params)

    # Create a cursor object
    cursor = conn.cursor()

    # Define the SQL statement to create the 'mydb' database
    create_db_query = "CREATE DATABASE mydb;"

    # Execute the SQL statement to create the database
    cursor.execute(create_db_query)

    print("Database 'mydb' created successfully!")

except psycopg2.Error as e:
    print(f"Error creating 'mydb' database: {e}")

finally:
    # Close the cursor and connection
    if cursor:
        cursor.close()
    if conn:
        conn.close()

