from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.register import Register
import pytest
from driver.driver import Driver
import time

class TestRegister(Driver):
    def test_register(self,driver):
        register_page = Register(driver)
        register_page.register('dongduong','too','opencart@gmail.com','12345')
        time.sleep(2)
        assert "account/success" in register_page.get_current_url()
    
    def test_register_exit_email(self,driver):
        register_page = Register(driver)
        register_page.register('duong','to','duong0023@gmail.com','12345')
        time.sleep(2)
        error_message = driver.find_element(By.XPATH, "/html/body/div[1]/dirv").text
        assert "Warning: E-Mail Address is already registered!" in error_message

    def test_register_noClick_privacy_policy(self,driver):
        register_page = Register(driver)
        register_page.register_noClick_privacy_policy('duong','to','abcvxbs@gmail.com','12345')
        time.sleep(2)
        error_message = driver.find_element(By.XPATH, "/html/body/div[1]/dirv").text
        assert "Warning: You must agree to the Privacy Policy!" in error_message

    def test_register_weak_password(self,driver):
        register_page = Register(driver)
        register_page.register('duong','to','abcvxbs@gmail.com','1')
        time.sleep(2)
        error_message = driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/form/fieldset[2]/div/div/div").text
        assert "Password must be between 4 and 20 characters!" in error_message
    
    def test_register_no_input(self,driver):
        register_page = Register(driver)
        register_page.register('','','','')
        time.sleep(2)
        error_message1 = driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/form/fieldset[1]/div[1]/div/div").text
        assert "First Name must be between 1 and 32 characters!" in error_message1
        error_message2 = driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/form/fieldset[1]/div[2]/div/div").text
        assert "Last Name must be between 1 and 32 characters!" in error_message2
        error_message3 = driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/form/fieldset[1]/div[3]/div/div").text
        assert "E-Mail Address does not appear to be valid!" in error_message3
        error_message4 = driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/form/fieldset[2]/div/div/div").text
        assert "Password must be between 4 and 20 characters!" in error_message4

    