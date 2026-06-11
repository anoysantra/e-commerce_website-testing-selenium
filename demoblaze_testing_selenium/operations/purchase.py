

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

class PlaceOrder(BasePage):
    def __init__(self,driver,wait):
        super().__init__(driver,wait)

    def show_products(self):
        #navigate to cartfirst
        self.click_element(locators.cart_locator)
        print("Cart URL :", self.driver.current_url)
        #table
        product_text_locator = ( By.XPATH, "//h2[normalize-space()='Products']")
        self.locate_element(product_text_locator)
        table = self.locate_element(locators.cart_table_body)
        rows = table.find_elements(By.TAG_NAME,'tr')
        products = []
        for row in rows:
            cells = row.find_elements(By.TAG_NAME,'td')
            if len(cells) >= 3:
                item = {
                    'title' : cells[1].text,
                    'price' : cells[2].text
                }
                products.append(item)
        print("Cart Products : ", products)
        return len(products),products
    
    def place_order(self):
        self.click_element(locators.place_order_button)
    
    def form_fill(self,data_customer):
        text_place_order = self.visible_element(locators.place_order_text).text
        print(text_place_order)
        # 2. Fill the fields using the dictionary keys
        print("Filling customer details...")
        self.send_text(locators.name, data_customer['name'])
        self.send_text(locators.country, data_customer['country'])
        self.send_text(locators.city, data_customer['city'])
        self.send_text(locators.card, data_customer['card'])
        self.send_text(locators.month, data_customer['month'])
        self.send_text(locators.year, data_customer['year'])

        # 3. Click Purchase
        print("Clicking final Purchase button...")
        self.click_element(locators.purchase_btn)

        msg = self.visible_element(locators.thank_you_msg).text
        print("Final Msg : ", msg)
        return msg

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
