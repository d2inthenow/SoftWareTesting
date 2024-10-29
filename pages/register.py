from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Register:
    def __init__(self,driver):
        self.driver = driver

    def register(self,firstname,lastname,email,password):
        self.driver.get("http://localhost/opencart/")
        self.driver.find_element(By.XPATH, "/html/body/nav/div/div[2]/ul/li[2]/div/a/span").click()
        self.driver.find_element(By.XPATH, "/html/body/nav/div/div[2]/ul/li[2]/div/ul/li[1]/a").click()
        self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/form/fieldset[1]/div[1]/div/input").send_keys(firstname)
        self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/form/fieldset[1]/div[2]/div/input").send_keys(lastname)
        self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/form/fieldset[1]/div[3]/div/input").send_keys(email)
        self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/form/fieldset[2]/div/div/input").send_keys(password)
        self.scroll(self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/form/div/div/input"))
        time.sleep(2)

        if self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/form/div/div/input").is_enabled():
            self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/form/div/div/input").click()

        self.driver.find_element(By.XPATH,'/html/body/main/div[2]/div/div/form/div/button').click()
        time.sleep(2)

    def register_noClick_privacy_policy(self,firstname,lastname,email,password):
        self.driver.get("http://localhost/opencart/")
        self.driver.find_element(By.XPATH, "/html/body/nav/div/div[2]/ul/li[2]/div/a/span").click()
        self.driver.find_element(By.XPATH, "/html/body/nav/div/div[2]/ul/li[2]/div/ul/li[1]/a").click()
        self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/form/fieldset[1]/div[1]/div/input").send_keys(firstname)
        self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/form/fieldset[1]/div[2]/div/input").send_keys(lastname)
        self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/form/fieldset[1]/div[3]/div/input").send_keys(email)
        self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/form/fieldset[2]/div/div/input").send_keys(password)
        self.scroll(self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/form/div/div/input"))
        self.driver.find_element(By.XPATH,'/html/body/main/div[2]/div/div/form/div/button').click()
        time.sleep(2)

    def get_current_url(self):
        return self.driver.current_url
    
    def scroll(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)

    def message(self):
        return self.driver.find_element(By.XPATH, "").text