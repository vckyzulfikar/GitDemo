import time
from selenium import webdriver

#chrome driver
from selenium.webdriver.chrome.service import Service
#-- Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("C:\\chromedriver.exe") # using double back slash
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

# ID, XPath, CSSSelector, Classname, name, linktext
driver.find_element(By.NAME, "email").send_keys("vickyzulfikar20@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID, "exampleCheck1").click()

# XPATH - //tagname[@attribute='value'] -> //input[@type='submit']
# CSS - tagname[attribute]'value'] -> input[type='submit'} #id, .classname
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Vicky")
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()

# Static Dropdown = if tag <select> then use Select class
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_index(0) # Select dropdown by index
dropdown.select_by_visible_text("Female") # Select dropdown by text
#dropdown.select_by_value("Male") # Select dropdown by value


driver.find_element(By.XPATH, "//input[@type='submit']").click() # Get XPATH Button Submit
message = driver.find_element(By.CLASS_NAME, "alert-success").text # Get text notification alert
print(message) # Output alert
assert "Success! The Form has been submitted successfully!." in message

driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("helloagain")
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear() # Clear field


time.sleep(5)