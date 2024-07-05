import pyautogui

pyautogui.PAUSE = 7 #isso significa antes do pyautogui executar cada comando, ele vai esperar dois segundos 



import time 
time.sleep(3) 
b = pyautogui.position()

print(b)
