import pyautogui
import time
pyautogui.PAUSE = 0.5

def baixar_Provas():
    pyautogui.click(x=890, y=18)
#     pyautogui.click(x=1484, y=690)
    
#     for i in range(2): #range depende da quantidade de fotos tiradas
#         pyautogui.click(x=1830, y=117)
#         pyautogui.click(x=1711, y=239)
#         pyautogui.click(x=1869, y=540)


def Entrar_No_I_lovePdf():
    pyautogui.click(x=366, y=20)
    pyautogui.click(x=1659, y=738)
    pyautogui.click(x=949, y=344)

# def selecionar_Fotos_Na_Area_de_Trabalho:

def Mover_Fotos_Para_I_love_Pdf():
    pyautogui.moveTo(177,126)
    time.sleep(1)
    pyautogui.dragTo(932,414, duration=1.0)
    pyautogui.click()
    pyautogui.click(776,505)

    pyautogui.moveTo(x=1256, y=600)
    time.sleep(1)
    pyautogui(x=222, y=345, duration=1.0)






