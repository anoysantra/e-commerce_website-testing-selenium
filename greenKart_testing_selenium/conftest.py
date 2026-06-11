import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="function")
def driver():
    options = Options()
    
    # These flags are essential for cloud/container environments
    options.add_argument("--headless=new") # Runs Chrome without a GUI
    options.add_argument("--no-sandbox")     # Required for many Docker/Linux setups
    options.add_argument("--disable-dev-shm-usage") # Prevents memory issues in containers
    
    driver = webdriver.Chrome(options=options)
    #driver = webdriver.Chrome()
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
    driver.maximize_window()

    yield driver

    driver.quit()
