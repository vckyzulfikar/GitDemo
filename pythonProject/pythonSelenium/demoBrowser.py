import time

from selenium import webdriver
#from selenium.webdriver.chrome.service import Service

# Chrome driver service Selenium 160->160 chrome driver
#service_obj = Service("C:\\chromedriver.exe") # using double back slash
#driver = webdriver.Chrome(service=service_obj)

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com")
driver.maximize_window() # Full screen window
print(driver.title) # Print output website title
print(driver.current_url) # Print output website url






time.sleep(2) # Time to close Chrome