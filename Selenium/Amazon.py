from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
driver= webdriver.Chrome()
driver.get("http://amazon.in")
driver.maximize_window()

elements= driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input")
elements.send_keys("macbook")
elements= driver.find_element(By.ID,"nav-search-submit-button")
elements.click()
item1= driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[5]/div/div/div/div/div/div[2]/div/div/div[1]/h2/a/span")
item1.click()

time.sleep(4)
#get current window handle
# Get the current window handle
parent_handle = driver.current_window_handle

# Get all window handles
window_handles = driver.window_handles

# Iterate through all window handles
for handle in window_handles:
    # If handle is not equal to the current window handle
    if handle != parent_handle:
        # Switch to the new window handle
        driver.switch_to.window(handle)


time.sleep(2)
cart= driver.find_element(By.XPATH,"/html/body/div[4]/div[2]/div[3]/div[9]/div[7]/div/div[1]/div/div[1]/div/div/div[2]/div/div[2]/div/form/div/div/div[32]/div[1]/span/span/span/input")
cart.click()
time.sleep(3)
driver.close()
driver.switch_to.window(parent_handle)

item2=driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[4]/div/div/div/div/div/div/div/div[2]/div/div/div[1]/h2/a/span")
item2.click()

window_handles = driver.window_handles
for handle in window_handles:
    # If handle is not equal to the current window handle
    if handle != parent_handle:
        # Switch to the new window handle
        driver.switch_to.window(handle)

cart2= driver.find_element(By.XPATH,"/html/body/div[4]/div[2]/div[3]/div[9]/div[7]/div/div[1]/div/div[1]/div/div/div[2]/div/div[2]/div/form/div/div/div[32]/div[1]/span/span/span/input")
cart2.click()


time.sleep(3)
driver.close()
driver.switch_to.window(parent_handle)
driver.refresh()
driver.refresh()

print("Number of items in the cart is:-",driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[1]/div[3]/div/a[4]/div[1]/span[1]").text)


driver.quit()
