from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.search import Search
import pytest
from driver.driver import Driver

class TestSearch(Driver):
    def test_search(self,driver):
        """
        Test search with keyword 'macbook'
        Notes:
            Step 1: Open the browser
            Step 2: Search 'macbook'
            Step 3: Check the current url
        Expected results:
            The current url contains 'product/search&language=en-gb&search=macbook'
        """
        search_data = Search(driver)
        search_data.search('macbook')
        assert "product/search&language=en-gb&search=macbook" in search_data.get_current_url()
    
    def test_search_empty(self,driver):
        """
        Test search with empty keyword
        Notes:
            Step 1: Open the browser
            Step 2: Search ''
            Step 3: Check the current url
        Expected results:
            The current url contains 'product/search&language=en-gb'

        """
        search_data = Search(driver)
        search_data.search('')
        assert "product/search&language=en-gb" in search_data.get_current_url()
    
    def test_search_not_exist(self,driver):
        """
        Test search with keyword 'abc'
        Notes:
            Step 1: Open the browser
            Step 2: Search 'abc'
            Step 3: Check the message
        Expected results:
            The message contains 'There is no product that matches the search criteria.'
        """
        search_data = Search(driver)
        search_data.search('abc')
        assert "There is no product that matches the search criteria." in search_data.message()
    
    def test_search_sql_injection(self,driver):
        """
        Test search with keyword 'select * from users'
        Notes:
            Step 1: Open the browser
            Step 2: Search 'select * from users'
            Step 3: Check the message
        Expected results:
            The message contains 'There is no product that matches the search criteria.'
        """
        search_data = Search(driver)
        search_data.search('select * from users')
        assert "There is no product that matches the search criteria." in search_data.message()
    
    def test_validate_search_xss(self,driver):
        """
        Test search with keyword '<script>alert("hello duong")</script>'
        Notes:
            Step 1: Open the browser
            Step 2: Search '<script>alert("hello duong")</script>'
            Step 3: Check the message
        Expected results:
            The message contains 'There is no product that matches the search criteria.'
        """
        search_data = Search(driver)
        search_data.search('<script>alert("hello duong")</script>')
        assert "There is no product that matches the search criteria." in search_data.message()
    