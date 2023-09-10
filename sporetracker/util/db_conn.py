import psycopg2
from psycopg2 import OperationalError

class DBConn:
    def __init__(self, dbname, user, password, host='localhost', port='5432'):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.connection = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            print("Connected to PostgreSQL!")
        except OperationalError as e:
            print(f"Error connecting to PostgreSQL: {e}")

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Disconnected from PostgreSQL!")

    def execute_query(self, query):
        if self.connection:
            try:
                cursor = self.connection.cursor()
                cursor.execute(query)
                return cursor.fetchall()
            except Exception as e:
                print(f"Error executing query: {e}")
        else:
            print("Not connected to PostgreSQL. Call connect() first.")
