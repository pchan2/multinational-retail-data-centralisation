-- In the sales_data database:

-- Set the uuid as primary key in dim_users table.
ALTER TABLE dim_users
ADD PRIMARY KEY (user_uuid);

-- Set the store_code as primary key in dim_store_details table.
ALTER TABLE dim_store_details
ADD PRIMARY KEY (store_code);

-- Set the product_code as primary key in dim_products table.
ALTER TABLE dim_products
ADD PRIMARY KEY (product_code);

-- Set the date_uuid as primary key in dim_date_times table.
ALTER TABLE dim_date_times
ADD PRIMARY KEY (date_uuid);

-- Set the card_number as primary key in dim_card_details table.
ALTER TABLE dim_card_details
ADD PRIMARY KEY (card_number);