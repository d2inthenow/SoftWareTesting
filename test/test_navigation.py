from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.navigation import Navigation
import pytest
from driver.driver import Driver
import time
from pages.login import Login

class TestNavigation(Driver):
    def test_register(self,driver):
        navigation = Navigation(driver)
        navigation.go_to_register()
        assert "account/register" in navigation.get_current_url()
    
    def test_login(self,driver):
        navigation = Navigation(driver)
        navigation.go_to_login()
        assert "account/login" in navigation.get_current_url()
    
    def test_shoppingcart(self,driver):
        navigation = Navigation(driver)
        navigation.go_to_shoppingcart()
        assert "checkout/cart" in navigation.get_current_url()
    
    def test_wishlist(self,driver):
        login_page = Login(driver)
        login_page.signIn('aaa@gmail.com','12345')
        navigation = Navigation(driver)
        navigation.go_to_wishlist()
        assert "account/wishlist" in navigation.get_current_url()

    def test_checkout(self,driver):
        login_page = Login(driver)
        login_page.signIn('aaa@gmail.com','12345')
        navigation = Navigation(driver)
        navigation.go_to_checkout()
        assert "checkout/cart" in navigation.get_current_url()
    
    def test_desktops_pc(self,driver):
        navigation = Navigation(driver)
        navigation.go_to_desktops_pc()
        assert "product/category&language=en-gb&path=20_26" in navigation.get_current_url()
    
    def test_desktops_mac(self,driver):
        navigation = Navigation(driver)
        navigation.go_to_desktops_mac()
        assert "product/category&language=en-gb&path=20_27" in navigation.get_current_url()
    
    def test_desktops_all(self,driver):
        navigation = Navigation(driver)
        navigation.go_to_desktops_all()
        assert "product/category&language=en-gb&path=20" in navigation.get_current_url()
    
    def test_laptopsandnotebooks_mac(self,driver):
        navigation = Navigation(driver)
        navigation.go_to_laptopsandnotebooks_mac()
        assert "route=product/category&language=en-gb&path=18_46" in navigation.get_current_url()
    
    def test_laptopsandnotebooks_windows(self,driver):
        navigation = Navigation(driver)
        navigation.go_to_laptopsandnotebooks_windows()
        assert "product/category&language=en-gb&path=18_45" in navigation.get_current_url()
    
    def test_laptopsandnotebooks_all(self,driver):
        navigation = Navigation(driver)
        navigation.go_to_laptopsandnotebooks_all()
        assert "product/category&language=en-gb&path=18" in navigation.get_current_url()

    def test_components_miceandtrackballs(self,driver):
        navigation = Navigation(driver)
        navigation.go_to_components_miceandtrackballs()
        assert "product/category&language=en-gb&path=25_29" in navigation.get_current_url()

    def test_components_monitors(self,driver):
        navigation = Navigation(driver)
        navigation.go_to_components_monitors()
        assert "product/category&language=en-gb&path=25_28" in navigation.get_current_url()

    def test_components_printers(self,driver):
        navigation = Navigation(driver)
        navigation.go_to_components_printers()
        assert "product/category&language=en-gb&path=25_30" in navigation.get_current_url()

    def test_components_scanners(self,driver):
        navigation = Navigation(driver)
        navigation.go_to_components_scanners()
        assert "product/category&language=en-gb&path=25_31" in navigation.get_current_url()
    
    def test_components_webcams(self,driver):
        navigation = Navigation(driver)
        navigation.go_to_components_webcams()
        assert "product/category&language=en-gb&path=25_32" in navigation.get_current_url()

    def test_tablets(self,driver):
        navigation = Navigation(driver)
        navigation.go_to_tablets_ipads()
        assert "product/category&language=en-gb&path=57" in navigation.get_current_url()
    
    def test_software(self,driver):
        navigation = Navigation(driver)
        navigation.go_to_software()
        assert "product/category&language=en-gb&path=17" in navigation.get_current_url()
    
    def test_phones(self,driver):
        navigation = Navigation(driver)
        navigation.go_to_phonesandPDAs()
        assert "product/category&language=en-gb&path=24" in navigation.get_current_url()
    
    def test_cameras(self,driver):
        navigation = Navigation(driver)
        navigation.go_to_cameras()
        assert "product/category&language=en-gb&path=33" in navigation.get_current_url()
    
    def test_mp3players(self,driver):
        navigation = Navigation(driver)
        navigation.go_to_mp3players_all()
        assert "product/category&language=en-gb&path=34" in navigation.get_current_url()

