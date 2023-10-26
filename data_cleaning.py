from data_transforms import DataTransforms
from pandas.core.frame import DataFrame


class DataCleaning(DataTransforms):

    def __init__(self) -> None:
        print('Initialise the new instance of DataCleaning.')

    def clean_user_data(self, df: DataFrame) -> DataFrame:
        df['date_of_birth'] = self.remove_non_datetime_values(df, 'date_of_birth')
        df['date_of_birth'] = self.format_datetime_values(df, 'date_of_birth')
        df['email_address'] = self.remove_invalid_emails(df, 'email_address')
        df['country'] = self.remove_non_countries(df, 'country')
        df['country_code'] = self.remove_non_alpha_values(df, 'country_code')
        df['country_code'] = self.correct_gb_country_code(df, 'country_code')
        df['phone_number'] = self.remove_alphanumerical_values(df, 'phone_number')
        df['join_date'] = self.remove_non_datetime_values(df, 'join_date')
        df['join_date'] = self.format_datetime_values(df, 'join_date')
        del df['index']
        df = df[((df['email_address'] != '') & (df['address'] != '') & (df['country'] != '') & (df['phone_number'] != ''))]
        df = df.drop_duplicates()
        df = self.remove_null_values(df)
        return df

    def clean_card_data(self, df: DataFrame) -> DataFrame:
        df['card_provider'] = self.remove_non_card_providers(df, 'card_provider')
        df['date_payment_confirmed'] = self.remove_non_datetime_values(df, 'date_payment_confirmed')
        df['date_payment_confirmed'] = self.format_datetime_values(df, 'date_payment_confirmed')
        df['expiry_date'] = self.remove_alphanumerical_values(df, 'expiry_date')
        df['card_number'] = df['card_number'].astype(str)
        df['card_number'] = self.remove_non_digit_values(df, 'card_number')
        df['card_number'] = df['card_number'].replace('', 0)
        df['card_number'] = df['card_number'].astype(int)
        df = df[df.card_number != 0]
        df = df.drop_duplicates()
        df = self.remove_null_values(df)
        return df

    def clean_store_data(self, df: DataFrame) -> DataFrame:
        df['longitude'] = self.remove_alphanumerical_values(df, 'longitude')
        df['locality'] = self.remove_strings_with_numbers(df, 'locality')
        df['store_code'] = self.remove_values_with_non_alpha_prefix(df, 'store_code')
        df['staff_numbers'] = self.remove_non_digit_values(df, 'staff_numbers')
        df['opening_date'] = self.remove_non_datetime_values(df, 'opening_date')
        df['opening_date'] = self.format_datetime_values(df, 'opening_date')
        df['store_type'] = self.remove_non_store_types(df, 'store_type')
        df['latitude'] = self.remove_alphanumerical_values(df, 'latitude')
        df['country_code'] = self.remove_strings_of_undesired_length(df, 'country_code', 2)
        df['continent'] = self.remove_non_alpha_values(df, 'continent')
        df['continent'] = df['continent'].replace('eeEurope', 'Europe')
        df['continent'] = df['continent'].replace('eeAmerica', 'America')
        df = df[(df.address != '') & (df.store_code != '')]
        del df['index']
        df = df.drop_duplicates()
        df = self.remove_null_values(df)
        return df

    def convert_product_weights(self, df: DataFrame) -> DataFrame:
        df['weight'] = self.remove_strings_with_invald_weight_suffix(df, 'weight')
        df['weight'] = self.calculate_weight_multiples(df, 'weight')
        df['weight'] = df['weight'].apply(lambda x: x.strip(' .') if x == '77g .' else x)
        df['weight'] = self.convert_product_weights_to_kg(df, 'weight')
        return df['weight']

    def clean_products_data(self, df: DataFrame) -> DataFrame:
        df['weight'] = self.convert_product_weights(df)
        df['product_price'] = self.remove_alphanumerical_values(df, 'product_price')
        df['category'] = self.remove_alphanumerical_values(df, 'category')
        df['date_added'] = self.remove_non_datetime_values(df, 'date_added')
        df['date_added'] = self.format_datetime_values(df, 'date_added')
        df['removed'] = self.remove_invalid_product_statuses(df, 'removed')
        del df['Unnamed: 0']
        df = df[((df['product_name'] != '') & (df['EAN'] != '') & (df['uuid'] != '') & (df['product_code'] != ''))]
        df = df.drop_duplicates()
        df = self.remove_null_values(df)
        return df

    def clean_orders_data(self, df: DataFrame) -> DataFrame:
        df['card_number'] = DataCleaning.remove_integers_of_undesired_length(df, 'card_number', 16)
        df = df.drop(['level_0', 'index', 'first_name', 'last_name', '1'], axis=1)
        df = df.drop_duplicates()
        df = self.remove_null_values(df)
        return df