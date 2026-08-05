import pyautogui
import time

# Intervalo de 0,5 segundo entre cada comando
pyautogui.PAUSE = 0.5

# Abre o menu Iniciar
pyautogui.press("win")

# Espera o menu abrir
time.sleep(1)

# Pesquisa pelo Google Chrome
pyautogui.write("chrome", interval=0.1)

# Abre o programa
pyautogui.press("enter")

# Aguarda o Chrome carregar
time.sleep(3)