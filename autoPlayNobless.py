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
    sleep(2)
    pydirectinput.keyDown("v")
    sleep(2)



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

def double_press_button(key):
    pydirectinput.keyDown(key=key)
    sleep(0.25)
    pydirectinput.keyUp(key=key)
    pydirectinput.keyDown(key=key)
    sleep(0.25)
    pydirectinput.keyUp(key=key)

def jump_to(side):
    if side == "up":
        pydirectinput.keyDown(key=side)
        pydirectinput.keyDown(key="x")
        sleep(0.15)
        pydirectinput.keyDown(key="x")
        sleep(0.15)
        pydirectinput.keyUp(key=side)
        pydirectinput.keyUp(key="x")
    elif side =="down":
        pydirectinput.keyDown(key=side)
        sleep(0.15)
        pydirectinput.keyDown(key="altleft")
        sleep(0.15)
        pydirectinput.keyDown(key="altleft")
        sleep(0.15)
        pydirectinput.keyDown(key="altleft")
        sleep(0.15)
        pydirectinput.keyDown(key="altleft")
        pydirectinput.keyUp(key=side)
        pydirectinput.keyUp(key="altleft")

if __name__ == '__main__':
    sleep(3)
    random_int=0
    random_int_jump=0
    while True:
        sleep(3)
        AutoBuff()
        AutoSell()
        run_auto_player=True
        current_time=datetime.now()
        current_two = current_time + pd.DateOffset(minutes=3)
        interval_side = current_time + pd.DateOffset(seconds=4)
        jump_interval = current_time + pd.DateOffset(seconds=8)
        while datetime.now()< current_two:
            if datetime.now() >= interval_side:
                random_int+=1
                interval_side = datetime.now() + pd.DateOffset(seconds=4)
                press_button("left" if random_int % 2 == 0 else "right")
            if datetime.now() > jump_interval:
                jump_to("up" if random_int_jump % 2 == 0 else "down")
                jump_interval = datetime.now() + pd.DateOffset(seconds=8)
                random_int_jump+=1


            pydirectinput.keyDown("a")
            pydirectinput.keyUp("a")
            if keyboard.is_pressed("="):
                sleep(0.5)
                while True:
                    if keyboard.is_pressed("="):
                        sleep(0.5)
                        break

