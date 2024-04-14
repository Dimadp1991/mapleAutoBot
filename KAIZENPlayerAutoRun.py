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


if __name__ == '__main__':
    sleep(3)
    random_int=0
    auto_click_a = False
    auto_click_d = False
    auto_click_run_left = False
    auto_click_run_right = False
    check_up=False
    combo_counter=0
    while True:
        # AutoBuff()

        current_time=datetime.now()
        current_two = current_time + pd.DateOffset(minutes=2)
        interval_side = current_time + pd.DateOffset(seconds=3)
        interval_boom = current_time + pd.DateOffset(seconds=35)
        # interval_step = current_time + pd.DateOffset(seconds=3)
        while datetime.now()< current_two:
            # if  auto_click_a or auto_click_d and datetime.now() >= interval_side:
            #     pydirectinput.keyUp("a")
            #     pydirectinput.keyUp("d")
            #     random_int+=1
            #     pydirectinput.keyDown("left" if random_int % 2 == 0 else "right")
            #     # sleep(1.7)
            #     pydirectinput.keyUp("left" if random_int % 2 == 0 else "right")
            #     interval_side =datetime.now() + pd.DateOffset(seconds=3)

   
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
  
                pydirectinput.keyDown("a")
                pydirectinput.keyUp("a")  
            

            if keyboard.is_pressed("="):
                pydirectinput.keyUp("a")
                sleep(0.5)
                auto_click_a = not auto_click_a

            if keyboard.is_pressed("["):
                if auto_click_run_left:
                    func=pydirectinput.keyUp
                else:
                    func=pydirectinput.keyDown
                auto_click_run_right=False
                pydirectinput.keyUp("right")
                auto_click_run_left= not auto_click_run_left
                func("left")

            if keyboard.is_pressed("]"):
                if auto_click_run_right:
                    func=pydirectinput.keyUp
                else:
                    func=pydirectinput.keyDown
                auto_click_run_left=False
                pydirectinput.keyUp("left")
                auto_click_run_right= not auto_click_run_right
                func("right")


