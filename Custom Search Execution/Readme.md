# Automated LinkedIn Information Extraction using Google Custom Search API (CSE)

This script automates the process of searching and extracting LinkedIn-related information using Google Custom Search API (CSE). It dynamically rotates through multiple API keys and CSE IDs to ensure uninterrupted operation. Extracted data includes key details for specified individuals, which are saved into a structured CSV file.

---

## **Key Functionalities**

### **1. API Key and CSE ID Management**
+ Loads a list of API keys and CSE IDs from Excel files  
+ Automatically rotates through keys and IDs after each request or upon encountering an error, ensuring uninterrupted functionality.  

### **2. Custom Search Execution**
+ Uses the `googleapiclient.discovery` module to interact with Google’s Custom Search API (CSE).  
+ Dynamically constructs a query for LinkedIn profiles using a combination of:
  - **First Name**
  - **Last Name**
  - **Company**
  - **Position**  
+ Implements retry logic to handle transient API or network failures, enhancing robustness.  

### **3. Data Processing and Structuring**
+ Reads input data from a CSV file (`Connections), including:
  - Names
  - Company
  - Positions  
+ Executes Google searches for LinkedIn profiles and extracts key information, such as:
  - **Profile Link**
  - **Description**
  - **Title and Snippet (Summary Text)**  
+ Appends the extracted data alongside original input columns into a structured format.

### **4. Output Generation**
+ Combines all search results into a consolidated DataFrame.  
+ Saves the processed data as a CSV file (`Connections-Extract`) in the specified output directory.  

---

## **Logging and Error Handling**
+ Handles and logs API request errors and row-level issues gracefully.  
+ Ensures no data is lost or the process halted, even in cases of:
  - API failures
  - Missing information  

---

## **Prerequisites**  

Ensure the following libraries are installed:  
+ `pandas`  
+ `google-api-python-client`  
+ `openpyxl`  

---

