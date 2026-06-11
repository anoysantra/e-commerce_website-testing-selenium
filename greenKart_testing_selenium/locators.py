
from selenium.webdriver.common.by import By

class Locators:
    cart_btn_icon_locator = (By.XPATH, "//a[@class='cart-icon']")
    proceed_to_checkout_locator = (By.XPATH, "//button[normalize-space()='PROCEED TO CHECKOUT']")
    cart_product_table = (By.XPATH,'//table[@class="cartTable"]')
    #total_locator = (By.CLASS_NAME,'promoWrapper')
    promo_code_locator = (By.CSS_SELECTOR,'input.promoCode')
    apply_button_promocode = (By.CSS_SELECTOR,'button.promoBtn')
    promo_msg = (By.CSS_SELECTOR,'span.promoInfo')
   