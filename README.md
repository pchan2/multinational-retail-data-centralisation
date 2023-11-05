# Multinational Retail Data

## Table of contents

* [Description](#description)
* [Learnings](#learnings)
* [Milestones](#milestones)
* [Installation](#installation)
* [Usage](#usage)
* [File structure of the project](#file-structure-of-the-project)
* [License](#license)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

## Description

Multinational Retail Data contains data of the following:
- card details.
- date times.
- users.
- products.
- store details.

The orders table is the single source of truth in the star schema, connecting to the tables above.

In this project, the full ETL is performed.

## Learnings
- [https://regexr.com/](https://regexr.com/)
- [https://www.asciitable.com/](https://www.asciitable.com/)
- [place-api-key-in-headers-or-url](https://stackoverflow.com/questions/5517281/place-api-key-in-headers-or-url)
    - To access data that requires an API Key, run:  
      `curl -H "X-API-KEY: <Example API Key 6fa741de1bdd1d91830ba>" <Example End Point `
      `https://api.mydomain.com/v1/users>`
- [making-python-imports-more-structured](https://stackoverflow.com/questions/7374100/making-python-imports-more-structured)
    1. standard libraries alphabetical with 'imports' before 'from' like this:  
        import csv  
        import logging  
        from collections import defaultdict  
        from datetime import date  
        #(blank line)
    2. third party packages alphabetical with imports first:  
        import numpy as  np  
        import pandas as pd  
        from statsmodels import api as sm  
        #(blank line again)
    3. your own stuff (also alphabetical):  
        from my_other_folder import my_other_file
- [postgres-change-column-from-type-text-to-uuid](https://varunver.wordpress.com/2020/07/07/postgres-change-column-from-type-text-to-uuid/)
- [LTRIM, RTRIM, BTRIM trim functions](https://www.postgresqltutorial.com/postgresql-string-functions/postgresql-trim-function/)
- [INSERT INTO + CASE STATEMENT](https://gis.stackexchange.com/questions/365860/postgresql-postgis-insert-values-in-a-new-column-with-a-case-statement)
- [INSERT INTO / UPDATE + CASE STATEMENT](https://www.devart.com/dbforge/sql/sqlcomplete/sql-case-expression.html)
- Use double quotation marks when the column name is:.
    - All uppercase `SELECT "EAN" FROM dim_products;`
    - Complex `SELECT example_col AS "percentage(%)"`
- [alter-column-text-to-boolean](https://stackoverflow.com/questions/48877158/postgresql-9-4-alter-column-text-to-boolean-with-values)
- [Alter empty string to date type](https://dba.stackexchange.com/questions/108227/postgres-converting-into-nulls)
- [Add primary key](https://www.commandprompt.com/education/postgresql-primary-key-a-complete-guide/)
- [Add foreign key](https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-foreign-key/)
- [OVER () function](https://www.postgresql.org/docs/current/tutorial-window.html)
- [Cast as timestamp](https://www.rudderstack.com/guides/queries-casting-postgresql/)
- [AGE() function to calculate the difference of timestamps](https://learnsql.com/cookbook/how-to-calculate-the-difference-between-two-timestamps-in-postgresql/)

## Milestones
- [x] Set up the environment.
- [x] Extract and clean the data from the data sources.
- [x] Create the database schema.
- [x] Querying the data.

## Installation

- [Python3](https://www.python.org/downloads/)
- [Pandas] (https://pandas.pydata.org/docs/getting_started/install.html)
    - Run `pip install pandas`
- [boto3] (https://pypi.org/project/boto3/)
    - Run `pip install boto3`
- Create `db_creds.yaml` in the parent directory to have credentials as per the `DatabaseConnector`
  class.

## Usage

1. Run `git clone https://github.com/pchan2/multinational-retail-data-centralisation.git`
1. Run `cd multinational-retail-data-centralisation` if the present directory is not already 
   multinational-retail-data-centralisation.
1. Run `sudo --login --user=postgres` and enter `<password>` to connect to Postgres in the terminal.
1. Run `psql`.
1. Run `\l` to list databases (optional).
1. Run `\c sales_data` to connect to the sales_data database.
1. Run `\dt` to list tables of the database.
1. Run `d orders_table` to see the orders_table table description.

## File structure of the project

**multinational_retail_data_centralisation**  
│  
├── **checks**  
│&emsp;&emsp;├── card_details.ipynb  
│&emsp;&emsp;├── date_times.ipynb  
│&emsp;&emsp;├── legacy_store.ipynb  
│&emsp;&emsp;├── legacy_users.ipynb  
│&emsp;&emsp;├── orders_table.ipynb  
│&emsp;&emsp;├── products.ipynb  
│&emsp;&emsp;└── store_details.ipynb  
│  
├── **ETL**  
│&emsp;&emsp;├── card_details.ipynb  
│&emsp;&emsp;├── date_times.ipynb  
│&emsp;&emsp;├── legacy_users.ipynb  
│&emsp;&emsp;├── orders_table.ipynb  
│&emsp;&emsp;├── products.ipynb  
│&emsp;&emsp;└── store_details.ipynb  
│  
├── **notes**  
│&emsp;&emsp;└── steps_to_clean_data.ipynb  
│  
├── **queries_to_db**  
│&emsp;&emsp;├── 1_total_no_stores.sql  
│&emsp;&emsp;├── 2_locations_with_most_stores.sql  
│&emsp;&emsp;├── 3_months_with_highest_sales.sql  
│&emsp;&emsp;├── 4_online_vs_offline_sales.sql  
│&emsp;&emsp;├── 5_sales_percentage_by_store_type.sql  
│&emsp;&emsp;├── 6_month_in_year_with_highest_sales.sql  
│&emsp;&emsp;├── 7_staff_headcount.sql  
│&emsp;&emsp;├── 8_german_store_types_with_most_sales.sql  
│&emsp;&emsp;└── 9_sales_lead_time.sql  
│  
├── **sales_data_db_sql**  
│&emsp;&emsp;├── 1_orders_table.sql  
│&emsp;&emsp;├── 2_dim_users.sql  
│&emsp;&emsp;├── 3_dim_store.sql  
│&emsp;&emsp;├── 4_dim_products.sql  
│&emsp;&emsp;├── 5_dim_products.sql  
│&emsp;&emsp;├── 6_dim_date_times.sql  
│&emsp;&emsp;├── 7_dim_cards_details.sql  
│&emsp;&emsp;├── 8_add_pk_to_dim_tables.sql  
│&emsp;&emsp;└── 9_add_fk_to_orders_table.sql  
│  
├── data_cleaning.py  
├── data_extraction.py  
├── data_transforms.py  
├── database_utils.py  
└── README.md  

### Directories
- The *checks* directory is for preliminary checks on individual methods and notes.
- The *ETL* directory is the refactored version of *checks*.
- The *sales_data_db_sql* directory has SQL query statements. 
- The *notes* directory has study notes on data cleaning.

## License

The MIT License (MIT)

Copyright (c) 2023 Patrick Chan

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and 
associated documentation files (the "Software"), to deal in the Software without restriction, 
including without limitation the rights to use, copy, modify, merge, publish, distribute, 
sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is 
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial 
portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT 
NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND 
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, 
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT 
OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.