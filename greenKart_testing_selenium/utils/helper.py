
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

#from conftest import Driver


class Basepage():
    """Contains common wrapper functions for Selenium actions."""
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def click_element(self, locator):
        """Wait for presence then click using JavaScript."""
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].click();", element)

    def click_visible(self, locator):
        """Wait for visibility then click using JavaScript."""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].click();", element)

    def send_text(self, locator, text):
        """Wait for presence, clear field, and send keys."""
        element = self.wait.until(EC.presence_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def locate_element(self, locator):
        """Return element once present in DOM."""
        element = self.wait.until(EC.presence_of_element_located(locator))
        return element

    def visible_element(self, locator):
        """Return element once visible on page."""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element

    def select_option(self, locator, option):
        """Select an option from a dropdown by visible text."""
        dropdown_element = self.wait.until(EC.presence_of_element_located(locator))
        select = Select(dropdown_element)
        select.select_by_visible_text(option)