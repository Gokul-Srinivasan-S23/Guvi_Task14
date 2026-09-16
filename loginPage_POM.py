from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Pages import basePage_POM
from Pages.basePage_POM import BasePage



class LoginPage(BasePage):
    email = (By.ID, ":r1:")
    password = (By.ID, ":r2:")
    rememberMe_text = (By.CLASS_NAME, "remeber-me-text")
    rememberMe_check = (By.CSS_SELECTOR, "input[aria-label='Checkbox demo']")
    forgotpassword = (By.CSS_SELECTOR, ".forgot-text-container")
    signin_button = (By.CSS_SELECTOR, "button[type='submit']")
    page_title = "GUVI"
    invalid_response = (By.CSS_SELECTOR,".password-input")
    incorrect_email = (By.CSS_SELECTOR,"p[id=':r1:-helper-text']")
    incorrect_password = (By.CSS_SELECTOR,"p[id=':r2:-helper-text']")

    def is_incorrect_email_displayed(self):
        return self.is_visible(self.incorrect_email)

    def is_error_passwordfield(self):
        return self.is_visible(self.incorrect_password)

    def is_invalid_response_displayed(self):
        return self.is_visible(self.invalid_response)

    def enter_email(self,data):
        return self.enter_data(self.email,data)

    def enter_password(self,data):
        return self.enter_data(self.password,data)

    def check_rememberMe(self):
        return self.click_action(self.rememberMe_check)

    def click_forgotpassword(self):
        return self.click_action(self.forgotpassword)

    def click_signin(self):
        return self.click_action(self.signin_button)

    def is_email_enabled(self):
        return self.is_enabled(self.email)

    def is_password_enabled(self):
        return self.is_enabled(self.password)

    def is_rememberMe_displayed(self):
        return self.is_visible(self.rememberMe_text)

    def is_rememberMe_enabled(self):
        return self.is_enabled(self.rememberMe_check)

    def is_forgotpassword_displayed(self):
        return self.is_visible(self.forgotpassword)

    def is_signin_clickable(self):
        return self.is_clickable(self.signin_button)

    def is_on_login_page(self):
         return self.validate_title(self.page_title)

    def login(self,email,password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_signin()


