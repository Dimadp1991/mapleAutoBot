from ast import While
from random import randint
from time import sleep
from pip import main
import pydirectinput
from  datetime import datetime
import pandas as pd
import keyboard
import threading

 

def AutoBuff():
    pydirectinput.keyDown("shift")
    sleep(2)
    pydirectinput.keyDown("c")
    sleep(2)
    pydirectinput.keyDown("v")
    sleep(2)
    pydirectinput.keyDown("n")
    sleep(2)

def MakeCombo(side):
    pydirectinput.keyDown("down")
    pydirectinput.keyUp("down")
    pydirectinput.keyDown(side)
    pydirectinput.keyUp(side)
    pydirectinput.keyDown("a")
    pydirectinput.keyUp("a")



def AutoSell():
    pydirectinput.keyDown("enter")
    sleep(0.5)
    pydirectinput.keyDown("up")
    sleep(0.5)
    pydirectinput.keyUp("up")
    pydirectinput.keyDown("enter")
    sleep(0.5)
    pydirectinput.keyDown("enter")
    sleep(0.5)
    pydirectinput.keyUp("enter")

def press_button(key):
    pydirectinput.keyDown(key=key)
    sleep(0.5)
    pydirectinput.keyUp(key=key)

def fast_step(side,how_many):
    pydirectinput.keyDown(side)
    sleep(how_many)
    pydirectinput.keyUp(side)
    pydirectinput.keyDown("left" if side == "right" else "right" )
    pydirectinput.keyUp("left" if side == "right" else "right" )
if __name__ == '__main__':
    sleep(3)
    random_int=0
    while True:
        sleep(3)
        AutoBuff()
        AutoSell()
        run_auto_player=True
        current_time=datetime.now()
        current_two = current_time + pd.DateOffset(minutes=3)
        interval_side = current_time + pd.DateOffset(seconds=20)
        interval_step = current_time + pd.DateOffset(seconds=3)
        while datetime.now()< current_two:
            if datetime.now() >= interval_side:
                random_int+=1
                interval_side = datetime.now() + pd.DateOffset(seconds=20)
                MakeCombo("left" if random_int % 2 == 0 else "right")
            if datetime.now() > interval_step:
                fast_step("left" if random_int % 2 == 0 else "right",1.3)
                interval_step = datetime.now() + pd.DateOffset(seconds=3)
                

            pydirectinput.keyDown("a")
            pydirectinput.keyUp("a")
            if keyboard.is_pressed("="):
                sleep(0.5)
                while True:
                    if keyboard.is_pressed("="):
                        sleep(0.5)
                        break

