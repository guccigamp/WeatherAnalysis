# File created by Aagam Shah

"""
This file's purpose is to interact with the sqlite database.
Definitions: 
1. Metadata: a container object that keeps together many different 
          features of a database (or multiple databases) being described
"""

from sqlalchemy import create_engine
from sqlalchemy import MetaData
# Importing functions for creating the table
from sqlalchemy import (Table, Column, String, Integer, Float)

# Created an engine with sqlite driver and the local sqlite file stored in Database Directory
engine = create_engine('sqlite:///Database/db/texas.db')

# Created an instance of Metadata object
metadata = MetaData()

# Established a connection with the database
connection = engine.connect()

# Creating a Table called Dallas and adding columns to it
# Data gets appended in the metadata
dallas = Table('Dallas', metadata,
               Column('Station', Integer()),
               Column('Date', String()),
               Column('Time', String()),
               Column('HourlyDryBulbTemp', Float()),
               Column('HourlyWetBulbTemp', Float())
               )

# Creates the table in the actual database by using the create_all() method to the metadata
metadata.create_all(engine)

# TODO: Make a database for each state and make tables for the cities of that state
# TODO: Load the CSV file into the SQLite Database
# FIXME: DO NOT FILTER OUT THE IRRELEVANT COLUMNS YET
