import pandas as pd
import os

data = { #dictionary
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24,30,45],
    'City':['NewYork', 'LosAngeles', 'Chicago']
}

df = pd.DataFrame(data) #dictionary to dataframe


# Adding a new row to df for version2
# new_row_loc = {'Name': 'V2', 'Age':20, 'City':'city1'}
# df.loc[len(df.index)] = new_row_loc

# Adding new row to df for version3
# new_row_loc2 = {'Name': 'V3', 'Age':30, 'City':'city2'}
# df.loc[len(df.index)] = new_row_loc

# Ensure the data directory exists at the root level
data_dir = 'data' #create a directory named data
os.makedirs(data_dir,exist_ok=True) #creates the directory, wont overwrite if exists

# Define the file path
file_path = os.path.join(data_dir, 'sample_data.csv') #path defined for new file to be saved

# Save the Dataframe to a csv file, including column names
df.to_csv(file_path, index=False) #saved to path 

print(f"CSV file saved to {file_path}")
