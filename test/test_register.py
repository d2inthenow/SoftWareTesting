from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.register import Register
import pytest
from driver.driver import Driver
import time

class TestRegister(Driver):
    def test_register(self,driver):
        register_page = Register(driver)
        register_page.register('dongduong','too','opencartttdemon@gmail.com','12345')
        time.sleep(2)
        assert "account/success" in register_page.get_current_url()
    
    def test_register_exit_email(self,driver):
        """
        Test case for verifying the registration process with an already registered email.
        Args:
        self: Instance of the test class.
        driver: WebDriver instance used to interact with the web page.
        Steps:
        1. Initialize the Register page object with the WebDriver instance.
        2. Attempt to register with a first name, last name, already registered email, and password.
        3. Wait for 2 seconds to allow the page to process the registration.
        4. Retrieve the error message displayed on the page.
        5. Assert that the error message contains the warning about the email address being already registered.
        Expected Result:
        The error message should contain the text "Warning: E-Mail Address is already registered!".
        """

        register_page = Register(driver)
        register_page.register('duong','to','duong0023@gmail.com','12345')
        time.sleep(2)
        error_message = driver.find_element(By.XPATH, "/html/body/div[1]/dirv").text
        assert "Warning: E-Mail Address is already registered!" in error_message

    def test_register_noClick_privacy_policy(self,driver):
        """
        Test case for verifying the registration process without clicking the privacy policy checkbox.
        Args:
            driver (WebDriver): The WebDriver instance used to interact with the web page.
        Steps:
            1. Initialize the Register page object with the provided driver.
            2. Attempt to register with the provided user details without clicking the privacy policy checkbox.
            3. Wait for 2 seconds to allow the error message to appear.
            4. Locate the error message element on the page.
            5. Assert that the error message contains the expected warning about agreeing to the Privacy Policy.
        Expected Result:
            The error message should contain the text "Warning: You must agree to the Privacy Policy!".
        """

        register_page = Register(driver)
        register_page.register_noClick_privacy_policy('duong','to','abcvxbs@gmail.com','12345')
        time.sleep(2)
        error_message = driver.find_element(By.XPATH, "/html/body/div[1]/dirv").text
        assert "Warning: You must agree to the Privacy Policy!" in error_message

    def test_register_weak_password(self,driver):
        """
        Test case for registering with a weak password.
        This test verifies that the registration process correctly identifies and 
        rejects a weak password that does not meet the required length criteria.
        Args:
            driver (WebDriver): The WebDriver instance used to interact with the web page.
        Steps:
            1. Initialize the Register page object with the provided driver.
            2. Attempt to register with a weak password ('1').
            3. Wait for 2 seconds to allow the page to process the registration.
            4. Locate the error message element on the page.
            5. Assert that the error message contains the expected text indicating 
               that the password must be between 4 and 20 characters.
        Asserts:
            The error message displayed on the page contains the text 
            "Password must be between 4 and 20 characters!".
        """

        register_page = Register(driver)
        register_page.register('duong','to','abcvxbs@gmail.com','1')
        time.sleep(2)
        error_message = driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/form/fieldset[2]/div/div/div").text
        assert "Password must be between 4 and 20 characters!" in error_message
    
    def test_register_no_input(self,driver):
        """
        Test case for the registration page with no input provided.
        This test verifies that appropriate error messages are displayed when 
        the registration form is submitted without any input.
        Args:
            driver (WebDriver): The WebDriver instance used to interact with the web page.
        Steps:
            1. Initialize the Register page object.
            2. Call the register method with empty strings for all input fields.
            3. Wait for 2 seconds to allow error messages to appear.
            4. Verify that the error message for the first name field is displayed and correct.
            5. Verify that the error message for the last name field is displayed and correct.
            6. Verify that the error message for the email address field is displayed and correct.
            7. Verify that the error message for the password field is displayed and correct.
        Asserts:
            - "First Name must be between 1 and 32 characters!" is in the error message for the first name field.
            - "Last Name must be between 1 and 32 characters!" is in the error message for the last name field.
            - "E-Mail Address does not appear to be valid!" is in the error message for the email address field.
            - "Password must be between 4 and 20 characters!" is in the error message for the password field.
        """

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

    