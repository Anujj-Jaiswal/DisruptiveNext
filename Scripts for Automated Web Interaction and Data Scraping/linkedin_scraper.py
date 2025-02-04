from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Setup ChromeDriver using WebDriverManager for automated installation
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Target LinkedIn post URL
    url = "https://www.linkedin.com/feed/update/urn:li:activity:7062682833596637184/"
    driver.get(url)

    # Attempt to locate and extract content from an element with the class name 'main'
    element = driver.find_element(By.CLASS_NAME, "main")  # Update 'main' class name if necessary
    data = element.text

    # Print the extracted data (content of the located element)
    print(data)

except Exception as e:
    # Handle and display errors if the script encounters an issue
    print(f"An error occurred: {e}")

finally:
    # Ensure the browser is closed after execution
    driver.quit()
