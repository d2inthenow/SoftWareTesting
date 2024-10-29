from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.login import Login
import pytest
from driver.driver import Driver

class TestLogin(Driver):
    def test_signIn(self,driver):
        login_page = Login(driver)
        login_page.signIn('duong0023@gmail.com','12345')
        assert "account/account" in login_page.get_current_url()
    
    def test_signIn_no_password(self,driver):
        login_page = Login(driver)
        login_page.signIn_nopassword('duong0023@gmail.com')
        error_message = login_page.message()
        print(error_message)
        assert "Warning: No match for E-Mail Address and/or Password." in error_message
    
    def test_signIn_no_email(self,driver):
        login_page = Login(driver)
        login_page.signIn_noemail('12345')
        error_message = login_page.message()
        assert "Warning: No match for E-Mail Address and/or Password." in error_message

    def test_signIn_empty(self,driver):
        login_page = Login(driver)
        login_page.signIn('','')
        error_message = login_page.message()
        assert "Warning: No match for E-Mail Address and/or Password." in error_message
    
    def test_signIn_not_exist(self,driver):
        login_page = Login(driver)
        login_page.signIn('abc@gmail.com','12345')
        error_message = login_page.message()
        assert "Warning: No match for E-Mail Address and/or Password." in error_message
    
    def test_logOut(self,driver):
        login_page = Login(driver)
        login_page.signIn('duong0023@gmail.com','12345')
        login_page.logout()
        assert "account/logout" in login_page.get_current_url()
    
