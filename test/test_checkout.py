from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.search import Search
import time
from driver.driver import Driver
from pages.login import Login
from pages.checkout import Checkout
from pages.addtocart import AddToCart

class TestCheckOut(Driver):
    def test_checkout_no_login_guest(self,driver):
        """
        Test checkout without login as guest
        
        Steps:
            1. Open the browser
            2. Add a product to cart
            3. Go to checkout page
            4. Fill in the form
            5. Click on Continue button
            6. Choose shipping method
            7. Choose payment method
            8. Confirm the order
            Expected results:
            The current url contains 'checkout/success'
            
            """
        add = AddToCart(driver)
        add.add_to_cart_single(driver)
        time.sleep(3)
        check = Checkout(driver)
        time.sleep(4)
        
        check.checkout_no_login_guest("Johnaaa", "Doae","john.doae@example.com",
                                 "Example aaCompany", "123aa Example St",
                                "Apt 4Baa","Example Cityaa","12345",
                                "United Kingdom","Devon")
        check.input_wish()
        check.btn_continue()
        check.shipping_method()
        check.payment_method_and_comment()
        check.confirm_order()
        noti = check.get_current_url()
        assert "checkout/succes" in noti

    def test_checkout_no_login_register(self,driver):
        """
        Test checkout without login as guest

        Steps:
            1. Open the browser
            2. Add a product to cart
            3. Go to checkout page
            4. Fill in the form
            5. Click on Continue button
            6. Choose shipping method
            7. Choose payment method
            8. Confirm the order
            Expected results:
            The current url contains 'checkout/success'
            
            """
        add = AddToCart(driver)
        add.add_to_cart_single(driver)
        time.sleep(3)
        check = Checkout(driver)
        time.sleep(4)
        
        check.checkout_no_login_register("Duong", "To","tommy.phaam@example.com",
                                 "Example aaCompany", "123aa Example St",
                                "Apt 4Baa","Example Cityaa","12345",
                                "Thailand","Bangkok")
        check.input_wish()
        check.input_privacy()
        check.btn_continue()
        check.shipping_method()
        check.payment_method_and_comment()
        check.confirm_order()
        noti = check.get_current_url()
        assert "checkout/succes" in noti



    def test_check_login(self,driver):
        """
        Test checkout with login

        Steps:
            1. Open the browser
            2. Login
            3. Add a product to cart
            4. Go to checkout page
            5. Fill in the form
            6. Click on Continue button
            7. Choose shipping method
            8. Choose payment method
            9. Confirm the order
            Expected results:
            The current url contains 'checkout/success'
            """
        login_page = Login(driver)
        login_page.signIn("aaa@gmail.com","12345")
        time.sleep(1)
        add = AddToCart(driver)
        add.add_to_cart_single(driver)
        time.sleep(3)
        check = Checkout(driver)
        time.sleep(4)
        
        check.checkout_login("Johnaaa", "Doae","john.doae@example.com",
                                 "Example aaCompany", "123aa Example St",
                                "Apt 4Baa","Example Cityaa","12345",
                                "United Kingdom","Devon")
        check.btn_continue_login()
        check.shipping_method()
        check.payment_method_and_comment_login()
        check.confirm_order()
        noti = check.get_current_url()
        assert "checkout/succes" in noti
        
    def test_checkout_empty(self,driver):
        """
        Test checkout with empty cart

        Steps:
            1. Open the browser
            2. Go to checkout page
            Expected results:
            The message contains 'Your shopping cart is empty!'
            
            """
        check = Checkout(driver)
        check.go_checkout()
        time.sleep(1)
        noti = driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/p").text
        assert "Your shopping cart is empty!" in noti
