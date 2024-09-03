import csv
import os

# Function to check if a string is numeric
def is_numeric(value):
    return value.isdigit()

# Open the file and read its contents
with open('log.txt', 'r') as file:
    lines = file.readlines()

# Initialize a set to store new MKN values
new_mkn = set()

# Iterate over each line in the file
for line in lines:
    # Check if the line starts with "M,K,N"
    if line.startswith("M,K,N"):
        # Strip any extra whitespace and split the line by spaces
        parts = line.strip().split()
        
        # Debug print to verify splitting
        print(f"Raw parts: {parts}")

        # Skip lines with more than 4 parts
        if len(parts) != 4:
            continue
        
        # Ensure parts[1], parts[2], and parts[3] are numeric
        if all(is_numeric(part) for part in parts[1:]):
            # Create a tuple of M, K, N values
            mkn_tuple = (parts[1], parts[2], parts[3])
            # Add the tuple to the set of new MKN values
            new_mkn.add(mkn_tuple)

# Define the CSV file path
csv_file_path = 'unique_mkn.csv'

# Initialize header and existing_mkn
header = ['m', 'k', 'n']
existing_mkn = set()

# Read existing MKN values if the file exists
if os.path.exists(csv_file_path):
    with open(csv_file_path, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        try:
            header = next(csvreader)
            existing_mkn = set(tuple(row) for row in csvreader if row)
        except StopIteration:
            # Handle the case where the file is empty
            pass

# Write only new MKN values to avoid duplicates
with open(csv_file_path, 'a', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    # Write the header row only if the file did not exist before
    if not os.path.exists(csv_file_path) or os.path.getsize(csv_file_path) == 0:
        csvwriter.writerow(header)
    # Write new MKN values that are not already in the file
    csvwriter.writerows(new_mkn - existing_mkn)

print("Unique MKN values have been appended to 'unique_mkn.csv'")
