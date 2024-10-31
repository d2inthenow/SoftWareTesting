from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

class Responsive():
    def __init__(self, driver):
        self.driver = driver

    def set_viewport_size(self, width, height):
        self.driver.set_window_size(width, height)
        time.sleep(1)  # Allow time for elements to adjust

    def is_header_displayed(self):
        return self.driver.find_element(By.XPATH, "/html/body/header/div").is_displayed()

    def is_footer_displayed(self):
        self.scroll(self.driver.find_element(By.XPATH, "/html/body/footer/div"))
        return self.driver.find_element(By.XPATH, "/html/body/footer/div").is_displayed()   

    def is_hamburger_menu_displayed(self):
        return self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/button").is_displayed()

    def click_hamburger_menu(self):
        self.scroll(self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/button"))
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/button").click()
    
    def scroll(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)

    def is_add_to_cart_button_displayed(self):
        # Assuming the page already has a product to add
        add_to_cart_buttons = self.driver.find_elements(By.XPATH, "/html/body/main/div[2]/div/div/div[2]/div[2]/div/div[2]/form/div/button[1]")
        return len(add_to_cart_buttons) > 0
