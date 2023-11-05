-- How many sales are coming from online?

-- The company is looking to increase its online sales.

-- They want to know how many sales are happening online vs offline.

-- Calculate how many products were sold and the amount of sales made for online
-- and offline purchases.

-- You should get the following information:

+------------------+-------------------------+----------+
| numbers_of_sales | product_quantity_count  | location |
+------------------+-------------------------+----------+
|            26957 |                  107739 | Web      |
|            93166 |                  374047 | Offline  |
+------------------+-------------------------+----------+

-- Experiment
SELECT DISTINCT(store_type),
    CASE
        WHEN store_type = 'Web Portal' THEN 'Web'
        ELSE 'Offline'
    END location
FROM dim_store_details;

-- Solution
WITH cte_store_details AS (
    SELECT store_code,
        CASE
            WHEN store_type = 'Web Portal' THEN 'Web'
            ELSE 'Offline'
        END location
    FROM dim_store_details
)
SELECT COUNT(*) AS numbers_of_sales,
    SUM(product_quantity),
    location
FROM orders_table
    JOIN cte_store_details ON cte_store_details.store_code = orders_table.store_code
GROUP BY cte_store_details.location
ORDER BY numbers_of_sales;