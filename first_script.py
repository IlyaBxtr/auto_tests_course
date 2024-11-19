import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
#open link
driver = webdriver.Chrome()
time.sleep(5)
driver.get("https://suninjuly.github.io/text_input_task.html")
time.sleep(5)
#find element
textarea= driver.find_element(By.CSS_SELECTOR, "submit-submission")
textarea.send_keys("get()")
time.sleep(5)

driver.quit()
