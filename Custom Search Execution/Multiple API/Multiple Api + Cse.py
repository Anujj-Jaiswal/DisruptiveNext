from googleapiclient.discovery import build
import pandas as pd
import os


indirectory = r"C:\myfiles\Internship\2.Connections\Multiple API"
outdirectory = r"C:\myfiles\Internship\2.Connections\Multiple API"
filename = "Connections1"
output_file = "Connections-Extract"

# Loading API keys and CSE IDs from Excel
api_keys_df = pd.read_excel(os.path.join(indirectory, "MultipleApi.xlsx"))
api_keys = api_keys_df["API Key"].tolist()

cse_ids_df = pd.read_excel(os.path.join(indirectory, "CseId.xlsx"))
cse_ids = cse_ids_df["CSE id"].tolist()

# Initializing index variables for API keys and CSE IDs
current_api_key_index = 0
current_cse_id_index = 0

def get_current_api_key():
    return api_keys[current_api_key_index]

def update_current_api_key():
    global current_api_key_index
    current_api_key_index = (current_api_key_index + 1) % len(api_keys)

def get_current_cse_id():
    return cse_ids[current_cse_id_index]

def update_current_cse_id():
    global current_cse_id_index
    current_cse_id_index = (current_cse_id_index + 1) % len(cse_ids)

def google_search_with_retry(search_term, max_retries=3, **kwargs):
    for _ in range(max_retries):
        try:
            api_key = get_current_api_key()
            cse_id = get_current_cse_id()
            service = build("customsearch", "v1", developerKey=api_key)
            res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
            return res.get('items', [])
        except Exception as e:
            print(f"Error with API key {api_key} and CSE ID {cse_id}: {str(e)}")
            update_current_api_key()
            update_current_cse_id()
    return []

# Loading the CSV file
df = pd.read_csv(os.path.join(indirectory, filename + '.csv'))

# Defining the range 
start_row = 2
end_row = 10

# Defining column names
first_name_column = "First Name"
last_name_column = "Last Name"
company_column = "Company"
position_column = "Position"

#Empty DataFrame to store results
result_dfs = []

# Loop through rows to search and collect data
for index, row in df.iloc[start_row:end_row].iterrows():
    try:
        search_query = (
            f"site:linkedin.com \"{row[first_name_column]} {row[last_name_column]}\""
            f" AND \"{row[company_column]}\""
            f" AND \"{row[position_column]}\""
        )
        print(search_query)
        results = google_search_with_retry(search_query, num=1)

        if results:
            result = results[0]
            link = result.get("link", "")
            description = result.get("pagemap", {}).get("metatags", [{}])[0].get("og:description", "")
            snippet = result.get("snippet", "")
            title = result.get("title", "")

            new_row = {
                "First Name": row[first_name_column],
                "Last Name": row[last_name_column],
                "Company": row[company_column],
                "Position": row[position_column],
                "Connected On": row["Connected On"],
                "Link": link,
                "Image": "", 
                "Thmbnail": "",  
                "Description": description,
                "Twitter": "",  
                "Twitter Description": "",  
                "Twitter Image": "",  
                "Snippet": snippet,
                "Snippet Title": title,
            }

            result_df = pd.DataFrame([new_row])
            result_dfs.append(result_df) 

    except Exception as e:
        print(f"Error processing row {index+1}: {str(e)}")

# Concatenate all result DataFrames into one DataFrame
outpd = pd.concat(result_dfs, ignore_index=True)

# Save the results to CSV
output_path = os.path.join(outdirectory, output_file + '.csv')
outpd.to_csv(output_path, index=False)
print(f"Results saved to {output_path}")
