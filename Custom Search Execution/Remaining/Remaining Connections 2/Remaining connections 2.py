import pandas as pd
import os

def compare_and_generate_remaining(source_file, output_file, remaining_file):
    source_data = pd.read_csv(source_file)
    output_data = pd.read_csv(output_file)
    
    # Select the relevant columns for comparison
    source_columns = ['First Name', 'Last Name', 'Company', 'Position', 'Connected On']
    output_columns = ['First Name', 'Last Name', 'Company', 'Position', 'Connected On']
    
    remaining_data = pd.merge(source_data[source_columns], output_data[output_columns], how='left', indicator=True)
    remaining_data = remaining_data[remaining_data['_merge'] == 'left_only'].drop(columns=['_merge'])
    
    remaining_data.to_csv(remaining_file, index=False)

if __name__ == "__main__":
    source_directory = r"C:\myprogs\Internship\Task 2\Remaining\Remaining Connections 2"
    source_file = os.path.join(source_directory, "Connections2.csv")
    output_file = os.path.join(source_directory, "Connections2op.csv")
    remaining_file = os.path.join(source_directory, "Remaining.csv")
    
    compare_and_generate_remaining(source_file, output_file, remaining_file)
    print("Remaining data has been generated in Remaining.csv")
