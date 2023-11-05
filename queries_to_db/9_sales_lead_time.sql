-- How quickly is the company making sales?

-- Sales would like to get an accurate metric for how quickly the company is 
-- making sales.

-- Determine the average time taken between each sale grouped by year, the query 
-- should return the following information:

 +------+--------------------------------------------------------+
 | year |                           actual_time_taken            |
 +------+--------------------------------------------------------+
 | 2013 | "hours": 2, "minutes": 17, "seconds": 12, "millise..." |
 | 1993 | "hours": 2, "minutes": 15, "seconds": 35, "millise..." |
 | 2002 | "hours": 2, "minutes": 13, "seconds": 50, "millise..." | 
 | 2022 | "hours": 2, "minutes": 13, "seconds": 6,  "millise..." |
 | 2008 | "hours": 2, "minutes": 13, "seconds": 2,  "millise..." |
 +------+--------------------------------------------------------+
 
--  Hint: You will need the SQL command LEAD.

-- Experiment
SELECT year,
    CONCAT(year, '-', month, '-', day, ' ', timestamp)::TIMESTAMP
        AS order_timestamp
FROM dim_date_times
GROUP BY year,
    order_timestamp
ORDER BY order_timestamp;

-- Solution
WITH cte_order_timestamp AS (
    SELECT year,
        CONCAT(year, '-', month, '-', day, ' ', timestamp)::TIMESTAMP
            AS order_timestamp
    FROM dim_date_times
    ORDER BY order_timestamp
),
cte_lead_order_time AS (
    SELECT year,
        AGE(
            LEAD(order_timestamp) OVER (
                PARTITION BY year
                ORDER BY order_timestamp
            ),
            order_timestamp
        ) AS difference
    FROM cte_order_timestamp
)
SELECT year,
    AVG(difference) AS actual_time_taken
FROM cte_lead_order_time
GROUP BY year
ORDER BY actual_time_taken DESC
LIMIT 5;