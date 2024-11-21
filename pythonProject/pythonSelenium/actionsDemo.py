import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

action = ActionChains(driver)
#action.click_and_hold() # Click and Hold mouse
#action.double_click(driver.find_element(By.)) # Double click mouse
#action.context_click() # Right click mouse
#action.drag_and_drop() # Drag and drop with source and target
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform() # Mouse hover
action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()




time.sleep(5)