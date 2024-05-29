# File Created by Aagam Shah

"""
About the Data Set:
The sample data set is sourced from National Ocean and Atomspheric Administration (NOAA). 
Currently, I have acquired the hourly temperature readings of
Dallas (Zip Code: 75001) from Jan 1, 2020 to Jan 1, 2024 (ie. 4 years)

Important Definitions for understanding the dataset

Dry Bulb Temperature
Definition: The dry bulb temperature is the temperature of air measured by a thermometer freely exposed to the air 
            but shielded from radiation and moisture.
Measurement: It is the standard temperature reading you get from a regular thermometer.
Usage: It is commonly referred to simply as "air temperature" and is used in most everyday weather reports.

Wet Bulb Temperature
Definition: The wet bulb temperature is the temperature read by a thermometer covered in a water-soaked cloth (wet bulb) over which air is passed.
Measurement: The wet bulb temperature is lower than the dry bulb temperature due to the cooling effect of evaporation. 
            The extent of this difference depends on the humidity level.
Usage: It is used to estimate the moisture content in the air and is a critical measure for assessing thermal comfort and potential heat stress.

In summary, the dry bulb temperature is the air temperature, while the wet bulb temperature is the lowest temperature 
that can be achieved through evaporative cooling. 
"""

# Importing pandas library for data manipulation and preprocessing
import pandas as pd

# Reading the csv file contents into a pandas DataFrame called "dataset"
weather_data = pd.read_csv("Database/csv/DataSet_from_Jan2024_to_Apr2024.csv")

# Acquiring the revelant data from the dataset into a sub dataset called "required_dataset"
# This dataset contains the Station, Date of Reading(includes time), Hourly Dry Bulb Temperature, and Hourly Wet Bulb Temperature
weather_data = weather_data[["STATION","DATE","HourlyDryBulbTemperature","HourlyWetBulbTemperature"]]

# Renaming DATE and STATION Columns to Date and Station
weather_data.rename(columns={'DATE':'Date', 'STATION':'Station'}, inplace=True)

# FIXME: Slicing the Date series into 2 series called Date and Time
# print(weather_data['Date'].iloc[10])

print(weather_data.head())

