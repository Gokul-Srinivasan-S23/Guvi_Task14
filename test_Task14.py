import time

import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common import keys

from Pages.loginPage_POM import LoginPage
from Pages.dashboardPage_POM import DashboardPage


valid_Username = ""
valid_password = ""
invalid_Username = "JUIOOP@gmail.com"
invalid_password = "HJUIoaas"


def test_pos_successful_login(login_page,dashboard_page):
    assert login_page.is_on_login_page(),"Not in Login Page"
    login_page.login(valid_Username, valid_password)
    assert dashboard_page.is_on_dashboard(),"Not in Dashboard Page"

def test_neg_unsuccessful_login(login_page,dashboard_page):
    assert login_page.is_on_login_page(),"Not in Login Page"
    login_page.login(invalid_Username, invalid_password)
    assert login_page.is_invalid_response_displayed(),"Login was successful"
    assert not dashboard_page.is_on_dashboard(),"In Dashboard Page"

def test_validate_pos_username(login_page):
    assert login_page.is_on_login_page(),"Not in Login Page"
    assert login_page.is_email_enabled(),"Email textbox is not enabled"
    login_page.enter_email("test@gmail.com"+ Keys.TAB)
    login_page.click_signin()
    assert not login_page.is_incorrect_email_displayed(),"Error msg displayed"

def test_validate_neg_username(login_page):
    assert login_page.is_on_login_page(),"Not in Login Page"
    assert login_page.is_email_enabled(),"Email textbox is not enabled"
    login_page.enter_email("test"+ Keys.TAB)
    login_page.click_signin()
    assert login_page.is_incorrect_email_displayed(),"Error msg not displayed"

def test_validate_pos_password(login_page):
    assert login_page.is_on_login_page(),"Not in Login Page"
    assert login_page.is_password_enabled(),"Password textbox is not enabled"
    login_page.login(valid_Username, valid_password)
    assert not login_page.is_error_passwordfield(),"Error msg displayed"

def test_validate_neg_password(login_page):
    assert login_page.is_on_login_page(),"Not in Login Page"
    assert login_page.is_password_enabled(),"Password textbox is not enabled"
    login_page.login(valid_Username, invalid_password)
    assert login_page.is_error_passwordfield(),"Error msg not displayed"

def test_validate_pos_submit_button(login_page,dashboard_page):
    assert login_page.is_on_login_page(),"Not in Login Page"
    assert login_page.is_signin_clickable(),"sign in button is not clickable"
    login_page.login(valid_Username, valid_password)
    assert dashboard_page.is_on_dashboard(),"Dashboard page is not displayed"
    assert dashboard_page.is_profile_icon_displayed(),"Dashboard page is not displayed"

def test_validate_neg_submit_button(login_page):
    assert login_page.is_on_login_page(),"Not in Login Page"
    assert login_page.is_signin_clickable(),"Sign in button is not clickable"
    login_page.click_signin()
    assert login_page.is_error_passwordfield(),"Error msg not displayed"

def test_validate_logout(login_page,dashboard_page):
    assert login_page.is_on_login_page(),"Not in Login Page"
    login_page.login(valid_Username, valid_password)
    assert dashboard_page.is_on_dashboard(),"Not in Dashboard Page"
    assert dashboard_page.is_profile_icon_displayed(),"Dashboard page is not displayed"
    assert dashboard_page.is_logout_clickable(),"Dashboard page is not clickable"
    dashboard_page.clicking_profile_icon()
    dashboard_page.clicking_logout()
    assert login_page.is_on_login_page(),"Not returned to Logout Page"










