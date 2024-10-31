from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Search:
    def __init__(self,driver):
        self.driver = driver

    def search(self,enter):
        self.driver.get("http://localhost/opencart/")
        self.driver.find_element(By.NAME, "search")
        self.driver.find_element(By.NAME, "search").clear()
        self.driver.find_element(By.NAME, "search").send_keys(enter)
        self.driver.find_element(By.XPATH,"/html/body/header/div/div/div[2]/div/button").click()
        time.sleep(2)

    def get_current_url(self):
        return self.driver.current_url
    
    def message(self):
        return self.driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/p").text