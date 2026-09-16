import pytest
from selenium import webdriver
from Pages.loginPage_POM import LoginPage
from Pages.dashboardPage_POM import DashboardPage

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get("https://v2.zenclass.in/login")
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def login_page(setup):
    driver = setup
    return LoginPage(driver)

@pytest.fixture
def dashboard_page(setup):
    driver = setup
    return DashboardPage(driver)

