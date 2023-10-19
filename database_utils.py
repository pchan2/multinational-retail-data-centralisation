import yaml

from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine


class DatabaseConnector():
    
    def __init__(self) -> None:
        print('Initialise the new instance of DatabaseConnector.')

    def read_db_creds(self) -> dict:
        with open('../db_creds.yaml', 'r') as file:
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