import yaml

from pandas.core.frame import DataFrame
from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine


class DatabaseConnector():
    
    def __init__(self) -> None:
        print('Initialise the new instance of DatabaseConnector.')

    def read_db_creds(self) -> dict:
        try:
            with open('../db_creds.yaml', 'r') as file:
                db_creds = yaml.safe_load(file)
                return db_creds
        except:
            with open('db_creds.yaml', 'r') as file:
                db_creds = yaml.safe_load(file)
                return db_creds

    def init_db_engine(self) -> Engine:
        db_creds = self.read_db_creds()
        DATABASE_TYPE = 'postgresql'
        DBAPI = 'psycopg2'
        ENDPOINT = db_creds['RDS_HOST']
        USER = db_creds['RDS_USER']
        PASSWORD = db_creds['RDS_PASSWORD']
        PORT = db_creds['RDS_PORT']
        DATABASE = db_creds['RDS_DATABASE']
        engine = create_engine(f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{ENDPOINT}:{PORT}/{DATABASE}")
        return engine
    
    def init_sales_data_db_engine(self) -> Engine:
        DATABASE_TYPE = 'postgresql'
        DBAPI = 'psycopg2'
        ENDPOINT = 'localhost'
        USER = 'postgres'
        PASSWORD = '' #password
        PORT = 5432
        DATABASE = 'sales_data'
        engine = create_engine(f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{ENDPOINT}:{PORT}/{DATABASE}")
        return engine
    
    def upload_to_db(self, df: DataFrame, table_name: str) -> None:
        engine = self.init_sales_data_db_engine()
        df.to_sql(table_name, con=engine, index=True, index_label='index', if_exists='replace')