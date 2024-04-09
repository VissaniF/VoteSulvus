import unittest
from selenium import webdriver
from login_page import LoginPage
import time

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://web.wowsulvus.com/login")
        self.login_page = LoginPage(self.driver)

    def test_successful_login(self):
        self.login_page.enter_username("puancito")
        self.login_page.enter_password("puancito")
        self.login_page.click_login_button()
        time.sleep(2)

    def test_votar_pag(self):
        self.login_page.enter_username("puancito")
        self.login_page.enter_password("puancito")
        self.login_page.click_login_button()
        time.sleep(2)
        self.login_page.boton_votar()
        time.sleep(3)
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
