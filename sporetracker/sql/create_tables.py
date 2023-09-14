import psycopg2
from sporetracker.util.db_conn import DBUtil
from psycopg2 import OperationalError

def create_tables():
    create_table_grow = """
    CREATE TABLE IF NOT EXISTS grow2 (
        grow_id SERIAL PRIMARY KEY,
        start_date DATE NOT NULL,
        strain VARCHAR(255) NOT NULL,
        media_number INT NOT NULL,
        method VARCHAR(255) NOT NULL
    );
    """

    create_table_flush = """
    CREATE TABLE IF NOT EXISTS flush2 (
        flush_id SERIAL PRIMARY KEY,
        harvest_date DATE NOT NULL,
        yield DECIMAL(10, 2) NOT NULL,
        grow_id INT REFERENCES grow(grow_id)
    );
    """

    create_table_spore = """
    CREATE TABLE IF NOT EXISTS spore2 (
        spore_id SERIAL PRIMARY KEY,
        flush_number INT NOT NULL,
        catalog_number INT NOT NULL,
        origin VARCHAR(255) NOT NULL,
        grow_id INT REFERENCES grow(grow_id),
        flush_id INT REFERENCES flush(flush_id)
    );
    """
    
    util = DBUtil(dbname='mydb', user='postgres', password='mysecretpassword')
    
    util.execute(create_table_grow)
    util.execute(create_table_flush)
    util.execute(create_table_spore)

if __name__ == "__main__":
    create_tables()
