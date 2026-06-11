from utils.helper import Basepage
from selenium.webdriver.common.by import By

class ShowTotal(Basepage):
    def __init__(self, driver):
        super().__init__(driver)
        
    def show_total(self):
        total = self.driver.find_element(By.CSS_SELECTOR, "span.totAmt").text
        discount = self.driver.find_element(By.CSS_SELECTOR, "span.discountPerc").text
        final_total = self.driver.find_element(By.CSS_SELECTOR, "span.discountAmt").text
        print(f"Gross Total: {total}")
        print(f"Discount   : {discount}")
        print(f"Net Total  : {final_total}")
        return final_total,discount,total