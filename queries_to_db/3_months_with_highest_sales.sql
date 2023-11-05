-- Which months produce the average highest cost of sales typically?

-- Query the database to find out which months typically have the most sales
-- your query should return the following information:

+-------------+-------+
| total_sales | month |
+-------------+-------+
|   673295.68 |     8 |
|   668041.45 |     1 |
|   657335.84 |    10 |
|   650321.43 |     5 |
|   645741.70 |     7 |
|   645463.00 |     3 |
+-------------+-------+

SELECT ROUND(
        SUM(product_price * product_quantity)::NUMERIC,
        2
    ) AS total_sales,
    month
FROM orders_table
    JOIN dim_products ON dim_products.product_code = orders_table.product_code
    JOIN dim_date_times ON dim_date_times.date_uuid = orders_table.date_uuid
GROUP BY dim_date_times.month
ORDER BY total_sales DESC
LIMIT 6;