import time

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.selenium.dev/documentation/")

lnks = driver.find_elements(By.TAG_NAME, "a")

print("No. of Links available in the page", len(lnks))

for totals in lnks:
    print(totals.text)

lnks[11].click()

time.sleep(4)
driver.close()
