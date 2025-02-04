import os
import pandas as pd

# Set the directory containing the CSV files
directory = r"C:\myprogs\Internship\2.Connections\Unique"

# Initialize an empty DataFrame to store the unique data entries
unique_data = pd.DataFrame()

# Iterate through all the CSV files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        file_path = os.path.join(directory, filename)
        df = pd.read_csv(file_path)
        unique_data = pd.concat([unique_data, df], ignore_index=True)

# Remove duplicates and repeated data entries
unique_data = unique_data.drop_duplicates()

# Save the unique data to a CSV file named "unique.csv"
output_file = os.path.join(directory, "unique.csv")
unique_data.to_csv(output_file, index=False)
