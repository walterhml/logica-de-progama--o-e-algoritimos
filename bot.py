import pyautogui 

pyautogui.PAUSE = 3

pyautogui.press("win")
pyautogui.write('login.xlsx')
pyautogui.press('backspace')
pyautogui.press('Enter')

pyautogui.click(x=812, y=684)
pyautogui.write('walter')
pyautogui.click(x=870, y=742)
pyautogui.write('84q8')
pyautogui.click(x=744, y=871)
pyautogui.click(x=1697, y=733)
pyautogui.click(x=945, y=739)


#descobrir valor de x e y da posição do mouse...
# import time

# time.sleep(5)
# x, y = pyautogui.position() 
# print(f'A posição atual do mouse é ({x}, {y})')