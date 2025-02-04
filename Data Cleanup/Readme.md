# LinkedIn Post Data Cleaning and Processing Script

This script is designed to clean, process, and extract meaningful insights from LinkedIn post data stored in an Excel file. The processed data, including author details, cleaned post content, and hashtags, is saved into a structured Excel file for easy analysis and reporting.

---

## **Key Functionalities**

### **1. Unstructured Text Processing**
+ Reads LinkedIn post data from an Excel file (`LinkedinPosts`).  
+ Extracts and cleans posts by removing unwanted content, including:
  - System messages
  - Keywords
  - Unwanted languages
  - Repetitive patterns  
+ Identifies and separates the following details from each post:
  - **Author Name**
  - **Designation**
  - **Contextual Details**

### **2. Text Cleaning and Post-Processing**
+ Removes predefined keywords and unnecessary substrings using helper functions.  
+ Eliminates redundant parts based on patterns, such as:
  - Numbers  
  - Common substrings  
  - System-generated text  

### **3. Hashtag Extraction**
+ Detects and retrieves hashtags from each post using regular expressions.  

### **4. Data Structuring**
+ Structures the processed data into the following columns:
  - **Author Name**
  - **Designation**
  - **Hashtags**
  - **Processed Post**  
+ Adds blank rows between processed entries for better readability in the output Excel file.

### **5. Output Generation**
+ Consolidates the cleaned and structured data into an Excel file (`Output`) for further use.  

---

## **Logging and Error Handling**
+ Incorporates custom helper functions to handle text processing errors gracefully.  
+ Skips posts containing unwanted languages or predefined patterns to ensure high data quality.  

---

## **Prerequisites**

Ensure the following libraries are installed:  
+ `pandas`  
+ `openpyxl`  
+ `logging`  
+ `re`  

 
