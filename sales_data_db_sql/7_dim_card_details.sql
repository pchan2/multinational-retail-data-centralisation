-- In the dim_card_details table of the sales_data database:

-- Set card_number data type to text.
ALTER TABLE dim_card_details
ALTER COLUMN card_number TYPE TEXT;

-- Get the maximum length of card_number.
SELECT MAX(LENGTH(card_number))
FROM dim_card_details; -- 19

-- Get the maximum length of expiry_date.
SELECT MAX(LENGTH(expiry_date))
FROM dim_card_details; -- 5

-- Set new data types
ALTER TABLE dim_card_details
ALTER COLUMN card_number TYPE VARCHAR(19),
    ALTER COLUMN expiry_date TYPE VARCHAR(5),
    ALTER COLUMN date_payment_confirmed TYPE DATE USING 
        date_payment_confirmed::DATE;

+------------------------+-------------------+--------------------+
|    dim_card_details    | current data type | required data type |
+------------------------+-------------------+--------------------+
| card_number            | TEXT              | VARCHAR(?)         |
| expiry_date            | TEXT              | VARCHAR(?)         |
| date_payment_confirmed | TEXT              | DATE               |
+------------------------+-------------------+--------------------+