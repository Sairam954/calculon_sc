import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = './Processor_Count_Analysis.csv'  # Replace with the actual path to your CSV file
data = pd.read_csv(file_path)

# Create the plot
fig, ax = plt.subplots()

# Filter the data based on gpu values
gpu_true = data[data['gpu'] == True]
gpu_false = data[data['gpu'] == False]

# Plot bars for gpu = True
ax.bar(gpu_true['num_procs'], gpu_true['sample_rate'], color='blue', label='GPU = True')

# Plot bars for gpu = False
ax.bar(gpu_false['num_procs'], gpu_false['sample_rate'], color='orange', label='GPU = False')

# Labeling the x-axis, y-axis, and the chart title
ax.set_xlabel('Number of Processes')
ax.set_ylabel('Sample Rate')
ax.set_title('Sample Rate vs Number of Processes with GPU Distinction')

# Adding a legend to differentiate between GPU = True and GPU = False
ax.legend()

# Display the plot
plt.show()
