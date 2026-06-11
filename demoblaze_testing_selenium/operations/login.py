
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from helper import BasePage
from locators import locators

class Loginpage(BasePage):
    def __init__(self,driver,wait):
        super().__init__(driver,wait)

    def login_ops(self,username_text,password_text):
        """
        try:
            alert = self.driver.switch_to.alert
            alert.accept()
        except:
            pass
        """
        self.click_element(locators.login_navbar)
        self.visible_element(locators.login_modal_header)
        print("Starting Login with creds....")
        self.send_text(locators.username,username_text)
        self.send_text(locators.password,password_text)
        self.click_element(locators.login_button)
        print("login btn clicked")
        name = self.visible_element(locators.name_of_user).text
        return name
        #return self.driver.current_url








