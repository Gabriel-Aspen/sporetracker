from sqlalchemy import create_engine

class PandasUtil:
    def __init__(self, dbname, user='postgres', password='mysecretpassword', host='localhost', port='5432'):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        
        self.engine = None
        
    def get_engine(self):
        db_connection = f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.dbname}"
        engine = create_engine(db_connection)
        self.engine = engine
        
    def to_db(self, table, df, if_exists='append'):
        self.get_engine()
        df.to_sql(table, self.engine, if_exists=if_exists, index=False)
        self.engine.dispose()