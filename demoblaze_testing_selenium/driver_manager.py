

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

class Driver():
    """Manages the WebDriver lifecycle and configuration."""
    def setup(self):
        options = Options()
        # Essential flags for Codespaces
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        #options.add_argument("--disable-gpu")
        
        # Point to the Chromium binary we just installed
        #options.binary_location = "/usr/bin/chromium-browser"
        
        # Initialize the driver
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://www.demoblaze.com/")
        self.wait = WebDriverWait(self.driver,20)
        
        return self.driver,self.wait

    def teardown(self):
        if self.driver:
            self.driver.quit()