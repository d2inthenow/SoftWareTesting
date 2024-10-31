from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.search import Search
from pages.responsive import Responsive
import time
from driver.driver import Driver

class TestEesponsive(Driver):
    def test_desktop_view_layout(self, driver):
        """
        Test the layout of the website on desktop view
        
        Steps:
            1. Open the browser
            2. Check the header and footer
        Expected results:
            Header and footer should be displayed on desktop view.
        """
        driver.get("http://localhost/opencart/")
        responsive = Responsive(driver)
        responsive.set_viewport_size(1920, 1080)
        
        assert responsive.is_header_displayed(), "Header should be displayed on desktop view."
        assert responsive.is_footer_displayed(), "Footer should be displayed on desktop view."

    def test_mobile_view_layout(self, driver):
        """
        Test the layout of the website on mobile view

        Steps:
            1. Open the browser
            2. Check the hamburger menu and footer
        Expected results:
            Hamburger menu and footer should be displayed on mobile view.
        """
        driver.get("http://localhost/opencart/")
        responsive = Responsive(driver)
        responsive.set_viewport_size(375, 667)  # Common mobile size
        
        assert responsive.is_hamburger_menu_displayed(), "Hamburger menu should be displayed on mobile view."
        responsive.click_hamburger_menu()  # Open the menu if needed
        assert responsive.is_footer_displayed(), "Footer should be visible on mobile view."

    def test_tablet_view_layout(self, driver):
        """
        Test the layout of the website on tablet view

        Steps:
            1. Open the browser
            2. Check the header and footer
        Expected results:
            Header and footer should be displayed on tablet view.
        """
        driver.get("http://localhost/opencart/")
        responsive = Responsive(driver)
        responsive.set_viewport_size(768, 1024)  # Common tablet size
        
        assert responsive.is_header_displayed(), "Header should be displayed on tablet view."
        assert responsive.is_footer_displayed(), "Footer should be displayed on tablet view."

    def test_touch_friendly_buttons(self, driver):
        """
        Test the accessibility of the Add to Cart button on mobile view
        Steps:
            1. Open the browser
            2. Check the Add to Cart button
        Expected results:
            Add to Cart button should be accessible on mobile view.
        """
        driver.get("http://localhost/opencart/")
        responsive = Responsive(driver)
        responsive.set_viewport_size(375, 667)
        
        assert responsive.is_add_to_cart_button_displayed(), "Add to Cart button should be accessible on mobile view."
