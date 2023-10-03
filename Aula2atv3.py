from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time


navegador = Firefox()

url = "https://web.whatsapp.com/"

navegador.get(url)
time.sleep(30)
navegador.find_element(By.CLASS_NAME, "_1AHcd")
navegador.find_element(By.XPATH,"/html/body/div[1]/div/div/div[4]/div/div[2]/div[2]/div/div/div[11]").click()
texto = navegador.find_element(By.XPATH,"/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div[2]/div[1]")
time.sleep(4)
msg = 'Automação Whatsapp web Squad Fenix!'
for m in msg:
    texto.send_keys(m)

texto.send_keys(Keys.ENTER)




