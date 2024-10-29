from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Navigation:
    def __init__(self,driver):
        self.driver = driver

    def go_to_register(self):
        self.driver.get("http://localhost/opencart/")
        self.driver.find_element(By.XPATH, "/html/body/nav/div/div[2]/ul/li[2]/div/a/span").click()
        self.driver.find_element(By.XPATH, "/html/body/nav/div/div[2]/ul/li[2]/div/ul/li[1]/a").click()
        time.sleep(2)

    def go_to_login(self):
        self.driver.get("http://localhost/opencart/")
        self.driver.find_element(By.XPATH, "/html/body/nav/div/div[2]/ul/li[2]/div/a/span").click()
        self.driver.find_element(By.XPATH, "/html/body/nav/div/div[2]/ul/li[2]/div/ul/li[2]/a").click()
        time.sleep(2)

    def go_to_shoppingcart(self):
        self.driver.get("http://localhost/opencart/")
        self.driver.find_element(By.XPATH, "/html/body/nav/div/div[2]/ul/li[4]/a/span").click()
        time.sleep(2)

    def go_to_wishlist(self):
        self.driver.find_element(By.XPATH, "/html/body/nav/div/div[2]/ul/li[3]/a/span").click()
        time.sleep(2)

    def go_to_checkout(self):
        self.driver.find_element(By.XPATH, "/html/body/nav/div/div[2]/ul/li[5]/a/span").click()
        time.sleep(2)
    
    def go_to_desktops_pc(self):
        self.driver.get("http://localhost/opencart/")
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[1]/a").click()
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[1]/div/div/ul/li[1]/a").click()
        time.sleep(2)
    
    def go_to_desktops_mac(self):
        self.driver.get("http://localhost/opencart/")
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[1]/a").click()
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[1]/div/div/ul/li[2]/a").click()
        time.sleep(2)

    def go_to_desktops_all(self):
        self.driver.get("http://localhost/opencart/")
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[1]/a").click()
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[1]/div/a").click()
        time.sleep(2)
    
    def go_to_laptopsandnotebooks_mac(self):
        self.driver.get("http://localhost/opencart/")
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[2]/a").click()
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[2]/div/div/ul/li[1]/a").click()
        time.sleep(2)
    
    def go_to_laptopsandnotebooks_windows(self):
        self.driver.get("http://localhost/opencart/")
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[2]/a").click()
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[2]/div/div/ul/li[2]/a").click()
        time.sleep(2)

    def go_to_laptopsandnotebooks_all(self):
        self.driver.get("http://localhost/opencart/")
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[2]/a").click()
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[2]/div/a").click()
        time.sleep(2)
    
    def go_to_components_miceandtrackballs(self):
        self.driver.get("http://localhost/opencart/")
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[3]/a").click()
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[3]/div/div/ul/li[1]/a").click()
        time.sleep(2)
    
    def go_to_components_monitors(self):
        self.driver.get("http://localhost/opencart/")
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[3]/a").click()
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[3]/div/div/ul/li[2]/a").click()
        time.sleep(2)

    def go_to_components_printers(self):
        self.driver.get("http://localhost/opencart/")
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[3]/a").click()
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[3]/div/div/ul/li[3]/a").click()
        time.sleep(2)
    
    def go_to_components_scanners(self):
        self.driver.get("http://localhost/opencart/")
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[3]/a").click()
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[3]/div/div/ul/li[4]/a").click()
        time.sleep(2)
    
    def go_to_components_webcams(self):
        self.driver.get("http://localhost/opencart/")
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[3]/a").click()
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[3]/div/div/ul/li[5]/a").click()
        time.sleep(2)
    
    def go_to_components_all(self):
        self.driver.get("http://localhost/opencart/")
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[3]/a").click()
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[3]/div/a").click()
        time.sleep(2)
    
    def go_to_tablets_ipads(self):
        self.driver.get("http://localhost/opencart/")
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[4]/a").click()
        time.sleep(2)
    
    def go_to_software(self):
        self.driver.get("http://localhost/opencart/")
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[5]/a").click()
        time.sleep(2)
    
    def go_to_phonesandPDAs(self):
        self.driver.get("http://localhost/opencart/")
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[6]/a").click()
        time.sleep(2)
    
    def go_to_cameras(self):
        self.driver.get("http://localhost/opencart/")
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[7]/a").click()
        time.sleep(2)
    
    def go_to_mp3players_all(self):
        self.driver.get("http://localhost/opencart/")
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[8]/a").click()
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[8]/div/a").click()
        time.sleep(2)

    def get_current_url(self):
        return self.driver.current_url

