-- In the dim_date_times table of the sales_data database:

-- Get the maximum length of month.
SELECT MAX(LENGTH(month))
FROM dim_date_times; -- 2

-- Get the maximum length of year.
SELECT MAX(LENGTH(year))
FROM dim_date_times; -- 4

-- Get the maximum length of day.
SELECT MAX(LENGTH(day))
FROM dim_date_times; -- 2

-- Get the maximum length of time_period.
SELECT MAX(LENGTH(time_period))
FROM dim_date_times; -- 10

-- Set new data types
ALTER TABLE dim_date_times
ALTER COLUMN month TYPE VARCHAR(2),
    ALTER COLUMN year TYPE VARCHAR(4),
    ALTER COLUMN day TYPE VARCHAR(2),
    ALTER COLUMN time_period TYPE VARCHAR(10),
    ALTER COLUMN date_uuid TYPE UUID USING date_uuid::UUID;

+-----------------+-------------------+--------------------+
| dim_date_times  | current data type | required data type |
+-----------------+-------------------+--------------------+
| month           | TEXT              | VARCHAR(?)         |
| year            | TEXT              | VARCHAR(?)         |
| day             | TEXT              | VARCHAR(?)         |
| time_period     | TEXT              | VARCHAR(?)         |
| date_uuid       | TEXT              | UUID               |
+-----------------+-------------------+--------------------+