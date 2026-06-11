from selenium import webdriver
from selenium.webdriver.common.by import By

class locators:
    #creds
    login_navbar = (By.CSS_SELECTOR,'a#login2')
    username = (By.ID,'loginusername')
    password = (By.ID,'loginpassword')
    login_button = (By.XPATH,'//button[contains(@class,"btn-primary") and normalize-space()="Log in"]')
    login_modal_header = (By.ID, 'logInModalLabel')
    name_of_user = (By.ID,'nameofuser')
    #categories
    category_text = (By.ID,'cat')
    phones_selector = (By.XPATH, '//a[@id="itemc" and normalize-space()="Phones"]')
    laptops_btn = (By.XPATH, '//a[@id="itemc" and normalize-space()="Laptops"]')
    monitors_btn = (By.XPATH, '//a[@id="itemc" and normalize-space()="Monitors"]')
    #product
    #mobiles
    samsung_galaxy = (By.XPATH,'//a[@class="hrefch" and normalize-space()="Samsung galaxy s6"]')
    #nokia_lumia = (By.XPATH,'//a[@class="hrefch" and normalize-space()="Nokia lumia 1520"]')
    nokia_lumia = (By.XPATH,'//a[contains(@href,"idp_=2")and normalize-space()="Nokia lumia 1520"]')
    nexus_6 = (By.XPATH,'//a[@class="hrefch" and normalize-space()="Nexus 6"]')
    #laptops
    sony_vaio = (By.XPATH,'//a[@class="hrefch" and normalize-space()="Sony vaio i5"]')
    macbook = (By.XPATH,'//a[@class="hrefch" and normalize-space()="MacBook air"]')
    #monitors
    apple_monitor = (By.XPATH,'//a[@class="hrefch" and normalize-space()="Apple monitor 24"]')
    asus_monitor = (By.XPATH,'//a[@class="hrefch" and normalize-space()="ASUS Full HD"]')
    add_to_cart_btn = (By.XPATH,'//a[contains(@class,"btn-success") and normalize-space()="Add to cart"]')
    #alert is there accept it after add to cart
    #cart
    cart_locator = (By.XPATH,'//a[@id="cartur" and normalize-space()="Cart"]')
    home_locator = (By.XPATH,'//a[contains(., "Home")]')
    #table
    cart_table_body = (By.ID, "tbodyid")
    #total
    total_price = (By.ID, "totalp")
    place_order_button = (By.XPATH,"//button[normalize-space()='Place Order']")
    #last_modal_purchase
    name = (By.ID, 'name')
    country = (By.ID, 'country')
    city = (By.ID, 'city')
    card = (By.ID, 'card')
    month = (By.ID, 'month')
    year = (By.ID, 'year')
    purchase_btn = (By.XPATH, '//button[text()="Purchase"]')

    thank_you_msg = (By.XPATH, "//h2[contains(text(), 'Thank you for your purchase!')]")
    place_order_text = (By.ID,'orderModalLabel')


