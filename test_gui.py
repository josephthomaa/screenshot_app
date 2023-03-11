import pyautogui
import os
import time
path = r"C:\Program Files\Hola\app\hola.exe"
os.system('start "" "' + path+ '"')

print(pyautogui.position())
print(pyautogui.size())
print("click1")
pyautogui.click(x=800, y=1057, clicks=1, interval=2, button='left')
time.sleep(5)
pyautogui.click(x=538, y=349, clicks=1, interval=2, button='left')
time.sleep(30)
pyautogui.click(x=800, y=1057, clicks=1, interval=2, button='right')
time.sleep(2)
pyautogui.click(x=787, y=1008, clicks=1, interval=2, button='left')
# print("click2")
# pyautogui.click(x=800, y=1057, clicks=1, interval=2, button='left')
# time.sleep(2)
# print("click3")
# pyautogui.click(x=800, y=1057, clicks=1, interval=2, button='left')
# time.sleep(10)
# pyautogui.click(x=515, y=356, clicks=1, interval=2, button='left')

