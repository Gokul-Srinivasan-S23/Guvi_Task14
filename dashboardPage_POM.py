from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Pages import basePage_POM
from Pages.basePage_POM import BasePage
from Pages.loginPage_POM import LoginPage



class DashboardPage(BasePage):

    page_title = "GUVI"
    url_segment = "/dashboard"
    profile_icon = (By.CSS_SELECTOR,"#profile-click-icon")
    logout_button = (By.XPATH, "//*[@id='root']/div[2]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div[4]")


    def is_profile_icon_displayed(self):
        return self.is_visible(self.profile_icon)

    def is_logout_displayed(self):
        self.click_action(self.profile_icon)
        return self.is_visible(self.logout_button)

    def is_profile_icon_clickable(self):
        return self.is_clickable(self.profile_icon)

    def is_logout_clickable(self):
        self.click_action(self.profile_icon)
        return self.is_clickable(self.logout_button)


    def clicking_profile_icon(self):
        return self.click_action(self.profile_icon)

    def clicking_logout(self):
        self.click_action(self.profile_icon)
        return self.click_action(self.logout_button)

    def is_on_dashboard(self):
        try:
            return self.wait.until(expected_conditions.url_contains(self.url_segment))
        except Exception as e:
            return False

    def logout(self):
        return self.clicking_logout()
