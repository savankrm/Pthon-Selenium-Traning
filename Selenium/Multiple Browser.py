import selenium
from selenium.webdriver.chrome import webdriver
from selenium import webdriver

#Open Chrome
driver= webdriver.Chrome()
driver.get("http://google.com")
driver.close()

#Open Edge
driver= webdriver.Edge()
driver.get("http://bing.com")
driver.close()

#Open Safari
driver= webdriver.Safari()
driver.maximize_window()
driver.get("http://youtube.com")

driver.close()