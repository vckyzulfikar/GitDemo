import time
from time import process_time_ns

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v127.fed_cm import click_dialog_button
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

expectedList = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
actualList = []

service_obj = Service("C:\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
# 5 seconds is max time out.. 2 seconds (3 seconds save)
driver.implicitly_wait(5)

driver.find_element(By.XPATH, "//input[@type='search']").send_keys("ber")
time.sleep(2)

# Add to Cart
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(results) # Calculate the value of products shown by "ber"
assert count > 0 # To make sure that count is more then 0
for result in results:
    actualList.append(result.find_element(By.XPATH, "h4").text) # Append to add item to list
    result.find_element(By.XPATH, "div/button").click() # Call result to add value

assert expectedList == actualList

# Cart then button Proceed To Checkout
driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

# SUM Validation
prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
sum = 0 # First declare sum is 0
for price in prices:
    sum = sum + int(price.text) # sum from all price from price.text

print("Total Amount is ",sum)
totalAmount = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text) # Convert to integer
assert sum == totalAmount

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
promoInfo = driver.find_element(By.CLASS_NAME, "promoInfo").text
print(promoInfo)
assert "Code applied ..!" in promoInfo

# Checking the discound should bigger than total amount
discountedAmount = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text) # float since output is decimal
assert totalAmount > discountedAmount
print(discountedAmount)



time.sleep(5)