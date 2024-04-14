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
    pydirectinput.keyDown("n")
    sleep(2)
    # pydirectinput.keyDown("f")
    # sleep(1)

def tp_move(side,how_many):
            
    for i in range(how_many):  
            pydirectinput.keyDown(key=side)
            pydirectinput.keyDown(key='x')
            pydirectinput.keyUp(key='x')
            pydirectinput.keyUp(key=side)

if __name__ == '__main__':
    pydirectinput.PAUSE=0.06
    sleep(3)
    random_int=0
    auto_click_a = False
    attack_key="a"
    check_up=False
    combo_counter=0
    SIDE_TIME=6
    interval_side = datetime.now() + pd.DateOffset(seconds=SIDE_TIME)
    interval_boom = datetime.now() + pd.DateOffset(seconds=3)
    side ="left" if random_int % 2 == 0 else "right"
    while True:
        # AutoBuff()

        current_two = datetime.now() + pd.DateOffset(minutes=2.5)
        # interval_step = current_time + pd.DateOffset(seconds=3)
        while datetime.now()< current_two:
            if auto_click_a and datetime.now() >= interval_side:
                pydirectinput.keyUp(attack_key)
                side ="left" if random_int % 2 == 0 else "right"
                pydirectinput.keyDown(side)
                sleep(0.3)
                pydirectinput.keyUp(side)
                interval_side = datetime.now() + pd.DateOffset(seconds=SIDE_TIME)
                random_int+=1
           


            if auto_click_a and \
                not keyboard.is_pressed('up')  \
                and not keyboard.is_pressed('down') \
                and not keyboard.is_pressed('alt') \
                and not keyboard.is_pressed('left') \
                and not keyboard.is_pressed('right'):
                tp_move(side=side,how_many=1)
                pydirectinput.keyDown(attack_key)
                # pydirectinput.keyUp(attack_key)
                # pydirectinput.keyDown("f")
                # pydirectinput.keyDown("f")
            #   eXyPlus#2919
                
            else:
                pydirectinput.keyUp(attack_key)    

                

            if keyboard.is_pressed("="):
                pydirectinput.keyUp(attack_key)
                sleep(0.5)
                auto_click_a = not auto_click_a
                print("= Clicked status is: ",auto_click_a)
            if keyboard.is_pressed("-"):
                print("Buffing...")
                pydirectinput.keyUp(attack_key)
                sleep(0.5)
                AutoBuff()

            if keyboard.is_pressed("[") or keyboard.is_pressed("]"):
                attack_key= "d" if  attack_key=="a" else "a"
                print(f"attack  key is {attack_key} ")
            # if keyboard.is_pressed("-"):
            #     print(f"Buffing.. ")
            #     AutoBuff()
        
#           