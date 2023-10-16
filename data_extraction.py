from database_utils import DatabaseConnector


class DataExtractor():
    
    def __init__(self) -> None:
        print('Initialise the new instance of DataExtractor.')
    
    def list_db_tables(self) -> None:
        engine = DatabaseConnector().init_db_engine()
        print(engine.table_names())