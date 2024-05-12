import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

geckodriver_path = r'c:/Drivers/SeleniumDrivers/geckodriver.exe'
os.environ['PATH'] += os.pathsep + os.path.dirname(geckodriver_path)
driver = webdriver.Firefox()
driver.get('https://www.wikipedia.org/')

wait = WebDriverWait(driver, 10)
first_element = wait.until(EC.presence_of_element_located((By.ID, 'js-link-box-en')))
first_element.click()

second_element = wait.until(EC.presence_of_element_located((By.ID, 'ca-history')))
second_element.click()
