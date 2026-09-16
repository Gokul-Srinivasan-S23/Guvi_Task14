from driver import driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (NoSuchElementException,TimeoutException,StaleElementReferenceException,ElementNotInteractableException,WebDriverException)
class BasePage():
    #parent class
    def __init__(self,driver,timeout=10):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(self.driver, self.timeout)

    def open(self,url):
        try:
            return self.driver.get(url)
        except WebDriverException as e:
            raise WebDriverException(f"Failed to open URL '{url}' due to {e}")

    def is_visible(self,locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(locator))
        except Exception as e:
            print(f"Error occurred during validation : {e}")

    def is_clickable(self,locator):
        try:
            return self.wait.until(EC.element_to_be_clickable(locator))
        except Exception as e:
            print(f"Error occurred during validation : {e}")

    def is_enabled(self,locator):
        try:
            return self.is_visible(locator).is_enabled()
        except Exception as e:
            print(f"Error occurred during validation : {e}")

    def enter_data(self,locator,data):
        ele = self.is_visible(locator)
        try:
            ele.send_keys(data)
        except Exception as e:
            print(f"Error occurred during entering data : {e}")
        return self
    def click_action(self,locator):
        ele = self.is_clickable(locator)
        try:
            ele.click()
        except Exception as e:
            print(f"Error occurred during clicking action: {e}")
        return self
    def get_title(self):
        return self.driver.title

    def validate_title(self,title):
        try:
            return self.wait.until(EC.title_contains(title))
        except Exception as e:
            print(f"Error occurred during validating title: {e}")

