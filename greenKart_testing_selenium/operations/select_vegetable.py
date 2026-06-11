
from locators import Locators
from utils.helper import Basepage
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from operations.product_table import ProductTable

class SelectVegetable(Basepage):

    def __init__(self, driver):
        #self.driver = driver
        super().__init__(driver)
    
    def select_vegetable(self,vegetable_names):
        for vegetable in vegetable_names:
            name = vegetable["name"].strip()
            qty = vegetable["quantity"].strip()
            qty_number = int(qty.split(' ')[0])
            #base_product_xpath = f"//h4[contains(text(), '{name}') and contains(text(), '1 Kg')]/ancestor::div[@class='product']"
            base_product_xpath = f"//h4[normalize-space()='{name} - 1 Kg']/ancestor::div[@class='product']"
            #print(qty_number)
            #print(type(qty_number))
            if qty_number > 1:
                increment_xpath = f"{base_product_xpath}//a[@class='increment']"
                increment_qty_locator = (By.XPATH,increment_xpath)
                for i in range(0,qty_number-1):
                    self.click_element(increment_qty_locator)

            print(f"Name: {name} and quantity: {qty}")
            xpath = f"{base_product_xpath}//button[normalize-space()='ADD TO CART']"
            vegetable_locator = (By.XPATH,xpath)
            self.click_element(vegetable_locator)
            print(f"Successfully clicked 'ADD TO CART' for: {vegetable}")

        self.click_element(Locators.cart_btn_icon_locator)
        print("Opening the dialog checkout box....")
        self.click_element(Locators.proceed_to_checkout_locator)
        print("Pressed Checkout Box")
        #self.wait.url_contains('/cart')
        self.wait.until(EC.url_contains('/cart'))
        cart_url = self.driver.current_url
        print("After URL : ", cart_url)
        return cart_url

        #pt = ProductTable(self.driver)
        #pt.product_table_display()