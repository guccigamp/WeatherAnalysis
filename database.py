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

# Environmental Variables:
DALLAS_DATASET_CSV = "Database/csv/Texas/DataSet_from_Jan_1_2020_to_Jan_1_2024.csv"
ARIZONA_STATION_METADATA_CSV = "Database/csv/Arizona/station_metadata.csv"
ARIZONA_DB_URL = "sqlite:///Database/db/arizona.db"

# Reading the Arizona selected WBAN Stations Metadata into a pandas DataFrame
df = pd.read_csv(ARIZONA_STATION_METADATA_CSV, encoding='cp1252', delimiter="	")

# Created an engine with sqlite driver and the local sqlite file stored in Database Directory
engine = create_engine(ARIZONA_DB_URL)

# Created an instance of Metadata object
metadata = MetaData()

# Established a connection with the database
connection = engine.connect()

# Creating a Table called Station Metadata using pd.to_sql()
# If exists, then replace
df.to_sql('Station Metadata', connection, if_exists="replace", index=False)


# TODO-Arizona: Create a table to Metadata
# TODO-Arizona: Before uploading all the datasets separately, merge all of them into one csv
# TODO-Arizona: Slice the datatime column into date and time column
# TODO-Arizona: Create a new column called Year
# TODO-Arizona: Index by Station Name, Co-ordinates, Station ID, Year
