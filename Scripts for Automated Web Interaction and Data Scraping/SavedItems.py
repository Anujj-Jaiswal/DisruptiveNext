import os
import pandas as pd
import time
import requests
from bs4 import BeautifulSoup
import logging
import random


current_dir = r"C:\\myfiles\\Internship\\1.SavedItems"
os.chdir(current_dir)

# Configured logging to track script activities and errors
logging.basicConfig(
    filename=os.path.join(current_dir, 'scraper.log'),
    filemode='a',
    format='%(name)s - %(levelname)s - %(message)s'
)


csv_file = "Saved_Items2.csv"
df = pd.read_csv(os.path.join(current_dir, csv_file))

# Limiting data to relevant rows for processing
df = df.iloc[1:5]

# Extracting the 'savedItem' column as a list of links
links = df["savedItem"].tolist()
texts = []  # To store the extracted text from each link

# Iterate through links to fetch and parse their content
for link in links:
    try:
        # Send an HTTP GET request to the current link
        response = requests.get(link)
        logging.info(f"Processing link: {link}")  # Log the link being processed
        
        # Check for HTTP errors
        response.raise_for_status()
        
        # Parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")
        texts.append(soup.get_text())  # Extract the visible text
        
        # Introduce a random delay to avoid being flagged as a bot
        time.sleep(random.randint(5, 15))
    except requests.exceptions.RequestException as e:
        # Log HTTP-related errors and continue processing the next link
        logging.error(f"Request error for link: {link} - {str(e)}")
        texts.append("")  # Append empty text to maintain list length
    except Exception as e:
        # Log any unexpected errors and continue processing
        logging.exception(f"Error processing link: {link}")
        texts.append("")  # Append empty text to maintain list length

# Verify if the lengths of links and texts are consistent
if len(links) != len(texts):
    logging.warning("Mismatch detected: Number of links and texts do not match.")

# Create a DataFrame with the original links and extracted text
output_df = pd.DataFrame({"Link": links, "Text": texts})

# Generate a timestamp for the output file
now = time.strftime("%Y-%m-%d-%H-%M-%S")

# Save the extracted data to a new Excel file
output_file = os.path.join(current_dir, f"{now}.xlsx")
output_df.to_excel(output_file, index=False)

# Notify completion in logs
logging.info(f"Data successfully saved to {output_file}")
