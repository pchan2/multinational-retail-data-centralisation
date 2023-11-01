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


## Milestones
- [x] Set up the environment.
- [x] Extract and clean the data from the data sources.
- [ ] Create the dataase schema.
- [ ] Querying the data.

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
│$\qquad$├── card_details.ipynb  
│$\qquad$├── date_times.ipynb  
│$\qquad$├── legacy_store.ipynb  
│$\qquad$├── legacy_users.ipynb  
│$\qquad$├── orders_table.ipynb  
│$\qquad$├── products.ipynb  
│$\qquad$└── store_details.ipynb  
│  
├── **ETL**  
│$\qquad$├── card_details.ipynb  
│$\qquad$├── date_times.ipynb  
│$\qquad$├── legacy_users.ipynb  
│$\qquad$├── orders_table.ipynb  
│$\qquad$├── products.ipynb  
│$\qquad$└── store_details.ipynb  
│  
├── **notes**  
│$\qquad$└── steps_to_clean_data.ipynb  
│  
├── **sales_data_db_sql**  
│$\qquad$├── 1_orders_table.sql  
│$\qquad$├── 2_dim_users.sql  
│$\qquad$├── 3_dim_store.sql  
│$\qquad$├── 4_dim_products.sql  
│$\qquad$├── 5_dim_products.sql  
│$\qquad$├── 6_dim_date_times.sql  
│$\qquad$├── 7_dim_cards_details.sql  
│$\qquad$├── 8_add_pk_to_dim_tables.sql  
│$\qquad$└── 9_add_fk_to_orders_table.sql  
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

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.