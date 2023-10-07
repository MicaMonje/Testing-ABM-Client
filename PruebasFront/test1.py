#from PruebasFront.funciones import funcionesGlobales
from selenium import webdriver
from selenium.webdriver.common.by  import By
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys




def testLogin1():
    global driver
    driver = webdriver.Chrome()
    driver.get("http://localhost:4200/")
    driver.maximize_window()
    
    nom = driver.find_element(By.XPATH, "//input[contains(@id,'name')]")
    nom.send_keys("Mina")
    ape = driver.find_element(By.XPATH, "//input[contains(@id,'lastName')]")
    ape.send_keys("zanco")
    fecha = driver.find_element(By.XPATH, "//input[contains(@nameid,'birthday')]")
    fecha.send_keys("22/08/1993")
    cuil = driver.find_element(By.XPATH, "//input[contains(@id,'CUIT')]")
    cuil.send_keys("27409271710")
    direccion = driver.find_element(By.XPATH, "//input[contains(@id,'address')]")
    direccion.send_keys("Calle san jose 927")
    celu = driver.find_element(By.XPATH, "//input[contains(@id,'telphone')]")
    celu.send_keys("154091675")
    mail = driver.find_element(By.XPATH, "//input[contains(@id,'email')]")
    mail.send_keys("mina.zanco@gmail.com")
    boton = driver.find_element(By.XPATH, "//button[contains(@id,'boton-registrar')]")
    boton.click
    
    
    time.sleep(3)
    

testLogin1()