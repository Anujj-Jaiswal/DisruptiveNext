# Internship - Phoenixgen Systems

A collection of scripts for automated LinkedIn content extraction, data cleaning, and structured output using web scraping and APIs.

---

## I. **Scripts for Automated Web Interaction and Data Scraping.**

### 1 **LinkedIn Post Content Extraction**
+ Automates the retrieval of specific LinkedIn post content using Selenium.
+ Ensures reliable extraction with exception handling and browser resource cleanup.

### 2 **Bulk Link Scraping and Text Extraction**
+ Reads URLs from a CSV file (`Saved_Items`) and extracts visible text.
+ Utilizes `requests` and `BeautifulSoup` for web scraping with random delays to prevent detection.
+ Saves extracted content in a timestamped Excel file.

### 3 **Outputs**
+ Logs in `scraper.log`.
+ Timestamped Excel file containing extracted data.

---

## II. **Custom Search Execution**

### 1 **LinkedIn Information Extraction with Google Custom Search API (CSE)**
+ Automates LinkedIn-related information extraction using the Google Custom Search API.

### 2 **API Key & CSE ID Management**
+ Dynamically rotates API keys and CSE IDs for uninterrupted processing.

### 3 **LinkedIn-specific queries**
+ Constructs LinkedIn-specific queries using names, companies, and positions from an input CSV (`Connections`).

### 4 **Data Structuring**
+ Extracts profile links, descriptions, and snippets.
+ Saves results in `Connections-Extract`.

### 5 **Outputs**
+ Consolidated CSV file containing structured LinkedIn profile data.

---

## III. **Data Cleanup**

### 1 **Text Cleaning**
+ Removes system messages, predefined keywords, and repetitive patterns from LinkedIn post data stored in an Excel file (`LinkedinPosts`).

### 2 **Hashtag Extraction**
+ Identifies hashtags using regular expressions.

### 3 **Data Structuring**
+ Organizes data into columns like:
  - **Author Name**
  - **Designation**
  - **Hashtags**
  - **Processed Post**

### 4 **Outputs**
+ A structured Excel file containing cleaned and processed data.

---
