from locators import Locators
from utils.helper import Basepage
from selenium.webdriver.common.by import By

class PromoCode(Basepage):
    def __init__(self, driver):
        super().__init__(driver)    
        self.driver=driver
         
    def promo_code(self,promocode):
        self.send_text(Locators.promo_code_locator,promocode)
        self.click_element(Locators.apply_button_promocode)
        msg = self.locate_element(Locators.promo_msg).text
        print("After applying coupon msg : ",msg)
        return msg
    
