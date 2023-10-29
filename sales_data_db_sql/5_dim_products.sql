-- In the dim_products table of the sales_data database:

-- Rename removed column to still_available
ALTER TABLE dim_products 
RENAME COLUMN removed TO still_available;

-- Get the maximum length of EAN.
SELECT MAX(LENGTH("EAN"))
FROM dim_products; -- 17

-- Get the maximum length of product_code.
SELECT MAX(LENGTH(product_code))
FROM dim_products; -- 11

-- Get the maximum length of weight_class.
SELECT MAX(LENGTH(weight_class))
FROM dim_products; -- 14

ALTER TABLE dim_products
ALTER COLUMN product_price TYPE FLOAT USING (NULLIF(product_price, '')::FLOAT),
    ALTER COLUMN weight TYPE FLOAT USING weight::FLOAT,
    ALTER COLUMN "EAN" TYPE VARCHAR(17),
    ALTER COLUMN product_code TYPE VARCHAR(11),
    ALTER COLUMN date_added TYPE DATE USING (NULLIF(date_added, '')::DATE),
    ALTER COLUMN uuid TYPE UUID USING (NULLIF(uuid, '')::UUID),
    ALTER COLUMN still_available TYPE BOOL USING CASE
        WHEN still_available = 'Still_available' THEN true
        WHEN still_available = 'Removed' THEN false
    END,
    ALTER COLUMN weight_class TYPE VARCHAR(14);

+-----------------+--------------------+--------------------+
|  dim_products   | current data type  | required data type |
+-----------------+--------------------+--------------------+
| product_price   | TEXT               | FLOAT              |
| weight          | TEXT               | FLOAT              |
| EAN             | TEXT               | VARCHAR(?)         |
| product_code    | TEXT               | VARCHAR(?)         |
| date_added      | TEXT               | DATE               |
| uuid            | TEXT               | UUID               |
| still_available | TEXT               | BOOL               |
| weight_class    | TEXT               | VARCHAR(?)         |
+-----------------+--------------------+--------------------+