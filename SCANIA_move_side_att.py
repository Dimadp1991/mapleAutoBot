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
    # pydirectinput.keyDown("n")
    # sleep(2)
    # pydirectinput.keyDown("f")
    # sleep(1)


def press_button(key):
    pydirectinput.PAUSE=0.05
    pydirectinput.keyDown(key=key)


def auto_sell_miu():
    sleep(3)

    pydirectinput.keyDown("enter")
    sleep(1)
    pydirectinput.keyUp("enter")

    pydirectinput.keyDown("shift")
    sleep(1)
    pydirectinput.keyDown("2")
    sleep(1)
    pydirectinput.keyUp("shift")
    sleep(1)
    pydirectinput.keyUp("2")

    pydirectinput.keyDown("m")
    sleep(1)
    pydirectinput.keyUp("m")

    pydirectinput.keyDown("i")
    sleep(1)
    pydirectinput.keyUp("i")

    pydirectinput.keyDown("u")
    sleep(1)
    pydirectinput.keyUp("u")

    pydirectinput.keyDown("enter")
    sleep(1)
    pydirectinput.keyUp("enter")


    sleep(2)
    pydirectinput.moveTo(x=760, y=375)
    sleep(2)
    pydirectinput.click()
    sleep(1)
    pydirectinput.keyDown("enter")
    sleep(1)
    pydirectinput.keyUp("enter")
    sleep(2)
    pydirectinput.keyDown("esc")
    sleep(1)
    pydirectinput.keyUp("esc")
    pydirectinput.keyDown("esc")
    sleep(1)
    pydirectinput.keyUp("esc")
    pydirectinput.keyDown("esc")
    sleep(1)
    pydirectinput.keyUp("esc")


def repeat_attack(n,key,sleep_time):
    for i in range(n): 
        pydirectinput.keyDown(key)
        sleep(sleep_time)
        pydirectinput.keyUp(key)

def run_runing_thread(side):
    th=threading.Thread(target=press_button,args=[side],daemon=True) 
    th.start()
    return th


if __name__ == '__main__':
    # pydirectinput.PAUSE=0.06
    sleep(3)
    random_int=1
    auto_click_a = True
    attack_key="a"
    SIDE_TIME=12
    MOVE_TIME=1
    new_line_move=True
    current_side="right" if random_int % 2 == 0 else "left"
    th2=run_runing_thread(side=current_side)

    interval_side = datetime.now() + pd.DateOffset(seconds=SIDE_TIME)
    interval_move = datetime.now() + pd.DateOffset(minutes=MOVE_TIME)
    interval_buff = datetime.now() + pd.DateOffset(minutes=2)
    interval_feed_pet = datetime.now() + pd.DateOffset(minutes=8)
    interval_auto_sell = datetime.now() + pd.DateOffset(minutes=10)
    while True:
            if auto_click_a and datetime.now() >= interval_side:
                pydirectinput.keyUp(attack_key)
                pydirectinput.keyUp(attack_key)

                pydirectinput.keyUp(current_side)
                pydirectinput.keyUp(current_side)
                th2.join()
                interval_side = datetime.now() + pd.DateOffset(seconds=SIDE_TIME)

                random_int+=1
                current_side="right" if random_int % 2 == 0 else "left"
                
                th2=run_runing_thread(side=current_side)
          


            if auto_click_a and datetime.now() >= interval_buff:
                pydirectinput.keyUp(attack_key)
                pydirectinput.keyUp(attack_key)

                pydirectinput.keyUp(current_side)
                pydirectinput.keyUp(current_side)
                th2.join()
                interval_buff = datetime.now() + pd.DateOffset(minutes=2)
                AutoBuff()
                th2=run_runing_thread(side=current_side)
            
            if auto_click_a and datetime.now() >= interval_auto_sell:
                    pydirectinput.keyUp(attack_key)
                    pydirectinput.keyUp(attack_key)

                    pydirectinput.keyUp(current_side)
                    pydirectinput.keyUp(current_side)
                    th2.join()
                    interval_auto_sell = datetime.now() + pd.DateOffset(minutes=10)
                    auto_sell_miu()
                    th2=run_runing_thread(side=current_side)

            
            if auto_click_a and datetime.now() >= interval_feed_pet:
                pydirectinput.keyDown("t")
                pydirectinput.keyUp("t")
                pydirectinput.keyDown("t")
                pydirectinput.keyUp("t")
                interval_feed_pet = datetime.now() + pd.DateOffset(minutes=8)
            

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
                and not keyboard.is_pressed('alt') :
                # and not keyboard.is_pressed('left') \
                # and not keyboard.is_pressed('right'):

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
                if auto_click_a:
                    pydirectinput.keyUp(attack_key)
                    pydirectinput.keyUp(attack_key)

                    pydirectinput.keyUp(current_side)
                    pydirectinput.keyUp(current_side)
                    th2.join()
                elif not auto_click_a:
                    th2=run_runing_thread(side=current_side)
            # if keyboard.is_pressed("-"):
            #     print("Buffing...")
            #     pydirectinput.keyUp(attack_key)
            #     AutoBuff()


            if keyboard.is_pressed("-"):
                attack_key= "d" if  attack_key=="a" else "a"
                print(f"attack  key is {attack_key} ")

    