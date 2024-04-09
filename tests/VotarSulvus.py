from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

USUARIO="Vissani"
CONTRASEÑA="Franco1737."
driver = webdriver.Chrome()


driver.get("https://web.wowsulvus.com/")


wait = WebDriverWait(driver, 10)
campo_busqueda = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#login")))


if campo_busqueda.is_displayed():
    
    campo_busqueda.click()
else:
    print("El elemento de búsqueda no está visible.")

time.sleep(3)
campo_usuario = driver.find_element("name", "username")
campo_contraseña = driver.find_element("name", "password")

campo_usuario.send_keys(USUARIO)
campo_contraseña.send_keys(CONTRASEÑA)
campo_contraseña.send_keys(Keys.ENTER)
time.sleep(3)
boton_votar = driver.find_element("id", "vote")
boton_votar.click()
time.sleep(3)

#establezco ventana principal para que no se dirija a la emergente
ventana_principal = driver.window_handles[0]


votar1 = driver.find_element(By.CSS_SELECTOR, "#body > div > div > div > div.vote-page > div.container_3.account-wide > ul > li:nth-child(1)")

votar1.click()
time.sleep(2)

driver.switch_to.window(ventana_principal)

votar2 = driver.find_element(By.CSS_SELECTOR, "#body > div > div > div > div.vote-page > div.container_3.account-wide > ul > li:nth-child(2)")
votar2.click()
time.sleep(2)

driver.switch_to.window(ventana_principal)

votar3 = driver.find_element(By.CSS_SELECTOR, "#body > div > div > div > div.vote-page > div.container_3.account-wide > ul > li:nth-child(3)")
votar3.click()
time.sleep(2)

driver.switch_to.window(ventana_principal)

votar4 = driver.find_element(By.CSS_SELECTOR, "#body > div > div > div > div.vote-page > div.container_3.account-wide > ul > li:nth-child(4)")
votar4.click()
time.sleep(2)


time.sleep(20)
driver.quit()
