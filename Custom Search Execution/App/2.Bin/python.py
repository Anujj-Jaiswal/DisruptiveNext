import os
import pandas as pd
import requests
from bs4 import BeautifulSoup
from googleapiclient.discovery import build


API_KEY = 'AIzaSyBt5wEowltHsfDpfmeXLzMsdMQl08ReDPs'
CSE_ID = '15f27f470cee94a60'


input_directory = r'C:\myprogs\Internship\2.Connections\App\3.Indirectory'
output_directory = r'C:\myprogs\Internship\2.Connections\App\4.Outdirectory'

# Function to perform a Google search and extract results excluding LinkedIn
def google_search(query):
    service = build("customsearch", "v1", developerKey=API_KEY)
    result = service.cse().list(q=query, cx=CSE_ID, excludeTerms="linkedin.com").execute()
    return result.get("items", [])

# Function to scrape data from a URL
def scrape_data(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        extracted_text = soup.get_text()  
        return extracted_text
    except Exception as e:
        return str(e)


from datetime import datetime
now = datetime.now()
timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
output_filename = f"extract_{timestamp}.xlsx"

# Reading the CSV file
csv_file_path = os.path.join(input_directory, 'sample.csv')
df = pd.read_csv(csv_file_path, encoding='utf-8')

# DataFrame for the output Excel file
output_df = df.copy()

# Range
for i in range(1, 5):
    output_df[f'url {i}'] = ""
    output_df[f'extract text {i}'] = ""

# Loop through the rows of the CSV file and perform web scraping
for index, row in df.iterrows():
    query = f"{row['First Name']} {row['Last Name']} {row['Email Address']} {row['Company']} {row['Position']}"
    search_results = google_search(query)
    result_count = min(len(search_results), 4)  
    for i in range(result_count):
        url = search_results[i]['link']
        extracted_text = scrape_data(url)
        output_df.at[index, f'url {i+1}'] = url
        output_df.at[index, f'extract text {i+1}'] = extracted_text

# Save the DataFrame to an Excel file
output_file_path = os.path.join(output_directory, output_filename)
output_df.to_excel(output_file_path, index=False, engine='openpyxl')
print(f"Data saved to {output_file_path}")
