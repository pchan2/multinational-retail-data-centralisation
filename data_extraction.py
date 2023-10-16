import pandas as pd

from database_utils import DatabaseConnector
from pandas.core.frame import DataFrame


class DataExtractor():
    
    def __init__(self) -> None:
        self.database_connector = DatabaseConnector()
        self.engine = self.database_connector.init_db_engine()
    
    def list_db_tables(self) -> list:
        return self.engine.table_names()
    
    def read_rds_table(self, table_name: str) -> DataFrame:
        df = pd.read_sql_table(table_name, self.engine)
        return df