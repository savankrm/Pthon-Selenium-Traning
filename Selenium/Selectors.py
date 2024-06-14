import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()
driver.get("https://petstore.octoperf.com/")
time.sleep(3)

elememt=driver.find_element(By.LINK_TEXT,"Enter the Store")
elememt.click()
time.sleep(10)
print("Button has been clicked using link text")

elememt=driver.find_element(By.NAME,"keyword")
elememt.send_keys("Fish")
elememt= driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/form/input[2]")
elememt.click()
time.sleep(10)
print("entered text to serch by using name and made search with xpath")


element= driver.find_element(By.ID,"BackLink")
element.click()
print("Made a back using ID")
time.sleep(4)