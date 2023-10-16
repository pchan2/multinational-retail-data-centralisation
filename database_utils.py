import yaml

class DatabaseConnector:
    
    def read_db_creds() -> dict:
        with open('db_creds.yaml', 'r') as file:
            db_creds = yaml.safe_load(file)
            return db_creds