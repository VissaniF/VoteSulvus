import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class ejeusando_unitest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_by_xpath(self):
        driver = self.driver
        driver.get("http://www.google.com")
        search_by_xpath = driver.find_element(By.XPATH,"//*[@id='APjFqb']")
        search_by_xpath.send_keys("selenium", Keys.ARROW_DOWN)
   

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
