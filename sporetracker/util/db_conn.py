import psycopg2
from psycopg2 import OperationalError

class DBUtil:
    def __init__(self, user, password, dbname=None, host='localhost', port='5432'):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        
        self.db_mode = self.fetch_db_mode()
        self.connection = None
    
    def fetch_db_mode(self):
        if self.dbname == None:
            return True
        else:
            return False
        
    def connect(self):
        try:
            self.connection = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )

            if self.db_mode == True:
                self.connection.autocommit = True
            print("Connected to PostgreSQL!")
        except OperationalError as e:
            print(f"Error connecting to PostgreSQL: {e}")

    def execute(self, query):
        self.connect()

        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()
            return cursor.fetchall()
            cursor.close()
        except Exception as e:
            print(f"Error executing query: {e}")
            
        self.connection.close()
        