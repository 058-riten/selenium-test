from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

firefox_driver_path = 'C:/Drivers/SeleniumDrivers/geckodriver.exe'
driver = webdriver.Firefox()
driver.maximize_window()
driver.get('https://orteil.dashnet.org/cookieclicker/')

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'langSelect-EN'))).click()
WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.ID, 'loader')))

cookie = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'bigCookie')))
cookie.click()

while True:
    cookie.click()
    cookies_count = driver.find_element(By.ID, 'cookies').text.split(" ")[0]
    cookies_count = int(cookies_count.replace(',', ''))

    for i in range(4):
        product_price = driver.find_element(By.ID, "productPrice" + str(i)).text.replace(',', '')

        if not product_price.isdigit():
            continue

        product_price = int(product_price)

        if cookies_count >= product_price:
            product = driver.find_element(By.ID, 'product' + str(i))
            product.click()
            break
            