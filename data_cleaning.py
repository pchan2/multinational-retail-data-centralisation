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
        has_correct_prefix = lambda x: (x[:2].isalpha() and x[2] == '-') or (x[:3].isalpha() and x[3] == '-')
        return df[column_name].apply(lambda x: x if has_correct_prefix(x) else '')
    
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
    
    @staticmethod
    def remove_strings_with_numbers(df: DataFrame, column_name: str) -> DataFrame:
        return df[column_name].apply(lambda x: '' if any(char.isdigit() for char in x) else x)
    
    @staticmethod
    def remove_strings_with_invald_weight_suffix(df: DataFrame, column_name: str) -> DataFrame:
        # digit plus optional digits plus optional decimal plus unit e.g 102.kg or 23ml or 38g https://regexr.com/
        PATTERN = '\d+?\.?(kg|g|ml)'
        return df[column_name].apply(lambda x: x if re.search(PATTERN, x) else '')

    @staticmethod
    def calculate_weight_multiples(df: DataFrame, column_name: str) -> DataFrame:
        # x plus whitespace(s) plus integer or float plus either kg, ml, g.
        PATTERN_KG_ML = 'x +((\d+?\.?\d+?)|(\d+?))(kg|ml)'
        PATTERN_G = 'x +((\d+?\.?\d+?)|(\d+?))g'
        df[column_name] = df[column_name].apply(lambda x: str(float(x.split('x')[0]) * float(x.split('x')[-1][:-2])) + x[-2] if re.search(PATTERN_KG_ML, x) else x)
        df[column_name] = df[column_name].apply(lambda x: str(float(x.split('x')[0]) * float(x.split('x')[-1][:-1])) + x[-1] if re.search(PATTERN_G, x) else x)
        return df[column_name]
    
    @staticmethod
    def convert_product_weights_to_kg(df: DataFrame, column_name: str) -> DataFrame:
        PATTERN_KG = '\d+?\.?kg'
        PATTERN_G = '\d+?\.?g'
        PATTERN_ML = '\d+?\.?ml'
        df[column_name] = df[column_name].apply(lambda x: '0' if len(x) == 0 else x)
        df[column_name] = df[column_name].apply(lambda x: 
                                                (x[:-2] if re.search(PATTERN_KG, x) else x))
        df[column_name] = df[column_name].apply(lambda x: 
                                                (str(float(x[:-1]) / 1_000) if re.search(PATTERN_G, x) else x))
        df[column_name] = df[column_name].apply(lambda x: 
                                                (str(float(x[:-2]) / 1_000) if re.search(PATTERN_ML, x) else x))
        df[column_name] = df[column_name].apply(lambda x: float(x))
        return df[column_name]
    
    @staticmethod
    def remove_invalid_product_statuses(df: DataFrame, column_name: str) -> DataFrame:
        statuses = ['Still_avaliable', 'Removed']
        return df[column_name].apply(lambda x: x if x in statuses else '')