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
    sleep(1)


if __name__ == '__main__':
    sleep(3)
    random_int=0
    auto_click_a = True
    auto_click_d = False
    auto_click_run_left = False
    auto_click_run_right = False
    check_up=False
    new_side=True
    combo_counter=0
    SIDE_SWTICH=5
    while True:
        AutoBuff()

        current_time=datetime.now()
        current_two = current_time + pd.DateOffset(minutes=2)
        interval_side = current_time + pd.DateOffset(seconds=SIDE_SWTICH)
        interval_boom = current_time + pd.DateOffset(seconds=35)
        # interval_step = current_time + pd.DateOffset(seconds=3)
        while datetime.now()< current_two:
            if auto_click_a and datetime.now() >= interval_side:
                new_side=True
                random_int+=1
                interval_side =datetime.now() + pd.DateOffset(seconds=SIDE_SWTICH)

   
            # if auto_click_a and \
            #     not keyboard.is_pressed('up')  \
            #     and not keyboard.is_pressed('down') \
            #     and not keyboard.is_pressed('alt') \
            #     and not keyboard.is_pressed('left') \
            #     and not keyboard.is_pressed('right'):
            #     pydirectinput.keyDown("a")
            # else:
            #     pydirectinput.keyUp("a")   

            if auto_click_a and \
                not keyboard.is_pressed('up')  \
                and not keyboard.is_pressed('down') \
                and not keyboard.is_pressed('alt'):
                if new_side:
                    pydirectinput.keyDown("left" if random_int % 2 == 0 else "right")
                    sleep(0.5)
                    pydirectinput.keyDown("x")
                    pydirectinput.keyUp("x")
                    pydirectinput.keyUp("left" if random_int % 2 == 0 else "right")
                    sleep(0.5)
                    pydirectinput.keyDown("right" if random_int % 2 == 0 else "left")
                    sleep(0.3)
                    pydirectinput.keyUp("right" if random_int % 2 == 0 else "left")
                    new_side=False
                pydirectinput.keyDown("a")



            if keyboard.is_pressed("="):
                pydirectinput.keyUp("a")
                sleep(0.5)
                auto_click_a = not auto_click_a

    



