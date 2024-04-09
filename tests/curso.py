import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/text-box")

########selectores########
nombre = driver.find_element(By.CSS_SELECTOR, "#userName") 
mail = driver.find_element(By.CSS_SELECTOR, "#userEmail")
Current = driver.find_element(By.CSS_SELECTOR, "#currentAddress")
Permanent = driver.find_element(By.CSS_SELECTOR, "#permanentAddress")
Boton = driver.find_element(By.CSS_SELECTOR, "#submit")


########Escribir########
nombre.send_keys("Franco")
mail.send_keys("Franco@yopmail.com")
Current.send_keys("Este es un correo")
Permanent.send_keys("Este es un correo2")
driver.maximize_window()
Boton.click()




time.sleep(4)
driver.quit()