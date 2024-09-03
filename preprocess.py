import os
import pandas as pd

# Define the folder containing the CSV files
folder_path = 'results/diff_tech_analysis/'

# Initialize an empty list to store DataFrames
dfs = []

# Loop through each file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        # Extract the value for the 'exp' column from the filename
        exp_value = filename.split('output_')[1].rsplit('_', 1)[0]
        
        # Read the CSV file into a DataFrame
        df = pd.read_csv(os.path.join(folder_path, filename))
        
        # Add the 'exp' column to the DataFrame
        df['exp'] = exp_value
        
        # Append the DataFrame to the list
        dfs.append(df)

# Concatenate all DataFrames into a single DataFrame
combined_df = pd.concat(dfs, ignore_index=True)

# Display the combined DataFrame
print(combined_df)

combined_df.to_csv('preprocessed_data.csv', index=False)

# Display the combined DataFrame (optional)
print(combined_df)