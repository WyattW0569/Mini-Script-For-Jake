import pyautogui
import keyboard
import time
import threading

while not keyboard.is_pressed('k'):
    time.sleep(0.01)

def spaceHit():
    while not keyboard.is_pressed('z'):
        pyautogui.keyDown('space')
        time.sleep(0.01)
        pyautogui.keyUp('space')

thread = threading.Thread(target=spaceHit)
thread.start()

isLeft = True
last_k_press = time.time()

while not keyboard.is_pressed('z'):
    current_time = time.time()
    
    if keyboard.is_pressed('k') and (current_time - last_k_press > 0.2):
        isLeft = not isLeft
        last_k_press = current_time
        time.sleep(0.1)

    if isLeft:
        pyautogui.keyDown('a')
        #pyautogui.keyDown('space')
        pyautogui.keyUp('d')
       # pyautogui.keyUp('space')
    else:
        pyautogui.keyDown('d')
       # pyautogui.keyDown('space')
        pyautogui.keyUp('a')
       # pyautogui.keyUp('space')

    time.sleep(0.01)

pyautogui.keyUp('a')
pyautogui.keyUp('d')
pyautogui.keyUp('space')