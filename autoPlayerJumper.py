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
    pydirectinput.keyDown("c")
    sleep(3)
    pydirectinput.keyDown("v")
    sleep(3)
    pydirectinput.keyDown("n")
    sleep(3)
    # pydirectinput.keyDown("n")
    # sleep(3)


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

def fast_step(side,how_many):
    pydirectinput.keyDown(key=side)
    sleep(how_many)
    pydirectinput.keyUp(key=side)
    pydirectinput.keyDown(key='x')
    pydirectinput.keyDown(key='x')
    sleep(how_many)
    pydirectinput.keyUp(key='x')
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
        interval_side = current_time + pd.DateOffset(seconds=10)
        interval_step = current_time + pd.DateOffset(seconds=2)
        while datetime.now()< current_two:
            if datetime.now() >= interval_side:
                random_int+=1
                interval_side = datetime.now() + pd.DateOffset(seconds=10)
            if datetime.now() > interval_step:
                fast_step("left" if random_int % 2 == 0 else "right",0.5)
                interval_step = datetime.now() + pd.DateOffset(seconds=2)

            pydirectinput.keyDown("space")
            if keyboard.is_pressed("="):
                sleep(0.5)
                while True:
                    if keyboard.is_pressed("="):
                        sleep(0.5)
                        break

