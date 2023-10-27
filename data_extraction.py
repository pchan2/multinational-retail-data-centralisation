import io

import boto3
import pandas as pd
import requests

from database_utils import DatabaseConnector
from pandas.core.frame import DataFrame
from tabula import read_pdf


class DataExtractor:
    '''
    This class contains data extracting methods.

    Attributes:
        database_connector (DatabaseConnector): the instance of
        DatabaseConnector.
        engine (Engine): the engine of the SQLAlchemy application.
        headers (dict): the HTTP header with the x-api-key for
        authentication.
    '''
    database_connector = DatabaseConnector()
    engine = database_connector.init_db_engine()
    headers = {'x-api-key': 'yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX'}

    def list_db_tables(self) -> list:
        '''
        This method returns a list of table names from the database
        engine.
        '''
        return self.engine.table_names()

    def read_rds_table(self, table_name: str) -> DataFrame:
        '''
        This method converts the RDS (AWS Relational Database Service)
        table to a dataframe.

        Args:
            table_name (str): the table name.

        Returns:
            df (DataFrame): the dataframe of the table.
        '''
        df = pd.read_sql_table(table_name, self.engine)
        return df

    def retrieve_pdf_data(self, pdf_filepath: str) -> DataFrame:
        '''
        This method is used to convert the PDF data to a dataframe.

        Args:
            pdf_filepath (str): the PDF filepath
            (https://data-handling-public.s3.eu-west-1.amazonaws.com/card_details.pdf).

        Returns:
            df (DataFrame): the dataframe of the PDF.
        '''
        dfs = read_pdf(pdf_filepath, pages='all')
        df = pd.concat(dfs)
        return df

    def list_number_of_stores(self, number_of_stores_endpoint: str) -> int:
        '''
        This method is used to get the number of stores from the 
        endpoint.

        Args:
            number_of_stores_endpoint (str): the endpoint to the number 
            of stores
            (https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/number_stores).

        Returns:
            number_stores (int): the number of stores.
        '''
        res = requests.get(number_of_stores_endpoint, headers=self.headers)
        number_stores = res.json()['number_stores']
        return number_stores

    def retrieve_stores_data(self, retrieve_a_store_endpoint: str, 
                             number_of_stores: int) -> DataFrame:
        '''
        This method is used to collect individual store data in a list 
        which is converted to a dataframe.

        Args: 
            retrieve_a_store_endpoint (str): the endpoint to 
            store_details
            (https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details).
            number_stores (int): the number of stores.

        Returns:
            _ (DataFrame): the dataframe of store_details.
        '''
        data = []
        for store_index in range(number_of_stores):
            endpoint = f'{retrieve_a_store_endpoint}/{store_index}'
            res = requests.get(endpoint, headers=self.headers)
            store_data = res.json()
            data.append(store_data)
        return pd.DataFrame(data)

    def extract_from_s3(self, s3_address: str) -> DataFrame:
        '''
        This method is used to get the object from the AWS S3 address 
        which is converted to a dataframe.

        Args:
            s3_address (str): the S3 address to products.csv
            (s3://data-handling-public/products.csv).

        Returns:
            df (DataFrame): the dataframe of products.
        '''
        address_parts = s3_address.split('/')
        bucket = address_parts[2]
        key_first_index = s3_address.find(address_parts[3])
        key = s3_address[key_first_index:]
        s3 = boto3.client('s3')
        obj = s3.get_object(Bucket=bucket, Key=key)
        df = pd.read_csv(io.BytesIO(obj['Body'].read()), skipinitialspace=True)
        return df
