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
    sleep(1.5)
    # pydirectinput.keyDown("v")
    # sleep(2)
    # pydirectinput.keyDown("n")
    # sleep(2)
    # pydirectinput.keyDown("f")
    # sleep(1)

def repeat_attack(n,key,sleep_time):
    for i in range(n): 
        pydirectinput.keyDown(key)
        sleep(sleep_time)
        pydirectinput.keyUp(key)

def flash_jump_side(n,side,jump_key,flash_jump_key):
    for i in range(n): 
        pydirectinput.keyDown(side)
        pydirectinput.keyDown(jump_key)
        sleep(0.1)
        pydirectinput.keyDown(flash_jump_key)
        pydirectinput.keyUp(jump_key)
        pydirectinput.keyUp(flash_jump_key)
        pydirectinput.keyUp(side)

if __name__ == '__main__':
    # pydirectinput.PAUSE=0.06
    sleep(3)
    random_int=0
    auto_click_a = True
    attack_key="a"
    SIDE_TIME=12
    MOVE_TIME=1
    new_line_move=True
    interval_side = datetime.now() + pd.DateOffset(seconds=SIDE_TIME)
    interval_move = datetime.now() + pd.DateOffset(minutes=MOVE_TIME)
    interval_buff = datetime.now() + pd.DateOffset(minutes=2)
    while True:
            if auto_click_a and datetime.now() >= interval_side:
                interval_side = datetime.now() + pd.DateOffset(seconds=SIDE_TIME)

                flash_jump_side(n=6,
                                side="left",
                                jump_key="alt",
                                flash_jump_key="x")
                # random_int+=1
                # pydirectinput.keyDown("right" if random_int % 2 == 0 else "left")
                # sleep(0.4)
                # pydirectinput.keyUp("right" if random_int % 2 == 0 else "left")

                pydirectinput.keyDown("right")
                sleep(0.4)
                pydirectinput.keyUp("right")
                new_line_move=True
            # if auto_click_a and datetime.now() >= interval_buff:
            #     interval_buff = datetime.now() + pd.DateOffset(minutes=2)
            #     AutoBuff()

            # if auto_click_a and datetime.now() >= interval_move:
            #     pydirectinput.keyDown("left")
            #     sleep(1)
            #     pydirectinput.keyUp("left")
            #     # pydirectinput.keyDown("right" if random_int % 2 == 0 else "left")
            #     # pydirectinput.keyUp("right" if random_int % 2 == 0 else "left")
            #     interval_move = datetime.now() + pd.DateOffset(minutes=MOVE_TIME)

    

            if auto_click_a and \
                not keyboard.is_pressed('up')  \
                and not keyboard.is_pressed('down') \
                and not keyboard.is_pressed('alt') \
                and not keyboard.is_pressed('left') \
                and not keyboard.is_pressed('right'):

                if new_line_move:    
                    repeat_attack(n=4,key="space",sleep_time=0.8)
                    new_line_move=False

                pydirectinput.keyDown(attack_key)

                
                # pydirectinput.keyDown("right" if random_int % 2 == 0 else "left")
                # pydirectinput.keyDown("space")
                # pydirectinput.keyUp("space")
                # pydirectinput.keyUp("right" if random_int % 2 == 0 else "left")

            else:
                pydirectinput.keyUp(attack_key)    

                

            if keyboard.is_pressed("="):
                pydirectinput.keyUp(attack_key)
                auto_click_a = not auto_click_a
                print("= Clicked status is: ",auto_click_a)
            # if keyboard.is_pressed("-"):
            #     print("Buffing...")
            #     pydirectinput.keyUp(attack_key)
            #     AutoBuff()


            if keyboard.is_pressed("-"):
                attack_key= "d" if  attack_key=="a" else "a"
                print(f"attack  key is {attack_key} ")

    