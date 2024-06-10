from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up the WebDriver (here we use Chrome)
driver = webdriver.Chrome()

x = 0
try:
    # Open the main blog page
    driver.get('https://stem4impact.wixsite.com/society/blog')
    time.sleep(3)  # Wait for the page to load
    
    while x < 25:
        # Navigate to the specific article
        article_url = 'https://stem4impact.wixsite.com/society/post/ethical-issues-of-ai-powered-hiring-lessons-from-amazon-s-biased-recruiting-tool'
        driver.get(article_url)
        time.sleep(5)  # Wait for the article to load
        
        # Go back to the main blog page
        driver.back()
        time.sleep(1)  # Wait for the page to load before repeating the process
        x+=1

finally:
    # Close the WebDriver
    driver.quit()
