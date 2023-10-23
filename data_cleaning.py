import pandas as pd
import re

from pandas.core.frame import DataFrame
from pandas._libs.tslibs.timestamps import Timestamp


class DataCleaning:
    
    def __init__(self) -> None:
        print('Initialise the new instance of DataCleaning.')

    @staticmethod
    def remove_null_values(df: DataFrame) -> DataFrame:
        df = df.fillna('')
        df = df.replace(to_replace='None', value='')
        df = df.replace(to_replace='Null', value='')
        df = df.replace(to_replace='NULL', value='')
        df = df.replace(to_replace='N/A', value='')
        return df

    # check isalnum(), if true, then we remove data
    # useful for when we want to keep '10.293'
    # useful for removing 'a99b2'
    @staticmethod
    def remove_alphanumerical_values(df: DataFrame, column_name: str) -> DataFrame:
        return df[column_name].apply(lambda x: '' if x.isalnum() else x)

    # useful for keeping alpha values and remove alphanumerical values
    @staticmethod
    def remove_non_alpha_values(df: DataFrame, column_name: str) -> DataFrame:
        return df[column_name].apply(lambda x: x if x.isalpha() else '')

    # starts with 2 alphas in prefix. 'BE-B069E157' good data. '9D4LK7X4LZ' is bad data
    @staticmethod
    def remove_values_with_non_alpha_prefix(df: DataFrame, column_name: str) -> DataFrame:
        return df[column_name].apply(lambda x: x if x[:2].isalpha() else '')
    
    # add dash in index 2. end result should be total length = 11, that's 2 + 1 + 8
    @staticmethod
    def insert_dash_in_string(df: DataFrame, column_name: str, index: int) -> DataFrame:
        return df[column_name].apply(lambda x: x if len(x) > 0 and x[index] == '-' else f'{x[:2]}-{x[2:]}')

    @staticmethod
    def remove_strings_of_undesired_length(df: DataFrame, column_name: str, desired_length: int) -> DataFrame:
        return df[column_name].apply(lambda x: x if len(x) == desired_length else '')
    
    @staticmethod
    def remove_non_digit_values(df: DataFrame, column_name: str) -> DataFrame:
        return df[column_name].apply(lambda x: x if x.isdigit() else '')
    
    @staticmethod
    def remove_non_datetime_values(df: DataFrame, column_name: str) -> DataFrame:
        return df[column_name].apply(lambda x: x if type(pd.to_datetime(x, errors='coerce')) == Timestamp else '')
    
    @staticmethod
    def format_datetime_values(df: DataFrame, column_name: str) -> DataFrame:
        return pd.to_datetime(df[column_name]).dt.strftime('%Y-%m-%d')
    
    @staticmethod
    def remove_non_store_types(df: DataFrame, column_name: str) -> DataFrame:
        store_types = ['Local', 'Super Store', 'Mall Kiosk', 'Outlet', 'Web Portal']
        return df[column_name].apply(lambda x: x if x in store_types else '')
    
    @staticmethod
    def remove_invalid_emails(df: DataFrame, column_name: str) -> DataFrame:
        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        return df[column_name].apply(lambda x: x if re.fullmatch(regex, x) else '')
    
    @staticmethod
    def remove_non_countries(df: DataFrame, column_name: str) -> DataFrame:
        countries = ['Germany', 'United Kingdom', 'United States']
        return df[column_name].apply(lambda x: x if x in countries else '')
    
    @staticmethod
    def correct_gb_country_code(df: DataFrame, column_name: str) -> DataFrame:
        return df[column_name].apply(lambda x: 'GB' if x == 'GGB' else x)
    
    @staticmethod
    def remove_integers_of_undesired_length(df: DataFrame, column_name: str, desired_length: int) -> DataFrame:
        return df[column_name].apply(lambda x: x if len(str(x)) == desired_length else 0)
    
    @staticmethod
    def remove_non_card_providers(df: DataFrame, column_name: str) -> DataFrame:
        card_providers = ['Diners Club / Carte Blanche', 'American Express', 'JCB 16 digit',
                          'JCB 15 digit', 'Maestro', 'Mastercard', 'Discover',
                          'VISA 19 digit', 'VISA 16 digit', 'VISA 13 digit']
        return df[column_name].apply(lambda x: x if x in card_providers else '')