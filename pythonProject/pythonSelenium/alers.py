import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
name = "Rahul"

# Alert button
driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
driver.find_element(By.ID, "alertbtn").click()
alert = driver.switch_to.alert # Get alert notification
alertText = alert.text # Get value alert
print(alertText) # Output alert
assert name in alertText
alert.accept() # To confirm the alert
#alert.dismiss()


time.sleep(5)