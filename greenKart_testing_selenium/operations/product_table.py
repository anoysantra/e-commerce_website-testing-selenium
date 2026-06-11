from locators import Locators
from utils.helper import Basepage
from selenium.webdriver.common.by import By


class ProductTable(Basepage):
    """Add your business logic and page operations here."""
    def __init__(self, driver):
        super().__init__(driver)
        #self.driver = Driver()

    def product_table_display(self):
        table = self.locate_element(Locators.cart_product_table)
        rows = table.find_elements(By.TAG_NAME,'tr')
        vegetables = []
        for row in rows[1:]:
            cells = row.find_elements(By.TAG_NAME,'td')
            if len(cells) >= 5:
                vegetable = {
                    'product_name' : cells[1].text,
                    'quantity' : cells[2].text,
                    'price' : cells[3].text,
                    'total' : cells[4].text
                }
                vegetables.append(vegetable)
        print("PRODUCT : ", vegetables)
        count_vegetables_in_cart = len(vegetables)
        return count_vegetables_in_cart
