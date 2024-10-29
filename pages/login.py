from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Login:
    def __init__(self,driver):
        self.driver = driver

    def signIn(self,email,password):
        self.driver.get("http://localhost/opencart/")
        self.driver.find_element(By.XPATH, "/html/body/nav/div/div[2]/ul/li[2]/div/a/span").click()
        self.driver.find_element(By.XPATH, "/html/body/nav/div/div[2]/ul/li[2]/div/ul/li[2]/a").click()
        self.driver.find_element(By.ID, "input-email").send_keys(email)
        self.driver.find_element(By.ID, "input-password").send_keys(password)
        self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div[2]/div/form/div[3]/button").click()
        time.sleep(2)
    
    def signIn_nopassword(self,email):
        self.driver.get("http://localhost/opencart/")
        self.driver.find_element(By.XPATH, "/html/body/nav/div/div[2]/ul/li[2]/div/a/span").click()
        self.driver.find_element(By.XPATH, "/html/body/nav/div/div[2]/ul/li[2]/div/ul/li[2]/a").click()
        self.driver.find_element(By.ID, "input-email").send_keys(email)
        self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div[2]/div/form/div[3]/button").click()
        time.sleep(2)
    
    def signIn_noemail(self,password):
        self.driver.get("http://localhost/opencart/")
        self.driver.find_element(By.XPATH, "/html/body/nav/div/div[2]/ul/li[2]/div/a/span").click()
        self.driver.find_element(By.XPATH, "/html/body/nav/div/div[2]/ul/li[2]/div/ul/li[2]/a").click()
        self.driver.find_element(By.ID, "input-password").send_keys(password)
        self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div[2]/div/form/div[3]/button").click()
        time.sleep(2)

    def logout(self):
        self.driver.find_element(By.XPATH, "/html/body/nav/div/div[2]/ul/li[2]/div/a/span").click()
        self.driver.find_element(By.XPATH, "/html/body/nav/div/div[2]/ul/li[2]/div/ul/li[5]/a").click()
        time.sleep(2)
        
    def get_current_url(self):
        return self.driver.current_url
    
    def message(self):
        return self.driver.find_element(By.XPATH, "/html/body/div/dirv").text
    
