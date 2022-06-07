from ast import While
from random import randint
from time import sleep
from pip import main
import pydirectinput
import pyautogui
from  datetime import datetime
import pandas as pd
import threading

 

def AutoBuff():
    pydirectinput.keyDown("t")
    sleep(2)


def fast_step(side,how_many):
    pydirectinput.keyDown(side)
    sleep(how_many)
    pydirectinput.keyUp(side)
    pydirectinput.keyDown("left" if side == "right" else "right" )
    pydirectinput.keyUp("left" if side == "right" else "right" )

def hold_a_key(key):
    while True:
        pydirectinput.keyDown(key)
        sleep(0.3)


        

if __name__ == '__main__':
    sleep(3)
    hold_a_key("a")