from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.search import Search
import pytest
from driver.driver import Driver

from pages.addtocart import AddToCart
import time
class TestAddToCart(Driver):
    def test_add_to_cart_single(self,driver):
        """
        Test add to cart single product
        Steps:
            1. Open the browser
            2. Add a product to cart
            Expected results:
            The notification contains 'Success: You have added iMac to your shopping cart!'
            """
        add = AddToCart(driver)
        add.add_to_cart_single(driver)
        time.sleep(3)
        noti = driver.find_element(By.XPATH,"/html/body/div").text
        assert "Success: You have added iMac to your shopping cart!" in noti
    
    def test_add_many_products(self,driver):
        """
        Test add many products to cart

        Steps:
            1. Open the browser
            2. Add multiple products to cart
            3. Go to shopping cart
        Expected results:
            The products should be displayed in the shopping cart.
        """
        add = AddToCart(driver)
        products = ["iMac", "MacBook", "iPhone"]
        for product in products:
            add.add_to_cart_by_name(driver, product)
            time.sleep(1)
        time.sleep(3)
        
        add.go_shopping_cart()

        for product in products:
            assert driver.find_element(By.XPATH, f"//a[contains(text(), '{product}')]"), f"{product} not found in cart"
    
    def test_add_to_cart_zero(self,driver):
        """
        Test add to cart with quantity 0
        Steps:
            1. Open the browser
            2. Add a product to cart with quantity 0
            Expected results:
            The notification contains 'Error: You must enter a valid quantity'
            """
        add = AddToCart(driver)
        add.add_to_cart_zero(driver)
        time.sleep(3)
        noti = driver.find_element(By.XPATH,"/html/body/div").text
        assert "Error: You must enter a valid quantity" in noti

         
    
