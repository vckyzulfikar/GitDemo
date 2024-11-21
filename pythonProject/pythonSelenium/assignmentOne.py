import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, ".blinkingText").click()
windowsOpened = driver.window_handles

driver.switch_to.window(windowsOpened[1])
print(driver.find_element(By.LINK_TEXT, "mentor@rahulshettyacademy.com").text)
driver.close()
driver.switch_to.window(windowsOpened[0])
assert "Username:" == driver.find_element(By.TAG_NAME, "label").text

# Login
driver.find_element(By.ID, "username").send_keys("contact@rahulshettyacademy.com")
driver.find_element(By.ID, "password").send_keys("12345")
driver.find_element(By.XPATH, "//input[@type='submit']").click()

alert = driver.find_element(By.XPATH, "//div[@style='display: block;']").text
print(alert)
assert "Incorrect" in alert

time.sleep(5)