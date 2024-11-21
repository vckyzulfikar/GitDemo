import time
from tabnanny import check

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

# Checkbox
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
#print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option1":
        checkbox.click()
        assert checkbox.is_selected()
        #checkbox1 = driver.find_element(By.XPATH, "//input[@type='checkbox']").get_attribute("value")
        #print("Checkbox is "+checkbox1) # To check choosen checkbox

        break

# Radio Button
radiobuttons = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
radiobuttons[2].click()
assert radiobuttons[2].is_selected()

# Hide and Show field
assert driver.find_element(By.ID, "displayed-text").is_displayed() # Make sure field is displayed
driver.find_element(By.ID, "hide-textbox").click()
assert not driver.find_element(By.ID, "displayed-text").is_displayed() # Assert now is make sure field not displayed


time.sleep(5)