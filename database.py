# File created by Aagam Shah
# This file's purpose is to interact with the sqlite database.
"""
Definitions: 
1. Metadata: a container object that keeps together many different 
          features of a database (or multiple databases) being described
"""

from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import (Table, Column, String, Integer, Float)
import pandas as pd

# Environment Variables:
DALLAS_DATASET_CSV = "Database/csv/Texas/DataSet_from_Jan_1_2020_to_Jan_1_2024.csv"
ARIZONA_STATION_METADATA_CSV = "Database/csv/Arizona/station_metadata.csv"
ARIZONA_DB_URL = "sqlite:///Database/db/arizona.db"
ARIZONA_DB_CSV = "Database/csv/Arizona/Arizona.csv"

# Reading the metadata csv file
metadata_df = pd.read_csv(ARIZONA_STATION_METADATA_CSV, dtype={'WBAN ID': 'string', 'Station Name': 'string'})

# Reading the master dataset csv file
master_df = pd.read_csv(ARIZONA_DB_CSV, dtype={'WBAN ID': 'string', 'Station Name': 'string', 'Hourly Wet Bulb Temperature': 'float64', 'Year': 'int64'})

# Created an engine with sqlite driver and the local sqlite file stored in Database Directory
engine = create_engine(ARIZONA_DB_URL)

# Created an instance of Metadata object
metadata = MetaData()

# Established a connection with the database
connection = engine.connect()

# Creating a Table called Station Metadata using pd.to_sql()
# If exists, then replace
metadata_df.to_sql('Station Metadata', connection, if_exists="replace", index=False)

# Creating a Table called Dataset using pd.to_sql()
# If exists, then replace
master_df.to_sql('Dataset of Last 3 years', connection, if_exists="replace", index=False)



# TODO-Arizona: Spliting the datatime column into date and time column
# TODO-Arizona: Create a new column called Year
# TODO-Arizona: Index by Station Name, Co-ordinates, Station ID, Year
