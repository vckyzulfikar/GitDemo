import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v127.fed_cm import click_dialog_button

service_obj = Service("C:\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
# 5 seconds is max time out.. 2 seconds (3 seconds save)
driver.implicitly_wait(5)

driver.find_element(By.XPATH, "//input[@type='search']").send_keys("ber")
time.sleep(2)
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(results) # Calculate the value of products shown by "ber"
assert count > 0 # To make sure that count is more then 0
for result in results:
    result.find_element(By.XPATH, "div/button").click() # Call result to add value

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

print(driver.find_element(By.CLASS_NAME, "promoInfo").text)




time.sleep(5)