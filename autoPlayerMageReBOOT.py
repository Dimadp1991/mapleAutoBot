
from time import sleep
import pydirectinput
from  datetime import datetime
import pandas as pd
import keyboard
import threading

 

def AutoBuff():
    pydirectinput.keyDown("c")
    sleep(3)
    pydirectinput.keyDown("n")
    sleep(1)
    pydirectinput.keyDown("6")
    sleep(1)
    pydirectinput.keyDown("7")
    sleep(1)

def FeedPet():
    press_button("insert")
    sleep(1)
    press_button("insert")


def press_button(key):
    pydirectinput.keyDown(key=key)
    pydirectinput.keyUp(key=key)

def fast_step(side,how_many):
    
  for i in range(how_many):  
        pydirectinput.keyDown(key=side)
        # if side != 'down':
        #     pydirectinput.keyDown(key='alt')
        pydirectinput.keyDown(key='x')
        pydirectinput.keyDown(key='x')
        pydirectinput.keyUp(key='x')
        pydirectinput.keyUp(key='alt')
        pydirectinput.keyUp(key=side)

def fast_step_with_jump(side,how_many):
    
  for i in range(how_many):  
        pydirectinput.keyDown(key=side)
        pydirectinput.keyDown(key='alt')
        pydirectinput.keyUp(key='alt')
        
        pydirectinput.keyDown(key='alt')
        pydirectinput.keyUp(key='alt')
        
        pydirectinput.keyUp(key=side)


if __name__ == '__main__':

    INTERVAL_JUMP_UP=10
    INTERVAL_ATTACK_SEC=8
    INTERVAL_CHANGE_SIDE_SEC=20
    TIME_TO_BUFF_IN_MINUTES=2

    sleep(3)
    random_int=0
    while True:
        sleep(3)
        AutoBuff()
        # AutoSell()
        run_auto_player=True
        current_time=datetime.now()
        current_two = current_time + pd.DateOffset(minutes=TIME_TO_BUFF_IN_MINUTES)
        interval_side = current_time + pd.DateOffset(seconds=INTERVAL_CHANGE_SIDE_SEC)
        interval_step = current_time + pd.DateOffset(seconds=INTERVAL_ATTACK_SEC)
        tele_up_step = current_time + pd.DateOffset(seconds=INTERVAL_ATTACK_SEC+1)

        feed_pet_interval = current_time + pd.DateOffset(minutes=10)

        while datetime.now()< current_two:
            if datetime.now() >= interval_side:                   
                random_int+=1
                interval_side = datetime.now() + pd.DateOffset(seconds=INTERVAL_CHANGE_SIDE_SEC)
                pydirectinput.keyUp("a")
                fast_step("left" if random_int % 2 == 0 else "right",2)

            if datetime.now() > tele_up_step:
                pydirectinput.keyUp("a")
                # fast_step_with_jump("up",1)
                fast_step_with_jump("up" if random_int % 2 == 0 else "down",1)
                tele_up_step = datetime.now() + pd.DateOffset(seconds=INTERVAL_JUMP_UP)

            if datetime.now() > feed_pet_interval:
                FeedPet()
                feed_pet_interval = datetime.now() + pd.DateOffset(minutes=10)

            pydirectinput.keyDown("a")
            if keyboard.is_pressed("="):
                sleep(0.5)
                while True:
                    if keyboard.is_pressed("="):
                        sleep(0.5)
                        break

