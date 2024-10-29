from selenium import webdriver
import pytest
class Driver:
    @pytest.fixture(scope="function")
    def driver(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(10) 
        yield driver
        driver.quit()