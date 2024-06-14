# Import selenium module
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


# Using chrome driver
driver = webdriver.Chrome()


# Web page url
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")


# Selecting radio button
# Select male
driver.find_element(By.XPATH,
	'//*[@id="q26"]/table/tbody/tr[1]/td/label').click()


# Selecting check box
# Select sunday
driver.find_element(By.XPATH,
	'//*[@id="q15"]/table/tbody/tr[1]/td/label').click()


# Select monday
driver.find_element(By.XPATH,
	'//*[@id="q15"]/table/tbody/tr[2]/td/label').click()

time.sleep(3)
driver.quit()