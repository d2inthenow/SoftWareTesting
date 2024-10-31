from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.ui import Select

class Checkout():
    def __init__(self,driver):
        self.driver = driver
    
    def checkout_no_login_guest(self,firstname,lastname,email,company,address1,address2,city,postcode,country,region):
        self.scroll(self.driver.find_element(By.XPATH,"/html/body/nav/div/div[2]/ul/li[5]/a/span"))
        time.sleep(1)
        self.driver.find_element(By.XPATH,"/html/body/nav/div/div[2]/ul/li[5]/a/span").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div/div[1]/div/form/fieldset[1]/div[1]/div[1]/div[2]/input").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div/div[1]/div/form/fieldset[1]/div[2]/div[1]/input").send_keys(firstname)
        self.driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div/div[1]/div/form/fieldset[1]/div[2]/div[2]/input").send_keys(lastname)
        time.sleep(1)
        self.driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div/div[1]/div/form/fieldset[1]/div[2]/div[3]/input").send_keys(email)
        self.driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div/div[1]/div/form/fieldset[2]/div/div[1]/input").send_keys(company)
        time.sleep(1)
        self.driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div/div[1]/div/form/fieldset[2]/div/div[2]/input").send_keys(address1)
        self.driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div/div[1]/div/form/fieldset[2]/div/div[3]/input").send_keys(address2)
        time.sleep(1)
        self.driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div/div[1]/div/form/fieldset[2]/div/div[4]/input").send_keys(city)
        self.driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div/div[1]/div/form/fieldset[2]/div/div[5]/input").send_keys(postcode)
        self.scroll(self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div[1]/div/form/fieldset[2]/div/div[6]/select"))
        time.sleep(1)
        Select(self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div[1]/div/form/fieldset[2]/div/div[6]/select")).select_by_visible_text(country)
        Select(self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div[1]/div/form/fieldset[2]/div/div[7]/select")).select_by_visible_text(region)
        time.sleep(4)

    def checkout_no_login_register(self,firstname,lastname,email,company,address1,address2,city,postcode,country,region):
        self.scroll(self.driver.find_element(By.XPATH,"/html/body/nav/div/div[2]/ul/li[5]/a/span"))
        time.sleep(1)
        self.driver.find_element(By.XPATH,"/html/body/nav/div/div[2]/ul/li[5]/a/span").click()
        time.sleep(1)
        # self.driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div/div[1]/div/fieldset/div[1]/div[2]/input").click()
        # time.sleep(1)
        self.driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div/div[1]/div/form/fieldset[1]/div[2]/div[1]/input").send_keys(firstname)
        self.driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div/div[1]/div/form/fieldset[1]/div[2]/div[2]/input").send_keys(lastname)
        time.sleep(1)
        self.driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div/div[1]/div/form/fieldset[1]/div[2]/div[3]/input").send_keys(email)
        self.driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div/div[1]/div/form/fieldset[2]/div/div[1]/input").send_keys(company)
        time.sleep(1)
        self.driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div/div[1]/div/form/fieldset[2]/div/div[2]/input").send_keys(address1)
        self.driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div/div[1]/div/form/fieldset[2]/div/div[3]/input").send_keys(address2)
        time.sleep(1)
        self.driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div/div[1]/div/form/fieldset[2]/div/div[4]/input").send_keys(city)
        self.driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div/div[1]/div/form/fieldset[2]/div/div[5]/input").send_keys(postcode)
        self.scroll(self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div[1]/div/form/fieldset[2]/div/div[6]/select"))
        time.sleep(1)
        Select(self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div[1]/div/form/fieldset[2]/div/div[6]/select")).select_by_visible_text(country)
        Select(self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div[1]/div/form/fieldset[2]/div/div[7]/select")).select_by_visible_text(region)
        self.driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div/div[1]/div/form/div[1]/div[1]/fieldset/div/div/input").send_keys("12345")
        time.sleep(4)

    def checkout_login(self,firstname,lastname,email,company,address1,address2,city,postcode,country,region):
        self.scroll(self.driver.find_element(By.XPATH,"/html/body/nav/div/div[2]/ul/li[5]/a/span"))
        time.sleep(1)
        self.driver.find_element(By.XPATH,"/html/body/nav/div/div[2]/ul/li[5]/a/span").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div/div[1]/div/fieldset/div[1]/div[2]/input").click()
        time.sleep(1)
        # self.driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div/div[1]/div/form/fieldset[1]/div[1]/div[1]/div[2]/input").click()
        self.driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div/div[1]/div/fieldset/div[3]/form/div[1]/div[1]/input").send_keys(firstname)
        self.driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div/div[1]/div/fieldset/div[3]/form/div[1]/div[2]/input").send_keys(lastname)
        time.sleep(1)
        self.driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div/div[1]/div/fieldset/div[3]/form/div[1]/div[3]/input").send_keys(company)
        time.sleep(1)
        self.driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div/div[1]/div/fieldset/div[3]/form/div[1]/div[4]/input").send_keys(address1)
        self.driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div/div[1]/div/fieldset/div[3]/form/div[1]/div[5]/input").send_keys(address2)
        time.sleep(1)
        self.driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div/div[1]/div/fieldset/div[3]/form/div[1]/div[6]/input").send_keys(city)
        time.sleep(1)
        self.scroll(self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div[1]/div/fieldset/div[3]/form/div[2]/button"))
        time.sleep(1)
        self.driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div/div[1]/div/fieldset/div[3]/form/div[1]/div[7]/input").send_keys(postcode)
        time.sleep(1)
        Select(self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div[1]/div/fieldset/div[3]/form/div[1]/div[8]/select")).select_by_visible_text(country)
        Select(self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div[1]/div/fieldset/div[3]/form/div[1]/div[9]/select")).select_by_visible_text(region)
        time.sleep(1)

    def shipping_method(self):
        self.scroll(self.driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div/div[2]/div[1]/fieldset/div[1]/button"))
        self.driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div/div[2]/div[1]/fieldset/div[1]/button").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/form/div[1]/label").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/form/div[2]/button").click()
        time.sleep(1)

    def payment_method_and_comment(self):
        self.driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div/div[2]/div[2]/fieldset/div[1]/button").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[2]/form/div[1]/label").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[2]/form/div[2]/button").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div/div[2]/div[2]/div/textarea").send_keys("asdasd")
        time.sleep(1)

    def payment_method_and_comment_login(self):
        self.driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div/div[2]/div[2]/fieldset/div[1]/button").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[2]/form/div[1]/label").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[2]/form/div[2]/button").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div/div[2]/div[2]/div/textarea").send_keys("asdasd")
        time.sleep(1)
        self.scroll(self.driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div/div[2]/div[3]/div[2]/div/button"))
        time.sleep(2)

    def confirm_order(self):
        self.driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div/div[2]/div[3]/div[2]/div/button").click()
        time.sleep(1)

    def input_wish(self):
        self.driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div/div[1]/div/form/div[2]/div/div[1]/input").click()
        time.sleep(1)
    def btn_continue(self):
        self.driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div/div[1]/div/form/div[2]/div/button").click()
        time.sleep(4)

    def btn_continue_login(self):
        self.driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div/div[1]/div/fieldset/div[3]/form/div[2]/button").click()
        time.sleep(1)
        self.scroll(self.driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div/div[2]/div[1]/fieldset/div[1]/button"))
        time.sleep(4)

    def scroll(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)

    def input_privacy(self):
        self.driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div/div[1]/div/form/div[2]/div/div[2]/input").click()
        time.sleep(1)

    def go_checkout(self):
        self.driver.get("http://localhost/opencart/")
        self.driver.find_element(By.XPATH,"/html/body/nav/div/div[2]/ul/li[5]/a/span").click()
        


    def get_current_url(self):
        return self.driver.current_url
    
