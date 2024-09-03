import os
import pandas as pd

# Folder path where your CSV files are located
folder_path = './results/'

# List to hold DataFrames
df_list = []


# Loop through the files in the folder
for filename in os.listdir(folder_path):
    
    if filename.endswith('.csv'):
        file_path = os.path.join(folder_path, filename)
        # Read the CSV file
        df = pd.read_csv(file_path)
        if 'gpu' in filename:
            df['device'] = 'gpu'
        else:
            df['device'] = 'sc'
        # Append the DataFrame to the list
        df_list.append(df)

# Concatenate all DataFrames in the list
combined_df = pd.concat(df_list, ignore_index=True)

# Display the combined DataFrame
print(combined_df)

combined_df.to_csv('Processor_Count_Analysis.csv')
