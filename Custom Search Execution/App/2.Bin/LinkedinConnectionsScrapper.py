import os
import pandas as pd
from googleapiclient.discovery import build

# Directory path of the currently executing script
script_directory = os.path.dirname(os.path.abspath(__file__))

# Construct paths relative to the script directory
bin_folder = os.path.join(script_directory, '2.Bin')
indirectory_folder = os.path.join(script_directory, '3.Indirectory')
outdirectory_folder = os.path.join(script_directory, '4.Outdirectory')
extract_folder = os.path.join(outdirectory_folder, '1.Extract')
error_folder = os.path.join(outdirectory_folder, '2.Error')
route_folder = os.path.join(script_directory, '5.Route')

# Loading API keys and CSE IDs
api_keys_df = pd.read_csv(os.path.join(route_folder, 'APIkey.csv'))
api_keys = api_keys_df['API Key'].tolist()

cse_ids_df = pd.read_csv(os.path.join(route_folder, 'CSEid.csv'))
cse_ids = cse_ids_df['CSEid'].tolist()

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

def google_search(search_term, **kwargs):
    api_key = get_current_api_key()
    cse_id = get_current_cse_id()
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res.get('items', [])

# Initializing a set to keep track of processed data
processed_data_set = set()

# Loading existing data from previously processed CSV files
for existing_filename in os.listdir(extract_folder):
    if existing_filename.startswith("Extract-") and existing_filename.endswith(".csv"):
        existing_filepath = os.path.join(extract_folder, existing_filename)
        existing_df = pd.read_csv(existing_filepath)
        processed_data_set.update(
            zip(
                existing_df["First Name"],
                existing_df["Last Name"],
                existing_df["Company"],
                existing_df["Position"],
            )
        )

def process_csv_file(csv_path, output_folder, error_folder, max_retries=1):
    df = pd.read_csv(csv_path)

    columns_to_compare = df.columns.tolist()

    processed_rows = []
    error_rows = []

    for index, row in df.iterrows():
        data_tuple = (row["First Name"], row["Last Name"], row["Company"], row["Position"])

        if data_tuple in processed_data_set:
            print(f"Skipping duplicate data: {data_tuple}")
            continue

        search_query = " AND ".join([f'"{row[col]}"' for col in columns_to_compare])

        retries = 0
        while retries < max_retries:
            try:
                print(f"Processing row Data: {data_tuple}")
                results = google_search(search_query, num=1)

                if results:
                    result = results[0]
                    link = result.get("link", "")
                    description = result.get("pagemap", {}).get("metatags", [{}])[0].get("og:description", "")
                    snippet = result.get("snippet", "")
                    title = result.get("title", "")

                    new_row = {
                        "First Name": row["First Name"],
                        "Last Name": row["Last Name"],
                        "Company": row["Company"],
                        "Position": row["Position"],
                        "Link": link,
                        "Image": "", 
                        "Thumbnail": "",  
                        "Description": description,
                        "Twitter": "",  
                        "Twitter Description": "", 
                        "Twitter Image": "", 
                        "Snippet": snippet,
                        "Snippet Title": title,
                    }

                    processed_rows.append(new_row)
                    processed_data_set.add(data_tuple)
                else:
                    error_rows.append(row)
                break  
            except Exception as e:
                print(f"An error occurred: {e}")
                retries += 1
                if retries < max_retries:
                    print(f"Retrying ({retries}/{max_retries})...")
                else:
                    print(f"Max retries reached for {data_tuple}. Moving to the next.")

    # Save processed rows to Extract csv
    if processed_rows:
        processed_df = pd.DataFrame(processed_rows)
        processed_filename = os.path.join(output_folder, f"Extract-{pd.Timestamp.now():%d-%m-%y-%H-%M}.csv")
        processed_df.to_csv(processed_filename, index=False)

    # Save error rows to Error csv
    if error_rows:
        error_df = pd.DataFrame(error_rows)
        error_filename = os.path.join(error_folder, f"Error-{pd.Timestamp.now():%d-%m-%y-%H-%M}.csv")
        error_df.to_csv(error_filename, index=False)

# Process csv files in the Indirectory
for filename in os.listdir(indirectory_folder):
    if filename.endswith(".csv"):
        csv_path = os.path.join(indirectory_folder, filename)
        process_csv_file(csv_path, extract_folder, error_folder, max_retries=1)