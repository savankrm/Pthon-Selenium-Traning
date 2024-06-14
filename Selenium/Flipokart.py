from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver= webdriver.Chrome()
driver.get("http://flipkart.com")
driver.maximize_window()

element=driver.find_element(By.XPATH,"/html/body/div[2]/div/div/button")
element.click()

a = ActionChains(driver)
m= driver.find_element(By.LINK_TEXT,"Electronics")
a.move_to_element(m).perform()

m= driver.find_element(By.LINK_TEXT,"Computer Peripherals")
a.move_to_element(m).perform()
m= driver.find_element(By.LINK_TEXT,"Printers")
a.move_to_element(m).click().perform()
time.sleep(6)
l=driver.find_element(By.XPATH,"/html/body/div/div/div[3]/div/div[1]/div/div/div/section[2]/div[3]/div[1]/div[1]/div")
a.drag_and_drop_by_offset(l,110,0).perform()

time.sleep(3)
r=driver.find_element(By.XPATH,"/html/body/div/div/div[3]/div/div[1]/div/div/div/section[2]/div[3]/div[1]/div[2]/div")
a.drag_and_drop_by_offset(r,-90,0).perform()
time.sleep(5)

product=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div/div[2]/div[3]/div/div[3]/div/a[2]").click()

current_window_handle = driver.current_window_handle

# Get all window handles
window_handles = driver.window_handles

# Iterate through all window handles
for handle in window_handles:
    # If handle is not equal to the current window handle
    if handle != current_window_handle:
        # Switch to the new window handle
        driver.switch_to.window(handle)

add=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div[1]/div[1]/div[2]/div/ul/li[1]/button").click()
time.sleep(5)

driver.close()
