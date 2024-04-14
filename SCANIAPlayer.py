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
    sleep(2.5)
    pydirectinput.keyUp("c")
    pydirectinput.keyDown("v")
    sleep(2.5)
    pydirectinput.keyUp("v")
    # pydirectinput.keyDown("v")
    # sleep(2)
    # pydirectinput.keyDown("n")
    # sleep(2)
    # pydirectinput.keyDown("f")
    # sleep(1)

# def press_button(key):
#     pydirectinput.keyDown(key=key)
#     sleep(0.5)
#     pydirectinput.keyUp(key=key)

# def fast_step(side,how_many):
#   for i in range(how_many):  
#     th1=threading.Thread(target=press_button,args=[side])
#     th2=threading.Thread(target=press_button,args=['x'])
#     th1.start()
#     th2.start()
#     th1.join()
#     th2.join()

if __name__ == '__main__':
    pydirectinput.PAUSE=0.06
    sleep(3)
    random_int=0
    current_side="right" if random_int % 2 == 0 else "left"
    auto_click_a = True
    auto_pick_up=False
    attack_key="a"
    SIDE_TIME=5
    MOVE_TIME=10
    new_line_move=True
    interval_side = datetime.now() +pd.DateOffset(seconds=SIDE_TIME)
    interval_move = datetime.now() + pd.DateOffset(seconds=MOVE_TIME)
    interval_buff = datetime.now() + pd.DateOffset(minutes=3)
    interval_speed = datetime.now() + pd.DateOffset(seconds=10)
    ultimate_att = datetime.now() + pd.DateOffset(minutes=1.1)
    while True:
            # if auto_click_a and datetime.now() >= interval_side:
            #     sleep(1)
            #     pydirectinput.keyUp(attack_key)  
            #     interval_side = datetime.now() + pd.DateOffset(seconds=SIDE_TIME)

            #     # print("Current Side is: ",current_side)
            #     random_int+=1
            #     current_side="right" if random_int % 2 == 0 else "left"


                

            # if auto_click_a and datetime.now() >= interval_move:
            #     pydirectinput.keyUp(attack_key)
            #     sleep(0.5)
            #     pydirectinput.keyDown("right" if random_int % 2 == 0 else "left")
            #     sleep(0.05)
            #     pydirectinput.keyUp("right" if random_int % 2 == 0 else "left")
            #     interval_move = datetime.now() + pd.DateOffset(seconds=MOVE_TIME)
            # #     random_int+=1

            
            # if  datetime.now() >= interval_buff:
            # #     # pydirectinput.keyDown("left")
            # #     # sleep(0.4)
            # #     # pydirectinput.keyUp("left")
            # #     # pydirectinput.keyDown("right")
            # #     # sleep(0.4)
            # #     # pydirectinput.keyUp("right")
            #     sleep
            #     pydirectinput.keyUp(attack_key)
            #     AutoBuff()
            #     interval_buff = datetime.now() + pd.DateOffset(minutes=3)

            # if datetime.now() >= interval_speed:
            #     pydirectinput.keyDown("t")
            #     pydirectinput.keyDown("t")
            #     interval_speed = datetime.now() + pd.DateOffset(seconds=10)


            if auto_click_a and \
                not keyboard.is_pressed('up')  \
                and not keyboard.is_pressed('down') :
                # and not keyboard.is_pressed('alt') :
                # and not keyboard.is_pressed('left') \
                # and not keyboard.is_pressed('right'):

                if auto_pick_up:
                    pydirectinput.keyUp("z")

                # fast_step(side=current_side,how_many=1)
                pydirectinput.keyDown(attack_key)
          

              
      
            else:
                pydirectinput.keyUp(attack_key)  
                if auto_pick_up:  
                    pydirectinput.keyDown("z")

                

            if keyboard.is_pressed("="):
                pydirectinput.keyUp(attack_key)
                auto_click_a = not auto_click_a
                auto_pick_up= False
                print("auto_pick_up: ",auto_pick_up)
                print("= Clicked status is: ",auto_click_a)
            if keyboard.is_pressed("]"):
                auto_pick_up= not auto_pick_up
                print("auto_pick_up: ",auto_pick_up)

            if keyboard.is_pressed("-"):
                attack_key= "d" if  attack_key=="a" else "a"
                print(f"attack  key is {attack_key} ")

    # R> Scarga Must have prequest Done