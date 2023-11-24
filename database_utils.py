import yaml

from pandas.core.frame import DataFrame
from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine


class DatabaseConnector:
    '''
    This class is used to represent a database connector.
    '''
    def read_db_creds(self, credentials_filename: str) -> dict:
        '''
        This method reads the yaml file.

        If the method is called from a child directory, the try block
        will be executed. If it is called from the same level directory,
        the except block will be executed.

        Args:
            credentials_filename (str): the filename of the database
            credentials.

        Returns:
            db_creds (dict): the database credentials.
        '''
        try:
            with open(f'../{credentials_filename}.yaml', 'r') as file:
                db_creds = yaml.safe_load(file)
                return db_creds
        except:
            with open(f'{credentials_filename}.yaml', 'r') as file:
                db_creds = yaml.safe_load(file)
                return db_creds

    def init_db_engine(self, credentials_filename: str) -> Engine:
        '''
        This method initialises the SQLAlchemy engine with the database
        credentials.

        Args:
            credentials_filename (str): the filename of the database
            credentials.

        Returns:
            engine (Engine): the database engine.
        '''
        db_creds = self.read_db_creds(credentials_filename)
        DATABASE_TYPE = 'postgresql'
        DBAPI = 'psycopg2'
        ENDPOINT = db_creds['ENDPOINT']
        USER = db_creds['USER']
        PASSWORD = db_creds['PASSWORD']
        PORT = db_creds['PORT']
        DATABASE = db_creds['DATABASE']
        engine = create_engine(
            f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{ENDPOINT}:{PORT}/{DATABASE}")
        return engine

    def upload_to_db(self, df: DataFrame, table_name: str) -> None:
        '''
        This method initialises the SQLAlchemy engine with the database
        credentials.

        Args:
            df (DataFrame): the dataframe to upload to PostgreSQL.
            table_name (str): the table name in the sales_data database.
        '''
        engine = self.init_db_engine('local_creds')
        df.to_sql(table_name, con=engine, index=True,
                  index_label='index', if_exists='replace')
