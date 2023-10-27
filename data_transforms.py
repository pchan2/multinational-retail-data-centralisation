import pandas as pd
import re

from pandas.core.frame import DataFrame
from pandas._libs.tslibs.timestamps import Timestamp


class DataTransforms:
    '''
    This class contains static helper methods that clean dataframes or 
    columns.
    '''
    @staticmethod
    def remove_null_values(df: DataFrame) -> DataFrame:
        '''
        This static method is used to remove null values from the ``df`` 
        dataframe.

        Args:
            df (DataFrame): the dataframe.

        Returns:
            df (DataFrame): the dataframe.
        '''
        df = df.fillna('')
        df = df.replace(to_replace='None', value='')
        df = df.replace(to_replace='Null', value='')
        df = df.replace(to_replace='NULL', value='')
        df = df.replace(to_replace='N/A', value='')
        return df

    @staticmethod
    def remove_alphanumerical_values(df: DataFrame, column_name: str) -> DataFrame:
        '''
        This static method is used to remove alphanumerical values from 
        the ``column_name`` dataframe.

        Args:
            df (DataFrame): the dataframe.
            column_name (str): the column name.

        Returns:
            df[column_name] (DataFrame): the dataframe of the column.

        Examples:
            >>> remove_alphanumerical_values(df, 'phone_number')
            >>> '+(1) 123-456-789'
            '+(1) 123-456-789'
            >>> 'ABCD12345'
            ''
        '''
        return df[column_name].apply(lambda x: '' if x.isalnum() else x)

    @staticmethod
    def remove_non_alpha_values(df: DataFrame, column_name: str) -> DataFrame:
        '''
        This static method is used to remove non-alphabetical values 
        from the ``column_name`` dataframe.

        Args:
            df (DataFrame): the dataframe.
            column_name (str): the column name.

        Returns:
            df[column_name] (DataFrame): the dataframe of the column.

        Examples:
            >>> remove_non_alpha_values(df, 'country_code')
            >>> 'US'
            'US'
            >>> 'ABCD12345'
            ''
        '''
        return df[column_name].apply(lambda x: x if x.isalpha() else '')

    @staticmethod
    def remove_values_with_non_alpha_prefix(df: DataFrame, 
                                            column_name: str) -> DataFrame:
        '''
        This static method is used to remove values with a 
        non-alphabetical prefix from the ``column_name`` dataframe.

        Valid prefixes are 2 characters long, or 3 for web denotation.

        Args:
            df (DataFrame): the dataframe.
            column_name (str): the column name.

        Returns:
            df[column_name] (DataFrame): the dataframe of the column.

        Examples:
            >>> remove_values_with_non_alpha_prefix(df, 'store_code')
            >>> 'BE-B069E157'
            'BE-B069E157'
            >>> 'WEB-1388012W'
            'WEB-1388012W'
            >>> 'ABCD12345'
            ''
        '''
        def has_correct_prefix(x): return (
            x[:2].isalpha() and x[2] == '-') or (x[:3].isalpha() 
                                                 and x[3] == '-')
        return df[column_name].apply(lambda x: 
                                     x if has_correct_prefix(x) else '')

    @staticmethod
    def remove_strings_of_undesired_length(df: DataFrame, column_name: str, 
                                           desired_length: int) -> DataFrame:
        '''
        This static method is used to remove strings of undesired length 
        from the ``column_name`` dataframe.

        Args:
            df (DataFrame): the dataframe.
            column_name (str): the column name.

        Returns:
            df[column_name] (DataFrame): the dataframe of the column.

        Examples:
        >>> remove_strings_of_undesired_length(df, 'country_code', 2)
        >>> 'US'
        'US'
        >>> 'ABCD12345'
        ''
        '''
        return df[column_name].apply(lambda x: x if len(x) == desired_length else '')

    @staticmethod
    def remove_non_digit_values(df: DataFrame, column_name: str) -> DataFrame:
        '''
        This static method is used to remove non-digit values from the 
        ``column_name`` dataframe.

        it removes values with alphabetical characters, whitespaces, etc 
        and keeps values with digits.

        Args:
            df (DataFrame): the dataframe.
            column_name (str): the column name.

        Returns:
            df[column_name] (DataFrame): the dataframe of the column.

        Examples:
            >>> remove_non_digit_values(df, 'card_number')
            >>> '123456789'
            '123456789'
            >>> 'ABCD12345'
            ''
        '''
        return df[column_name].apply(lambda x: x if x.isdigit() else '')

    @staticmethod
    def remove_non_datetime_values(df: DataFrame, 
                                   column_name: str) -> DataFrame:
        '''
        This static method is used to remove non-datetime values from 
        the ``column_name`` dataframe.

        Args:
            df (DataFrame): the dataframe.
            column_name (str): the column name.

        Returns:
            df[column_name] (DataFrame): the dataframe of the column.

        Examples:
            >>> remove_non_datetime_values(df, 'date_of_birth')
            >>> '2000-01-20'
            '2000-01-20'
            >>> 'September 2017 06'
            'September 2017 06'
            >>> 'ABCD12345'
            ''
        '''
        def is_datetime(x): return type(pd.to_datetime(x, errors='coerce'))
        return df[column_name].apply(lambda x: 
                                     x if is_datetime(x) == Timestamp else '')

    @staticmethod
    def format_datetime_values(df: DataFrame, column_name: str) -> DataFrame:
        '''
        This static method is used to format datetime values in the 
        ``column_name`` dataframe.

        Args:
            df (DataFrame): the dataframe.
            column_name (str): the column name.

        Returns:
            df[column_name] (DataFrame): the dataframe of the column.

        Examples:
            >>> format_datetime_values(df, 'date_of_birth')
            >>> '2000-01-20'
            '2000-01-20'
            >>> 'September 2017 06'
            '2017-09-06'
        '''
        return pd.to_datetime(df[column_name]).dt.strftime('%Y-%m-%d')

    @staticmethod
    def remove_non_store_types(df: DataFrame, column_name: str) -> DataFrame:
        '''
        This static method is used to remove non-store_type values from 
        the ``column_name`` dataframe.

        Args:
            df (DataFrame): the dataframe.
            column_name (str): the column name.

        Returns:
            df[column_name] (DataFrame): the dataframe of the column.

        Examples:
            >>> remove_non_store_types(df, 'store_type')
            >>> 'Local'
            'Local'
            >>> 'Mall Kiosk'
            'Mall Kiosk'
            >>> 'ABCD12345'
            ''
        '''
        store_types = ['Local', 'Super Store',
                       'Mall Kiosk', 'Outlet', 'Web Portal']
        return df[column_name].apply(lambda x: x if x in store_types else '')

    @staticmethod
    def remove_invalid_emails(df: DataFrame, column_name: str) -> DataFrame:
        '''
        This static method is used to remove invalid email addresses 
        from the ``column_name`` dataframe.

        Args:
            df (DataFrame): the dataframe.
            column_name (str): the column name.

        Returns:
            df[column_name] (DataFrame): the dataframe of the column.

        Examples:
            >>> remove_invalid_emails(df, 'email_address')
            >>> 'world@peace.com'
            'world@peace.com'
            >>> 'worldpeace.com'
            ''
        '''
        pattern = re.compile(r'([!-~])*@\w+(\.[A-Z|a-z]{2,})+')
        return df[column_name].apply(lambda x: 
                                     x if re.fullmatch(pattern, x) else '')

    @staticmethod
    def remove_non_countries(df: DataFrame, column_name: str) -> DataFrame:
        '''
        This static method is used to remove non-countries from the 
        ``column_name`` dataframe.

        Args:
            df (DataFrame): the dataframe.
            column_name (str): the column name.

        Returns:
            df[column_name] (DataFrame): the dataframe of the column.

        Examples:
            >>> remove_non_countries(df, 'country')
            >>> 'Germany'
            'Germany'
            >>> 'ABCD12345'
            ''
        '''
        countries = ['Germany', 'United Kingdom', 'United States']
        return df[column_name].apply(lambda x: x if x in countries else '')

    @staticmethod
    def correct_gb_country_code(df: DataFrame, column_name: str) -> DataFrame:
        '''
        This static method is used to correct 'GB' country code typos in 
        the ``column_name`` dataframe.

        Args:
            df (DataFrame): the dataframe.
            column_name (str): the column name.

        Returns:
            df[column_name] (DataFrame): the dataframe of the column.

        Examples:
            >>> correct_gb_country_code(df, 'country_code')
            >>> 'GGB'
            'GB'
            >>> 'US'
            'US'
        '''
        return df[column_name].apply(lambda x: 'GB' if x == 'GGB' else x)

    @staticmethod
    def remove_non_card_providers(df: DataFrame, 
                                  column_name: str) -> DataFrame:
        '''
        This static method is used to remove non-card-providers from the 
        ``column_name`` dataframe.

        Args:
            df (DataFrame): the dataframe.
            column_name (str): the column name.

        Returns:
            df[column_name] (DataFrame): the dataframe of the column.

        Examples:
            >>> remove_non_card_providers(df, 'card_provider')
            >>> 'Maestro'
            'Maestro'
            >>> 'ABCD12345'
            ''
        '''
        card_providers = ['Diners Club / Carte Blanche', 'American Express', 
                          'JCB 16 digit','JCB 15 digit', 'Maestro', 
                          'Mastercard', 'Discover', 'VISA 19 digit', 
                          'VISA 16 digit', 'VISA 13 digit']
        return df[column_name].apply(lambda x: 
                                     x if x in card_providers else '')

    @staticmethod
    def remove_strings_with_numbers(df: DataFrame, 
                                    column_name: str) -> DataFrame:
        '''
        This static method is used to remove strings with numbers from 
        the ``column_name`` dataframe.

        It removes values with digits and keeps values with alphabetical 
        characters, whitespaces, etc.

        Args:
            df (DataFrame): the dataframe.
            column_name (str): the column name.

        Returns:
            df[column_name] (DataFrame): the dataframe of the column.

        Examples:
            >>> remove_strings_with_numbers(df, 'locality')
            >>> 'High Wycombe'
            'High Wycombe'
            >>> 'ABCD12345'
            ''
        '''
        return df[column_name].apply(
            lambda x: '' if any(char.isdigit() for char in x) else x)

    @staticmethod
    def remove_strings_with_invald_weight_suffix(
        df: DataFrame, column_name: str) -> DataFrame:
        '''
        This static method is used to remove strings with invalid weight 
        suffix from the ``column_name`` dataframe.

        Args:
            df (DataFrame): the dataframe.
            column_name (str): the column name.

        Returns:
            df[column_name] (DataFrame): the dataframe of the column.

        Examples:
            >>> remove_strings_with_invald_weight_suffix(df, 'weight')
            >>> '1kg'
            '1kg'
            >>> '2.2kg'
            '2.2kg'
            >>> '30.g'
            '30.g'
            >>> '4 x 400ml'
            '4 x 400ml'
            >>> 'ABCD12345'
            ''
        '''
        PATTERN = '\d+?\.?(kg|g|ml)'
        return df[column_name].apply(lambda x: 
                                     x if re.search(PATTERN, x) else '')

    @staticmethod
    def calculate_weight_multiples(df: DataFrame, 
                                   column_name: str) -> DataFrame:
        '''
        This static method is used to calculate the total weights of 
        each row in the ``column_name`` dataframe.

        Args:
            df (DataFrame): the dataframe.
            column_name (str): the column name.

        Returns:
            df[column_name] (DataFrame): the dataframe of the column.

        Examples:
            >>> calculate_weight_multiples(df, 'weight')
            >>> '3 x 300ml'
            '900ml'
            >>> '2 x 2.5g'
            '5g'
            >>> '1kg'
            '1kg'
        '''
        PATTERN_KG_ML = 'x +((\d+?\.?\d+?)|(\d+?))(kg|ml)'
        PATTERN_G = 'x +((\d+?\.?\d+?)|(\d+?))g'
        df[column_name] = df[column_name].apply(
            lambda x: str(
                float(x.split('x')[0]) * float(x.split('x')[-1][:-2])) + x[-2]
            if re.search(PATTERN_KG_ML, x) else x)
        df[column_name] = df[column_name].apply(
            lambda x: str(
                float(x.split('x')[0]) * float(x.split('x')[-1][:-1])) + x[-1]
            if re.search(PATTERN_G, x) else x)
        return df[column_name]

    @staticmethod
    def convert_product_weights_to_kg(df: DataFrame, 
                                      column_name: str) -> DataFrame:
        '''
        This static method is used to convert the weights to floats in 
        kg in the ``column_name`` dataframe.

        Args:
            df (DataFrame): the dataframe.
            column_name (str): the column name.

        Returns:
            df[column_name] (DataFrame): the dataframe of the column.

        Examples:
            >>> convert_product_weights_to_kg(df, 'weight')
            >>> '1kg'
            1.0
            >>> '250g'
            0.25
            >>> '3500ml'
            3.5
        '''
        PATTERN_KG = '\d+?\.?kg'
        PATTERN_G = '\d+?\.?g'
        PATTERN_ML = '\d+?\.?ml'
        df[column_name] = df[column_name].apply(
            lambda x: '0' if len(x) == 0 else x)
        df[column_name] = df[column_name].apply(
            lambda x: (x[:-2] if re.search(PATTERN_KG, x) else x))
        df[column_name] = df[column_name].apply(
            lambda x: 
            str(float(x[:-1]) / 1_000 if re.search(PATTERN_G, x) else x))
        df[column_name] = df[column_name].apply(
            lambda x: 
            str(float(x[:-2]) / 1_000 if re.search(PATTERN_ML, x) else x))
        df[column_name] = df[column_name].apply(lambda x: float(x))
        return df[column_name]

    @staticmethod
    def remove_invalid_product_statuses(df: DataFrame, 
                                        column_name: str) -> DataFrame:
        '''
        This static method is used to remove invalud product statuses 
        from the ``column_name`` dataframe.

        Args:
            df (DataFrame): the dataframe.
            column_name (str): the column name.

        Returns:
            df[column_name] (DataFrame): the dataframe of the column.

        Examples:
            >>> remove_invalid_product_statuses(df, 'removed')
            >>> 'Still_avaliable'
            'Still_avaliable'
            >>> 'ABCD12345'
            ''
        '''
        statuses = ['Still_avaliable', 'Removed']
        return df[column_name].apply(lambda x: x if x in statuses else '')

    @staticmethod
    def remove_non_time_periods(df: DataFrame, 
                                column_name: str) -> DataFrame:
        '''
        This static method is used to remove non-time-periods from the 
        ``column_name`` dataframe.

        Args:
            df (DataFrame): the dataframe.
            column_name (str): the column name.

        Returns:
            df[column_name] (DataFrame): the dataframe of the column.

        Examples:
            >>> remove_non_time_periods(df, 'time_period')
            >>> 'Evening'
            'Evening'
            >>> 'ABCD12345'
            ''
        '''
        time_periods = ['Evening', 'Morning', 'Midday', 'Late_Hours']
        return df[column_name].apply(lambda x: 
                                     x if x in time_periods else '')
