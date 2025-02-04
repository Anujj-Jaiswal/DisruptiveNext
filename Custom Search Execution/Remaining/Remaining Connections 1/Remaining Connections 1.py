import pandas as pd
import os

def compare_and_generate_remaining(source_file, output_file, remaining_file):
    source_data = pd.read_csv(source_file)
    output_data = pd.read_csv(output_file)
    
    # Select the relevant columns for comparison
    source_columns = ['First Name', 'Last Name', 'Email Address', 'Company', 'Position', 'Connected On']
    output_columns = ['First Name', 'Last Name', 'Company', 'Position', 'Link', 'Image', 'Thumbnail', 'Description', 'Twitter', 'Twitter Description', 'Twitter Image', 'Snippet', 'Title']
    
    remaining_data = pd.merge(source_data[source_columns], output_data[output_columns], how='left', indicator=True)
    remaining_data = remaining_data[remaining_data['_merge'] == 'left_only'].drop(columns=['_merge'])
    
    remaining_data.to_csv(remaining_file, index=False)

if __name__ == "__main__":
    source_directory = r"C:\myprogs\Internship\Task 2\Remaining\Remaining Connections 1"
    source_file = os.path.join(source_directory, "Connections1.csv")
    output_file = os.path.join(source_directory, "Connections1op.csv")
    remaining_file = os.path.join(source_directory, "Remaining.csv")
    
    compare_and_generate_remaining(source_file, output_file, remaining_file)
    print("Remaining data has been generated in Remaining.csv")
