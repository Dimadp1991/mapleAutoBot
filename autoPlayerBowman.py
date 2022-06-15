from ast import While
from random import randint
from time import sleep
from pip import main
import pydirectinput
from  datetime import datetime
import pandas as pd
import keyboard

 

def AutoBuff():
    pydirectinput.keyDown("c")
    sleep(2)
    # pydirectinput.keyDown("d")
    # sleep(2)
    pydirectinput.keyDown("v")
    sleep(3)
    # pydirectinput.keyDown("n")
    # sleep(3)

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
        run_auto_player=True
        current_time=datetime.now()
        current_two = current_time + pd.DateOffset(minutes=3)
        interval_side = current_time + pd.DateOffset(seconds=10)
        interval_step = current_time + pd.DateOffset(seconds=6)
        while datetime.now()< current_two:
            if datetime.now() >= interval_side:
                random_int+=1
                interval_side = datetime.now() + pd.DateOffset(seconds=30)
            if datetime.now() > interval_step:
                fast_step("left" if random_int % 2 == 0 else "right",1)
                interval_step = datetime.now() + pd.DateOffset(seconds=6)

            pydirectinput.keyDown("space")
            if keyboard.is_pressed("="):
                sleep(0.5)
                while True:
                    if keyboard.is_pressed("="):
                        sleep(0.5)
                        break

