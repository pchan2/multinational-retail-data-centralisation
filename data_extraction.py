import boto3
import pandas as pd
import requests

from database_utils import DatabaseConnector
from pandas.core.frame import DataFrame
from tabula import read_pdf


class DataExtractor():
    
    def __init__(self) -> None:
        self.database_connector = DatabaseConnector()
        self.engine = self.database_connector.init_db_engine()
        self.headers = {'x-api-key': 'yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX'}
    
    def list_db_tables(self) -> list:
        return self.engine.table_names()
    
    def read_rds_table(self, table_name: str) -> DataFrame:
        df = pd.read_sql_table(table_name, self.engine)
        return df
    
    def retrieve_pdf_data(self, pdf_link: str) -> DataFrame:
        dfs = read_pdf(pdf_link, pages='all')
        df = pd.concat(dfs)
        return df

    def list_number_of_stores(self, number_of_stores_endpoint: str) -> int:
        # https://stackoverflow.com/questions/5517281/place-api-key-in-headers-or-url
        # Custom Header: curl -H "X-API-KEY: 6fa741de1bdd1d91830ba" https://api.mydomain.com/v1/users
        # curl -H 'x-api-key: yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX' https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/number_stores
        res = requests.get(number_of_stores_endpoint, headers=self.headers)
        number_stores = res.json()['number_stores']
        return number_stores
    
    def retrieve_stores_data(self, retrieve_a_store_endpoint: str, number_of_stores: int) -> DataFrame:
        data = []
        for i in range(number_of_stores):
            endpoint = f'{retrieve_a_store_endpoint}/{i}'
            res = requests.get(endpoint, headers=self.headers)
            store_data = res.json()
            data.append(store_data)
        return pd.DataFrame(data)
    
    def extract_from_s3(self, s3_address: str, destination: str) -> None:
        address_parts = s3_address.split('/')
        source_bucket = address_parts[2]
        source_filename_first_index = s3_address.find(address_parts[3])
        source_filename = s3_address[source_filename_first_index:]
        s3 = boto3.client('s3')
        s3.download_file(source_bucket, source_filename, destination)