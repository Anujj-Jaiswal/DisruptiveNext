# Automated Web Interaction and Data Scraping Scripts

This project includes two scripts designed to efficiently extract and process web content.

---

## 1. **LinkedIn Post Content Extraction**

### **Purpose**  
Automates the retrieval of content from a specific LinkedIn post.

### **Key Features**
+ Uses `Selenium WebDriver` with `ChromeDriver` for browser automation.  
+ Locates and extracts the desired element by its class name.  
+ Implements robust exception handling for reliability.  
+ Ensures the browser is properly closed after execution to free resources.  

---

## 2. **Bulk Link Scraping and Text Extraction**

### **Purpose**  
Reads saved URLs from a CSV file and extracts visible text from each link.

### **Key Features**  
+ Reads a list of links from the `Saved_Items2.csv` file.  
+ Uses the `requests` library to fetch HTML content and `BeautifulSoup` for parsing.  
+ Logs activities and errors to track script execution and handle failures gracefully.  
+ Introduces random delays between requests to prevent bot detection.  
+ Saves extracted text alongside corresponding links into an Excel file, named with a timestamp for easy tracking.  

---

## **Logging and Outputs**  

### **Logs**
+ All activities and errors are recorded in `scraper.log`, located in the working directory.  

### **Output**
+ Extracted data is saved as a timestamped Excel file in the working directory.  

---

## **Prerequisites**  

Ensure the following libraries are installed:  
+ `selenium`  
+ `beautifulsoup4` (`bs4`)  
+ `pandas`  
+ `requests`  
+ `webdriver-manager`  
+ `openpyxl` (for Excel file generation)  

---

