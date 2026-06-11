# Selenium Online Compiler (Python)
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
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
        self.driver.get("https://rahulshettyacademy.com/locatorspractice/")
        return self.driver

        #self.driver.get("https://rahulshettyacademy.com/locatorspractice/")
        #return self.driver

    def teardown(self):
        if self.driver:
            self.driver.quit()

class BasePage:
    """Utility wrapper for common Selenium interactions."""
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def click_element(self, locator):
        """Wait for presence then click via JavaScript (bypasses overlays)."""
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].click();", element)

    def click_visible(self, locator):
        """Wait for visibility then click via JavaScript."""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].click();", element)

    def send_text(self, locator, text):
        """Clear field and send keys."""
        element = self.wait.until(EC.presence_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def locate_element(self, locator):
        """Return element once present in DOM."""
        return self.wait.until(EC.presence_of_element_located(locator))

    def visible_element(self, locator):
        """Return element once visible on UI."""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def select_option(self, locator, option_text):
        """Select from a <select> dropdown by visible text."""
        dropdown_element = self.wait.until(EC.presence_of_element_located(locator))
        select = Select(dropdown_element)
        select.select_by_visible_text(option_text)

class Locators:
    """
    Define locators here.
    Example: LOGIN_BTN = (By.ID, 'login')
    """
    forget_password_locator = (By.CSS_SELECTOR,'div.forgot-pwd-container a')
    text_locator = (By.CSS_SELECTOR,'div.sign-up-container form h2') #contains text-forget password
    info_msg_locator = (By.CLASS_NAME,'infoMsg')
    name_locator = (By.XPATH,'//input[@placeholder="Name"]')
    phone_locator = (By.XPATH,'//input[@placeholder="Email"]')
    email_locator = (By.XPATH,'//input[@placeholder="Phone Number"]')
    go_to_login_button = (By.XPATH,'//button[normalize-space()="Go to Login"]')
    reset_button = (By.XPATH,'//button[normalize-space()="Reset Login"]')
    #login_page locator
    login_text_locator = (By.CSS_SELECTOR,'div.sign-in-container form h1')
    username = (By.ID,'inputUsername')
    password = (By.CSS_SELECTOR, 'input[name="inputPassword"]')
    login_button = (By.CSS_SELECTOR, 'button.submit.signInBtn')
    checkbox_1 = (By.CSS_SELECTOR,'input#chkboxOne')
    checkbox_2 = (By.CSS_SELECTOR,'input#chkboxTwo')

class Operation(BasePage):
    """Define specific test steps and business workflows here."""
    def login(self):
        login_text = self.visible_element(Locators.login_text_locator).text
        print("Login Text : ",login_text)
        self.send_text(Locators.username,'rahulshettyacademy')
        self.send_text(Locators.password,'rahulshettyacademy')
        self.click_element(Locators.checkbox_1)
        self.click_element(Locators.checkbox_2)
        self.click_element(Locators.login_button)
        print("After LOGIN URL : ",self.driver.current_url)

    def forget_password(self):
        self.click_element(Locators.forget_password_locator)
        msg = self.visible_element(Locators.text_locator).text
        print(msg)
        self.send_text(Locators.name_locator,'testuser')
        self.send_text(Locators.name_locator,'testuser12@gmail.com')
        self.send_text(Locators.name_locator,'916443870')
        self.click_element(Locators.reset_button)
        print("Reset Button Clicked")
        info_msg = self.visible_element(Locators.info_msg_locator).text
        print(info_msg)
        self.click_element(Locators.go_to_login_button)
        print("Go to login button clicked")

if __name__ == '__main__':
    # Configuration
    # Initialize Driver
    driver_manager = Driver()
    my_driver = driver_manager.setup()
    try:
        # Instantiate Operations class
        app = Operation(my_driver)
        # Execute Workflows
        print(f"Testing started on: {my_driver.current_url}")
        app.forget_password()
        app.login()
    except Exception as e:
        print(f"An error occurred: {type(e).__name__}")
        print(f"Error Details: {e}")
    finally:
        # Clean up
        driver_manager.teardown()