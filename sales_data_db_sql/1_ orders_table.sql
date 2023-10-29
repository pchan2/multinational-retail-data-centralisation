-- In the orders_table table of the sales_data database:

-- Change card_number type from bigint to text.
ALTER TABLE orders_table
ALTER COLUMN card_number TYPE text;

-- Get the maximum length of card_number.
SELECT MAX(LENGTH(card_number))
FROM orders_table; -- 19

-- Get the maximum  length of store_code.
SELECT MAX(LENGTH(store_code))
FROM orders_table; -- 12

-- Get the maximum  length of product_code.
SELECT MAX(LENGTH(product_code))
FROM orders_table; -- 11

-- Set new data types
ALTER TABLE orders_table
ALTER COLUMN date_uuid TYPE UUID USING date_uuid::UUID,
    ALTER COLUMN user_uuid TYPE UUID USING user_uuid::UUID,
    ALTER COLUMN card_number TYPE VARCHAR(19),
    ALTER COLUMN store_code TYPE VARCHAR(12),
    ALTER COLUMN product_code TYPE VARCHAR(11),
    ALTER COLUMN product_quantity TYPE SMALLINT;

+------------------+--------------------+--------------------+
|   orders_table   | current data type  | required data type |
+------------------+--------------------+--------------------+
| date_uuid        | TEXT               | UUID               |
| user_uuid        | TEXT               | UUID               |
| card_number      | TEXT               | VARCHAR(?)         |
| store_code       | TEXT               | VARCHAR(?)         |
| product_code     | TEXT               | VARCHAR(?)         |
| product_quantity | BIGINT             | SMALLINT           |
+------------------+--------------------+--------------------+