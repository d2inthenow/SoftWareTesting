from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.login import Login
import time


class DataValidation:
    def __init__(self,driver):
        self.driver = driver
    
    def validate_changepassword(self,newpassword,confirmpassword):
        self.driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/ul[1]/li[2]/a").click()
        self.driver.find_element(By.NAME,"password").send_keys(newpassword)
        self.driver.find_element(By.NAME,"confirm").send_keys(confirmpassword)
        self.driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/form/div/div[2]/button").click()
        time.sleep(2)
    
    def validate_quantity(self):
        product_items = self.driver.find_elements(By.CSS_SELECTOR, ".product-thumb")
        self.driver.execute_script("arguments[0].scrollIntoView();", product_items[0])
        time.sleep(3)
        self.driver.find_element(By.LINK_TEXT, "MacBook").click()
        time.sleep(5)
        
        

