-- Which German store type is selling the most?

-- The sales team is looking to expand their territory in Germany. Determine which type of store is generating the most sales in Germany.

-- The query will return:

+--------------+-------------+--------------+
| total_sales  | store_type  | country_code |
+--------------+-------------+--------------+
|   198373.57  | Outlet      | DE           |
|   247634.20  | Mall Kiosk  | DE           |
|   384625.03  | Super Store | DE           |
|  1109909.59  | Local       | DE           |
+--------------+-------------+--------------+

SELECT ROUND(
        SUM(product_price * product_quantity)::NUMERIC,
        2
    ) AS total_sales,
    store_type,
    country_code
FROM orders_table
    JOIN dim_store_details
        ON dim_store_details.store_code = orders_table.store_code
    JOIN dim_products
        ON dim_products.product_code = orders_table.product_code
WHERE country_code = 'DE'
GROUP BY store_type,
    country_code
ORDER BY total_sales;