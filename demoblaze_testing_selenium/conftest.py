import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from operations.login import Loginpage
from helper import BasePage
from locators import locators
from operations.purchase import PlaceOrder


@pytest.fixture(scope="function")
#@pytest.fixture(scope="module")
def driver_setup():
        print("Starting browser........")
        # Essential flags for Codespaces
        options = Options()
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        #driver = webdriver.Chrome(options=options)
        driver = webdriver.Chrome()
        driver.get("https://www.demoblaze.com/")
        wait = WebDriverWait(driver,20)


        yield driver,wait
        
        print("Closing browser.........")
        driver.quit()

#@pytest.fixture(scope="function")
@pytest.fixture(scope="module")
def keep_logged_in():
        print("LOGIN FIXTURE EXECUTED")
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        wait = WebDriverWait(driver,20)
        driver.get("https://www.demoblaze.com/")
        login = Loginpage(driver,wait)
        login.login_ops('anoy_123','anoy123')

        #order = PlaceOrder(driver, wait)
        #order.clear_entire_cart()
        yield driver, wait

        driver.quit()









