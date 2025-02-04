import os
import pandas as pd

# Set the directory path where the Excel files are located
directory = r"C:\myprogs\Internship\1.SavedItems\Unique"

# Create an empty DataFrame to store the unique links and texts
unique_data = pd.DataFrame(columns=['Link', 'Text'])

# Iterate over each file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".xlsx"):
        file_path = os.path.join(directory, filename)
        # Read the Excel file
        df = pd.read_excel(file_path)
        
        # Filter out rows with empty Text column
        df = df.dropna(subset=['Text'])
        
        # Find the unique links not present in the unique_data DataFrame
        unique_links = df[~df['Link'].isin(unique_data['Link'])]
        
        # Append the unique links and texts to the unique_data DataFrame
        unique_data = pd.concat([unique_data, unique_links], ignore_index=True)

# Write the unique_data DataFrame to a new Excel file named "mergeunique.xlsx"
output_file = os.path.join(directory, "mergeunique.xlsx")
unique_data.to_excel(output_file, index=False)
