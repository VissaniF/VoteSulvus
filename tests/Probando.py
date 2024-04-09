import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestYopmailLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_login_and_write_message(self):
        self.driver.get("https://www.yopmail.com")
        correo_electronico = self.driver.find_element(By.ID, "login")
        correo_electronico.send_keys("francotest@yopmail.com")
        correo_electronico.send_keys(Keys.ENTER)
        time.sleep(5)
        self.assertIn("Buzón de Correos", self.driver.title)

        celda_para_escribir = self.driver.find_element(By.ID, "msgbody")
        celda_para_escribir.send_keys("Hola este es un mensaje de prueba con Selenium")

if __name__ == "__main__":
    unittest.main()
