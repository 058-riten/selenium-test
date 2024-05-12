import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

geckodriver_path = r'c:/Drivers/SeleniumDrivers/geckodriver.exe'
os.environ['PATH'] += geckodriver_path
driver = webdriver.Firefox()
driver.get('https://www.facebook.com/')
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)

email = wait.until(EC.presence_of_element_located((By.ID, 'email')))
email.send_keys('<your email>')
pw = wait.until(EC.presence_of_element_located((By.ID, 'pass')))
pw.send_keys('<your password>')
# wait.until(EC.presence_of_element_located((By.ID, 'email'))).send_keys('9860938013')
# wait.until(EC.presence_of_element_located((By.ID, 'pass'))).send_keys('090807')