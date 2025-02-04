from googleapiclient.discovery import build
import pprint
import pandas as pd
import pickle
import os

 #API key 
my_api_key = "AIzaSyBt5wEowltHsfDpfmeXLzMsdMQl08ReDPs"
my_cse_id = "15f27f470cee94a60"

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']


# Set the directory containing the CSV files
indirectory = r"C:\myfiles\Internship\2.Connections"
outdirectory = r"C:\myfiles\Internship\2.Connections"
filename = "Connections2"

output_file = "Connections-Extract"

outpd = pd.DataFrame()

df = pd.read_csv(os.path.join(indirectory, filename + '.csv'))

# Define the range of rows to process
start_row = 1
end_row = 5

# Update column names if necessary
first_name_column = "First Name"
last_name_column = "Last Name"
company_column = "Company"
position_column = "Position"

for index, row in df.iloc[start_row:end_row].iterrows():
    try:
        search_query = (
            "site:linkedin.com \""
            + row[first_name_column]
            + " "
            + row[last_name_column]
            + "\""
            + " AND \""
            + row[company_column]
            + "\""
            + " AND \""
            + row[position_column]
            + "\""
        )
        print(search_query)
        results = google_search(search_query, my_api_key, my_cse_id, num=1)

        if len(results) > 0:
            result = results[0]
            link = result.get("link")
            image = result.get("pagemap", {}).get("cse_image", [{}])[0].get("src", "")
            thumbnail = result.get("pagemap", {}).get("cse_thumbnail", [{}])[0].get("src", "")
            description = result.get("pagemap", {}).get("metatags", [{}])[0].get("og:description", "")
            twitter = result.get("pagemap", {}).get("metatags", [{}])[0].get("twitter:title", "")
            twitter_description = result.get("pagemap", {}).get("metatags", [{}])[0].get("twitter:description", "")
            twitter_image = result.get("pagemap", {}).get("metatags", [{}])[0].get("twitter:image", "")
            snippet = result.get("snippet", "")
            title = result.get("title", "")

            new_row = {
                "First Name": row[first_name_column],
                "Last Name": row[last_name_column],
                "Company": row[company_column],
                "Position": row[position_column],
                "Connected On": row["Connected On"],
                "Link": link,
                "Image": image,
                "Thumbnail": thumbnail,
                "Description": description,
                "Twitter": twitter,
                "Twitter Description": twitter_description,
                "Twitter Image": twitter_image,
                "Snippet": snippet,
                "Snippet Title": title,
            }

            outpd = pd.concat([outpd, pd.DataFrame([new_row])], ignore_index=True)

    except Exception as e:
        print(str(e))

outpd.to_csv(os.path.join(outdirectory, output_file + '.csv'), index=False)
