from ast import While
from random import randint
from time import sleep
from pip import main
import pydirectinput
import pyautogui
from  datetime import datetime
import pandas as pd
import threading
import keyboard

def AutoBuff():
    pydirectinput.keyDown("c")
    sleep(2)
    pydirectinput.keyDown("d")
    sleep(2)
    pydirectinput.keyDown("v")
    sleep(3)
    pydirectinput.keyDown("n")
    sleep(3)
        

if __name__ == '__main__':
    sleep(3)
    auto_click=False
    while True:
        if keyboard.is_pressed("="):
            pydirectinput.keyUp('a')
            auto_click= not auto_click
            print(f"auto click = {auto_click}")
            sleep(0.5)
        if keyboard.is_pressed("0"):
            print(f"buffing...")
            AutoBuff()
        if auto_click:
                pydirectinput.keyDown('a')
                
        
