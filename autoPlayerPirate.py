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
    # pydirectinput.keyDown("v")




def fast_step(side,how_many):
    pydirectinput.keyDown(side)
    sleep(how_many)
    pydirectinput.keyUp(side)
    pydirectinput.keyDown("left" if side == "right" else "right" )
    pydirectinput.keyUp("left" if side == "right" else "right" )
if __name__ == '__main__':
    sleep(3)
    random_int=0
    auto_click = False
    while True:
        # pydirectinput.keyUp("left" if random_int % 2 == 0 else "right")
        # sleep(2)
        # AutoBuff()

        run_auto_player=True
        current_time=datetime.now()
        current_two = current_time + pd.DateOffset(minutes=3)
        interval_side = current_time + pd.DateOffset(seconds=5)
        interval_boom = current_time + pd.DateOffset(seconds=70)
        interval_step = current_time + pd.DateOffset(seconds=3)
        while datetime.now()< current_two:
            # if  auto_click and datetime.now() >= interval_side:
            #     random_int+=1
            #     pydirectinput.keyDown("left" if random_int % 2 == 0 else "right")
            #     sleep(1.7)
            #     pydirectinput.keyUp("left" if random_int % 2 == 0 else "right")

            #     interval_side = datetime.now() + pd.DateOffset(seconds=5)
            # if  auto_click and datetime.now() >= interval_boom:
                   # random_int+=1
                # pydirectinput.keyUp("a")
                # sleep(1)
                # pydirectinput.keyDown("left" if random_int % 2 == 0 else "right")
                # pydirectinput.keyUp("left" if random_int % 2 == 0 else "right")
                # interval_kaboom = datetime.now() + pd.DateOffset(secondas=5)
                # while datetime.now()< interval_kaboom:
                #     pydirectinput.keyDown("f")
                #     pydirectinput.keyUp("f")                
                # interval_boom = datetime.now() + pd.DateOffset(seconds=70)
   
            if auto_click and not keyboard.is_pressed('up')  \
                and not keyboard.is_pressed('down') \
                and not keyboard.is_pressed('alt') \
                and not keyboard.is_pressed('left') \
                and not keyboard.is_pressed('right'):
                pydirectinput.keyDown("a")

           
            else:
                pydirectinput.keyUp("a")
    
            if keyboard.is_pressed("="):
                pydirectinput.keyUp("a")
                sleep(0.5)
                auto_click = not auto_click
            