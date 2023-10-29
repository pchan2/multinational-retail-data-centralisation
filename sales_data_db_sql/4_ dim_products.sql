-- In the dim_products table of the sales_data database:

-- Remove £ from product_price.
UPDATE dim_products
SET product_price = LTRIM(product_price, '£');

-- Add a new column weight_class based on the following conditions.
ALTER TABLE dim_products
ADD COLUMN weight_class VARCHAR;

-- Failed attempt.
INSERT INTO dim_products (weight_class)
SELECT CASE
        WHEN weight < 2 THEN 'Light'
        WHEN weight >= 2
        AND weight < 40 THEN 'Mid_Sized'
        WHEN weight >= 40
        AND weight < 140 THEN 'Heavy'
        WHEN weight >= 140 THEN 'Truck_Required'
    END
FROM dim_products;

-- Passed attempt.
UPDATE dim_products
SET weight_class = CASE
        WHEN weight < 2 THEN 'Light'
        WHEN weight >= 2
        AND weight < 40 THEN 'Mid_Sized'
        WHEN weight >= 40
        AND weight < 140 THEN 'Heavy'
        WHEN weight >= 140 THEN 'Truck_Required'
    END;

-- Passed attempt.
UPDATE dim_products
SET weight_class = 'Light'
WHERE weight < 2;

UPDATE dim_products
SET weight_class = 'Mid_Sized'
WHERE weight >= 2
    AND weight < 40;

UPDATE dim_products
SET weight_class = 'Heavy'
WHERE weight >= 40
    AND weight < 140;

UPDATE dim_products
SET weight_class = 'Truck_Required'
WHERE weight >= 140;

+--------------------------+-------------------+
| weight_class VARCHAR(?)  | weight range(kg)  |
+--------------------------+-------------------+
| Light                    | < 2               |
| Mid_Sized                | >= 2 - < 40       |
| Heavy                    | >= 40 - < 140     |
| Truck_Required           | => 140            |
+----------------------------+-----------------+