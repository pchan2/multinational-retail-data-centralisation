-- In the dim_store_details table of the sales_data database:

-- Merge lat and latitude columns, or drop lat which is empty.
ALTER TABLE dim_store_details
DROP COLUMN lat;

-- Get the maximum length of store_code.
SELECT MAX(LENGTH(store_code))
FROM dim_store_details; -- 12

-- Get the maximum length of country_code.
SELECT MAX(LENGTH(country_code))
FROM dim_store_details; -- 2

-- Set '' longitude to 0.
UPDATE dim_store_details
SET longitude = '0'
WHERE longitude = '';

-- Set '' latitude to 0.
UPDATE dim_store_details
SET latitude = '0'
WHERE latitude = '';

-- Set new data types
ALTER TABLE dim_store_details
ALTER COLUMN longitude TYPE FLOAT USING longitude::FLOAT,
    ALTER COLUMN locality TYPE VARCHAR(255),
    ALTER COLUMN store_code TYPE VARCHAR(12),
    ALTER COLUMN staff_numbers TYPE SMALLINT USING 
        (NULLIF(staff_numbers, '')::SMALLINT),
    ALTER COLUMN opening_date TYPE DATE USING opening_date::DATE,
    ALTER COLUMN store_type TYPE VARCHAR(255),
    ALTER COLUMN latitude TYPE FLOAT USING latitude::FLOAT,
    ALTER COLUMN country_code TYPE VARCHAR(2),
    ALTER COLUMN continent TYPE VARCHAR(255);

+---------------------+-------------------+------------------------+
| store_details_table | current data type |   required data type   |
+---------------------+-------------------+------------------------+
| longitude           | TEXT              | FLOAT                  |
| locality            | TEXT              | VARCHAR(255)           |
| store_code          | TEXT              | VARCHAR(?)             |
| staff_numbers       | TEXT              | SMALLINT               |
| opening_date        | TEXT              | DATE                   |
| store_type          | TEXT              | VARCHAR(255) NULLABLE  |
| latitude            | TEXT              | FLOAT                  |
| country_code        | TEXT              | VARCHAR(?)             |
| continent           | TEXT              | VARCHAR(255)           |
+---------------------+-------------------+------------------------+