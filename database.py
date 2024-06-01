# File created by Aagam Shah

"""
This file's purpose is to interact with the sqlite database.
Definitions: 
1. Metadata: a container object that keeps together many different 
          features of a database (or multiple databases) being described
"""

from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import (Table, Column, String, Integer, Float)
import pandas as pd

# Reading the csv file contents into a pandas DataFrame
df = pd.read_csv("Database/csv/DataSet_from_Jan_1_2020_to_Jan_1_2024.csv")


# Created an engine with sqlite driver and the local sqlite file stored in Database Directory
engine = create_engine('sqlite:///Database/db/texas.db')

# Created an instance of Metadata object
metadata = MetaData()

# Established a connection with the database
connection = engine.connect()

# Creating a Table called Dallas using pd.to_sql()
# If exists, then replace
df.to_sql('Dallas', connection, if_exists="replace", index=False)

# TODO: Make a database for each state and make tables for the cities of that state

