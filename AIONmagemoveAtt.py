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
    pydirectinput.keyUp("c")
    # pydirectinput.keyDown("v")
    # sleep(1)
    # pydirectinput.keyUp("v")
    # pydirectinput.keyDown("v")
    # sleep(2)
    # pydirectinput.keyDown("n")
    # sleep(2)
    # pydirectinput.keyDown("f")
    # sleep(1)


def jump_att_side(n,side,jump_key,attack_key):
    for i in range(n): 
        pydirectinput.keyDown(side)
        pydirectinput.keyDown(jump_key)
        sleep(0.1)
        pydirectinput.keyDown(attack_key)
        pydirectinput.keyUp(attack_key)
        pydirectinput.keyUp(jump_key)
        pydirectinput.keyUp(side)

if __name__ == '__main__':
    pydirectinput.PAUSE=0.06
    sleep(3)
    random_int=0
    current_side="right" if random_int % 2 == 0 else "left"
    auto_click_a = True
    attack_key="a"
    SIDE_TIME=60
    MOVE_TIME=10
    BUFF_TIME=120
    new_line_move=True
    interval_side = datetime.now() +pd.DateOffset(seconds=SIDE_TIME)
    interval_move = datetime.now() + pd.DateOffset(seconds=MOVE_TIME)
    interval_buff = datetime.now() + pd.DateOffset(seconds=BUFF_TIME)
    while True:
            if auto_click_a and datetime.now() >= interval_side:
                sleep(1)
                pydirectinput.keyUp(attack_key)  
                # AutoBuff()
                interval_side = datetime.now() + pd.DateOffset(seconds=SIDE_TIME)
                pydirectinput.keyDown(current_side)
                sleep(0.2)
                pydirectinput.keyUp(current_side)  
                # print("Current Side is: ",current_side)
                random_int+=1
                current_side="right" if random_int % 2 == 0 else "left"


            if auto_click_a and datetime.now() >= interval_buff:
                interval_buff = datetime.now() + pd.DateOffset(seconds=BUFF_TIME)
                AutoBuff()

            # if auto_click_a and datetime.now() >= interval_move:
            #     pydirectinput.keyUp(attack_key)
            #     sleep(0.5)
            #     pydirectinput.keyDown("right" if random_int % 2 == 0 else "left")
            #     sleep(0.05)
            #     pydirectinput.keyUp("right" if random_int % 2 == 0 else "left")
            #     interval_move = datetime.now() + pd.DateOffset(seconds=MOVE_TIME)
            #     random_int+=1

    

            if auto_click_a and \
                not keyboard.is_pressed('up')  \
                and not keyboard.is_pressed('down') \
                and not keyboard.is_pressed('alt') \
                and not keyboard.is_pressed('left') \
                and not keyboard.is_pressed('right'):

                pydirectinput.keyDown(attack_key)
                # pydirectinput.keyUp(attack_key)
              
      
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

    