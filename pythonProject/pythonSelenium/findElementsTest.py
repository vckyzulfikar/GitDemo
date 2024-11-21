import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()

# Dynamic Dropdown
driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(2)
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a") # find_elements with s
#print(len(countries)) # To check all list dropdown

for country in countries:
    if country.text == "Indonesia":
        country.click()
        break

#print(driver.find_element(By.ID, "autosuggest").text)
dropdownCountry = driver.find_element(By.ID, "autosuggest").get_attribute("value")
print("Country is "+dropdownCountry) # Checking dropdown choosen
#assert driver.find_element(By.ID, "autosuggest").get_attribute("value")


time.sleep(5)