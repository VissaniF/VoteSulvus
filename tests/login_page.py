from selenium.webdriver.common.by import By
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, 'username')
        self.password_input = (By.ID, 'password')
        self.login_button = (By.CSS_SELECTOR, '#body > div > div.container_3.account-wide > form > div:nth-child(3) > input[type=submit]')
        self.button_vote = (By.ID, 'vote')
        time.sleep(2)
    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()

    def boton_votar(self):
        self.driver.find_element(*self.button_vote).click()
