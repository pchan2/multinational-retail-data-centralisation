-- What percentage of sales come through each type of store?

-- The sales team wants to know which of the different store types is generated 
-- the most revenue so they know where to focus.

-- Find out the total and percentage of sales coming from each of the different 
-- store types.

-- The query should return:

+-------------+-------------+---------------------+
| store_type  | total_sales | percentage_total(%) |
+-------------+-------------+---------------------+
| Local       |  3440896.52 |               44.87 |
| Web portal  |  1726547.05 |               22.44 |
| Super Store |  1224293.65 |               15.63 |
| Mall Kiosk  |   698791.61 |                8.96 |
| Outlet      |   631804.81 |                8.10 |
+-------------+-------------+---------------------+

-- Experiment
SELECT store_type,
    ROUND(
        SUM(product_price * product_quantity)::NUMERIC,
        2
    ) AS total_sales
FROM orders_table
    JOIN dim_store_details ON dim_store_details.store_code = orders_table.store_code
    JOIN dim_products ON dim_products.product_code = orders_table.product_code
GROUP BY dim_store_details.store_type
ORDER BY total_sales DESC;

-- Solution
WITH cte_total_sales_by_store_type AS (
    SELECT store_type,
        ROUND(
            SUM(product_price * product_quantity)::NUMERIC,
            2
        ) AS total_sales
    FROM orders_table
        JOIN dim_store_details ON dim_store_details.store_code = orders_table.store_code
        JOIN dim_products ON dim_products.product_code = orders_table.product_code
    GROUP BY dim_store_details.store_type
)
SELECT store_type,
    total_sales,
    ROUND(
        (total_sales / SUM(total_sales) OVER ()) * 100,
        2
    ) AS "percentage_total(%)"
FROM cte_total_sales_by_store_type
ORDER BY total_sales DESC;