import psycopg2
from sporetracker.util.db_conn import DBUtil
from psycopg2 import OperationalError

def create_db():
    create_db = """
    CREATE DATABASE mydb;
    """
    util = DBUtil(user='postgres', password='mysecretpassword')
    util.execute(create_db)

if __name__ == "__main__":
    create_db()
