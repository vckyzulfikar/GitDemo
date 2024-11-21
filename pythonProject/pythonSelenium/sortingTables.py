import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)

browserSortedVeggies = [] # List empty Array

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.maximize_window()

# Click on column header
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()

# Collect all veggie names -> BrowserSortedveggieList ( A,B,C )
veggieWebElements = driver.find_elements(By.XPATH, "//tr//td[1]")
for ele in veggieWebElements:
    browserSortedVeggies.append(ele.text)

originalBrowserSortedList = browserSortedVeggies.copy() # To create another copy of the list

# Sort this veggieList => newSortedList -> (A,B,C)
browserSortedVeggies.sort()
assert browserSortedVeggies == originalBrowserSortedList
print(browserSortedVeggies)



time.sleep(5)