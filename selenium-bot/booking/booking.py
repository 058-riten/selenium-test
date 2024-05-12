from types import TracebackType
from typing import Type
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
            element = WebDriverWait(self, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[aria-label="Dismiss sign-in info."]')))
            element.click()
            
        except TimeoutException:
            print("Element with the specified namespace not found within the timeout period.")

    # def change_currency(self, currency = None):
    #     wait = WebDriverWait(self, 10)
    #     currency_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="header-currency-picker-trigger"]')))
    #     currency_element.click()
    #     selected_currency_element = WebDriverWait(self, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, f'div[ea1163d21f*="{currency}"]')))
    #     selected_currency_element.click()

    def select_place_to_go(self, place_to_go):
        search_field = WebDriverWait(self, 5).until(EC.presence_of_element_located((By.ID, ':re:')))
        search_field.clear()
        search_field.send_keys(place_to_go)
        first_elm = WebDriverWait(self, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'li[id="autocomplete-result-0"]')))
        first_elm.click()