from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.login import Login
import pytest
from driver.driver import Driver

class TestLogin(Driver):
    def test_signIn(self,driver):
        """
    Test the sign-in functionality of the login page.
    This test will:
    1. Instantiate the Login page object with the provided WebDriver.
    2. Attempt to sign in using the provided email and password.
    3. Assert that the current URL contains "account/account" to verify successful login.
    Args:
    self: The instance of the test case.
    driver: The WebDriver instance used to interact with the web page.
    Raises:
    AssertionError: If the current URL does not contain "account/account".
        """
        login_page = Login(driver)
        login_page.signIn('aaa@gmail.com','12345')
        assert "account/account" in login_page.get_current_url()
    
    def test_signIn_no_password(self,driver):
        """
        Test case for signing in without providing a password.
        This test verifies that an appropriate error message is displayed when 
        attempting to sign in with an email address but without a password.
        Args:
            driver (WebDriver): The WebDriver instance used to interact with the web page.
        Steps:
            1. Initialize the Login page object with the provided WebDriver.
            2. Attempt to sign in using the email 'duong0023@gmail.com' without a password.
            3. Retrieve the error message displayed on the login page.
            4. Print the error message for debugging purposes.
            5. Assert that the error message contains the expected warning about missing password.
        Asserts:
            The error message should contain the text "Warning: No match for E-Mail Address and/or Password."
        """

        login_page = Login(driver)
        login_page.signIn_nopassword('duong0023@gmail.com')
        error_message = login_page.message()
        print(error_message)
        assert "Warning: No match for E-Mail Address and/or Password." in error_message
    
    def test_signIn_no_email(self,driver):
        """
        Test the sign-in functionality with no email provided.
        This test case verifies that attempting to sign in without providing an email
        address results in the appropriate error message being displayed.
        Args:
            driver (WebDriver): The WebDriver instance used to interact with the web page.
        Steps:
            1. Initialize the Login page object with the provided WebDriver.
            2. Attempt to sign in using a password but no email.
            3. Retrieve the error message displayed on the login page.
            4. Assert that the error message contains the expected warning about no match
               for the email address and/or password.
        Asserts:
            The error message should contain the text "Warning: No match for E-Mail Address
            and/or Password."
        """

        login_page = Login(driver)
        login_page.signIn_noemail('12345')
        error_message = login_page.message()
        assert "Warning: No match for E-Mail Address and/or Password." in error_message

    def test_signIn_empty(self,driver):
        """
        Test case for signing in with empty credentials.
        This test verifies that attempting to sign in with empty email and password
        fields results in the appropriate error message being displayed.
        Args:
            driver (WebDriver): The WebDriver instance used to interact with the web page.
        Asserts:
            The error message contains the text "Warning: No match for E-Mail Address and/or Password."
        """

        login_page = Login(driver)
        login_page.signIn('','')
        error_message = login_page.message()
        assert "Warning: No match for E-Mail Address and/or Password." in error_message
    
    def test_signIn_not_exist(self,driver):
        """
        Test case for attempting to sign in with a non-existent user.
        This test verifies that the appropriate error message is displayed when 
        trying to sign in with an email and password that do not match any existing 
        user account.
        Args:
        self: Instance of the test class.
        driver: WebDriver instance used to interact with the web page.
        Steps:
        1. Initialize the login page with the provided WebDriver.
        2. Attempt to sign in using a non-existent email and password.
        3. Retrieve the error message displayed on the login page.
        4. Assert that the error message contains the expected warning text.
        Expected Result:
        The error message should contain the text "Warning: No match for E-Mail 
        Address and/or Password."
        """

        login_page = Login(driver)
        login_page.signIn('abc@gmail.com','12345')
        error_message = login_page.message()
        assert "Warning: No match for E-Mail Address and/or Password." in error_message
    
    def test_logOut(self,driver):
        """
        Test the logout functionality of the application.
        This test will:
        1. Instantiate the Login page object.
        2. Sign in using the provided credentials.
        3. Perform the logout action.
        4. Assert that the current URL contains "account/logout" to verify successful logout.
        Args:
        driver (WebDriver): The WebDriver instance used to interact with the web application.
        """

        login_page = Login(driver)
        login_page.signIn('aaa@gmail.com','12345')
        login_page.logout()
        assert "account/logout" in login_page.get_current_url()
    
