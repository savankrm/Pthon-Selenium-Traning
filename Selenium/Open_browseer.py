import selenium
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
driver= webdriver.Chrome()
driver.get("https://google.com")
driver.close()