from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()

driver.get("https://www.globalsqa.com/demo-site/select-dropdown-menu/")

drop_down = Select(driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div/div/div[2]/div/div/div/p/select"))

default_selected_option = drop_down.first_selected_option.text
print("The default selected option is:", default_selected_option)

drop_down.select_by_visible_text("India")

newly_selected_option = drop_down.first_selected_option.text
print("The newly selected option is:", newly_selected_option)

assert newly_selected_option == "India", "The newly selected option is not Afghanistan"
driver.quit()
