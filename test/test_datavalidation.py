from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.datavalidation import DataValidation
from pages.search import Search
from pages.login import Login
from driver.driver import Driver
import time 
import random


class TestDataValidation(Driver):
    def test_validate_changepassword(self,driver):
        """
        Test case for validating the change password functionality.
        This test performs the following steps:
        1. Logs in to the application using the provided credentials.
        2. Navigates to the change password section.
        3. Attempts to change the password with the provided new password.
        4. Verifies that the success notification is displayed indicating the password has been updated.
        Args:
            driver (WebDriver): The WebDriver instance used to interact with the web application.
        """

        login_page = Login(driver)
        login_page.signIn('nabee2412@gmail.com','12345')
        data_validation = DataValidation(driver)
        data_validation.validate_changepassword('123456','123456')
        noti = driver.find_element(By.XPATH,"/html/body/main/div[2]/div[1]").text
        assert "Success: Your password has been successfully updated." in noti
    
    def test_validate_changepassword_exceed_the_limit(self,driver):
        """
        Test case for validating the change password functionality when the 
        new password exceeds the character limit.
        This test performs the following steps:
        1. Logs in to the application using valid credentials.
        2. Attempts to change the password to a value that exceeds the allowed limit.
        3. Verifies that the appropriate error message is displayed.
        Args:
            self: The instance of the test case class.
            driver: The WebDriver instance used to interact with the web application.
        Asserts:
            The error message "Password must be between 4 and 20 characters!" is displayed.
        """
        login_page = Login(driver)
        login_page.signIn('nabee2412@gmail.com','123456')
        data_validation = DataValidation(driver)
        data_validation.validate_changepassword('111','111')
        noti = driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/form/fieldset/div[1]/div/div").text
        assert "Password must be between 4 and 20 characters!" in noti

    def test_validate_multi_quantity(self,driver): 
        """
        Test the validation of multiple quantities in the shopping cart.
        This test performs the following steps:
        1. Searches for "macbook" using the search page.
        2. Validates the quantity input field.
        3. Clears the quantity input field and sets it to a random integer between 1 and 100.
        4. Retrieves the price of the item.
        5. Adds the item to the cart.
        6. Navigates to the shopping cart.
        7. Verifies that the total value in the cart matches the expected value based on the quantity and item price.
        Args:
            driver (WebDriver): The WebDriver instance used to interact with the web page.
        Asserts:
            The total value in the cart matches the expected formatted value.
        """
        
        search_page = Search(driver)
        search_page.search("macbook")
        data = DataValidation(driver)
        data.validate_quantity()
        
        quantity = driver.find_element(By.ID, "input-quantity")
        quantity.clear()

        random_integer = random.randint(1, 100)
        random_integer_str = str(random_integer)

        quantity.send_keys(random_integer_str)
        time.sleep(3)

        price = driver.find_element(By.CLASS_NAME, "price-new")
        numeric_value = float(price.text.replace("$", ""))

        driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div[1]/div[2]/div[1]/form/div/button").click()
        time.sleep(7)
        driver.find_element(By.XPATH,"/html/body/nav/div/div[2]/ul/li[4]/a/span").click()
        time.sleep(3)

        
        total_value = driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div[1]/div/table/tfoot/tr[4]/td[2]").text

        total = random_integer * numeric_value
        formatted_value = f"${total:,.2f}"

        time.sleep(2)
        assert total_value == formatted_value, f"Expected {formatted_value} but got {total_value}"


    
