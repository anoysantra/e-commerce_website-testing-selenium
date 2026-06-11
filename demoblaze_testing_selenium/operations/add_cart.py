
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

class Purchaseitem(BasePage):
    def __init__(self,driver,wait):
        super().__init__(driver,wait)
    
    def add_to_cart(self,product_name):
        text_cat = self.visible_element(locators.category_text).text
        print(text_cat)
        product_xpath = f'//a[@class="hrefch" and normalize-space()="{product_name}"]'
        element = (By.XPATH,product_xpath)
        print("element identified")
        print("the xpath :",product_xpath)
        self.click_element(element)
        print("Prod URL; ",self.driver.current_url)
        print("Waiting for product page to load...")
        self.wait.until(EC.url_contains('prod.html'))
        self.click_element(locators.add_to_cart_btn)
        print("element clicked")
        self.handle_alert(action='accept')
        print("Item added")
        self.click_element(locators.home_locator)
        #print("Home URL; ",self.driver.current_url)
        #self.wait.until(EC.visibility_of_element_located(locators.category_text))
        self.wait.until(EC.url_contains("index.html"))
        return 'item accepted'
    """
    def clear_entire_cart(self):
        self.click_element(locators.cart_locator)
        print("Starting cart cleanup...")
        
        while True:
            # Re-find the delete buttons every time because the list changes
            delete_links = self.driver.find_elements(By.LINK_TEXT, "Delete")
            
            if not delete_links:
                print("Cart is now empty.")
                break
                
            # Click the first delete button found
            delete_links[0].click()
            
            # Wait for that specific element to disappear before trying the next one
            self.wait.until(EC.staleness_of(delete_links[0]))
"""




        
