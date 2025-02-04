import os
import pandas as pd

# Set the directory paths
excel_directory = r"C:\myprogs\Internship\1.SavedItems\Remaining"
csv_directory = r"C:\myprogs\Internship\1.SavedItems\Remaining"

# Read the generated output file "mergeunique.xlsx"
output_file_path = os.path.join(excel_directory, "Merged.xlsx")
df_output = pd.read_excel(output_file_path)

# Read the "Saved_Items.csv" file
csv_file_path = os.path.join(csv_directory, "Saved_Item 2.csv")
df_csv = pd.read_csv(csv_file_path)

# Find the links present in "Saved_Items.csv" but not in "mergeunique.xlsx"
remaining_links = df_csv[~df_csv['savedItem'].isin(df_output['Link'])]

# Create a DataFrame with the remaining links
df_remaining = pd.DataFrame(remaining_links, columns=['savedItem'])

# Write the remaining links to a new Excel file named "Remaining.xlsx"
remaining_file_path = os.path.join(csv_directory, "Remaining.xlsx")
df_remaining.to_excel(remaining_file_path, index=False)