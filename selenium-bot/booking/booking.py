from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import booking.constants as const
from selenium.common.exceptions import TimeoutException

class Booking(webdriver.Firefox):
    def __init__(self, driver_path=r'c:\Drivers\SeleniumDrivers', teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super().__init__()
        self.implicitly_wait(10)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)
        try:
            element = WebDriverWait(self, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[aria-label="Dismiss sign-in info."]')))
            element.click()
            
        except TimeoutException:
            print("Element with the specified namespace not found within the timeout period.")

    def select_place_to_go(self, place_to_go):
        search_field = self.find_element(By.ID, ':re:')
        search_field.clear()
        search_field.send_keys(place_to_go)

        first_elm = self.find_element(By.CSS_SELECTOR, 'li[id="autocomplete-result-0"]')
        first_elm.click()
    
    def select_dates(self, check_in_date, check_out_date):
        check_in_element = self.find_element(By.CSS_SELECTOR, f'span[data-date="{check_in_date}"]')
        check_in_element.click()

        check_out_element = self.find_element(By.CSS_SELECTOR, f'span[data-date="{check_out_date}"]')
        check_out_element.click()
        
    def click_search(self):
        search_button = self.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        search_button.click()