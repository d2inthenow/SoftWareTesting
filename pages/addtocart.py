from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from pages.search import Search

class AddToCart():
    def __init__(self,driver):
        self.driver = driver

    def add_to_cart_single(self,driver):
        search_data = Search(driver)
        search_data.search('iMac')
        self.scroll(self.driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div[5]/div/div/div[2]/form/div/button[1]"))
        self.driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div[5]/div/div/div[2]/form/div/button[1]").click()
        
    def add_to_cart_by_name(self,driver,product_name):
        search_data = Search(driver)
        search_data.search(product_name)
        self.scroll(self.driver.find_element(By.XPATH, "//button[@type='submit' and @title='Add to Cart']"))
        self.driver.find_element(By.XPATH, "//button[@type='submit' and @title='Add to Cart']").click()

    def add_to_cart_zero(self,driver):
        search_data = Search(driver)
        search_data.search('iMac')
        self.scroll(self.driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div[5]/div/div/div[2]/div/h4/a"))
        self.driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div[5]/div/div/div[2]/div/h4/a").click()
        self.driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div[1]/div[1]/div[2]/div[1]/form/div/input[1]").clear()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div[1]/div[1]/div[2]/div[1]/form/div/input[1]").send_keys('0')
        time.sleep(1)
        self.driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div[1]/div[1]/div[2]/div[1]/form/div/button").click()

    def go_shopping_cart(self):
        self.scroll(self.driver.find_element(By.XPATH,"/html/body/nav/div/div[2]/ul/li[4]/a/span"))
        self.driver.find_element(By.XPATH,"/html/body/nav/div/div[2]/ul/li[4]/a/span").click()
        time.sleep(1)
        

    def scroll(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)

    def get_current_url(self):
        return self.driver.current