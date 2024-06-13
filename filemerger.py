# File created by Aagam Shah

import os
import pandas as pd

# Empty list that will be populated with the datasets
all_dfs = []

# Loops through the files in the Datasets directory
for file in os.listdir("Database/csv/Arizona/datasets"):

    # Executes only the .csv files
    if(file.endswith('.csv')):

        # Creates a new DataFrame with STATION, DATE, Hourly Dry Bulb Temperature, and Hourly Wet Bulb Temperature 
        new_df = pd.read_csv(f'Database/csv/Arizona/datasets/{file}', usecols=['STATION', 'DATE', 'HourlyDryBulbTemperature', 'HourlyWetBulbTemperature'])
        
        # Appends the new DataFrame in the list
        all_dfs.append(new_df)

        # Deletes the new DataFrame from the memory
        del new_df

# Created a DataFrame that contains all the DataFrames 
master_df = pd.concat(all_dfs)

# Converts the DataFrame to a csv file
master_df.to_csv("Master_Dataset.csv", index=False)
