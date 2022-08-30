from time import sleep
from pip import main
import pydirectinput
import pyautogui
from  datetime import datetime
import pandas as pd

def button_press(key,how_many=1):
    pydirectinput.keyDown(key)
    sleep(how_many)
    pydirectinput.keyUp(key)


if __name__ == '__main__':
    # position screen top right corner of the screen resolution 1920X1080
    # speed cap to 268
    sleep(2)
    while True:
        button_press('shift',1)
        button_press('t',1)
        pyautogui.click(x=1283,y=454)
        sleep(1)

        # button_press('down',1) #for party dojo option
        button_press('enter',1)
        # Point(x=1283, y=454) DOJO enterence 
        button_press(key='right',how_many=1)
        interval_shoot = datetime.now() + pd.DateOffset(minutes=0.9)
        while datetime.now()< interval_shoot:
            pydirectinput.keyDown('a')
        sleep(1)
        # Point(x=1369, y=229) DOJO out
        pyautogui.click(x=1369,y=229)
        sleep(1)
        button_press('y',1)
        button_press(key='right',how_many=1.85)
        sleep(1)
        button_press('up',1)
        button_press('up',1)
        sleep(1)



    # print(pyautogui.position())
    # sleep(3)