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
    # pydirectinput.keyDown("n")
    # sleep(2)



# def AutoSell():
#     pydirectinput.keyDown("enter")
#     sleep(0.5)
#     pydirectinput.keyDown("up")
#     sleep(0.5)
#     pydirectinput.keyUp("up")
#     pydirectinput.keyDown("enter")
#     sleep(0.5)
#     pydirectinput.keyDown("enter")
#     sleep(0.5)
#     pydirectinput.keyUp("enter")

# #
def press_button(key,sleep_time=None,how_many=20):
    pydirectinput.PAUSE=0.05
    for i in range(how_many):
        pydirectinput.keyDown(key=key)
        if sleep_time:
            th2=threading.Thread(target=press_button,args=['a',None,20],daemon=True) 
            th2.start()
            sleep(sleep_time)
            th2.join()
        # pydirectinput.keyUp(key=key)


 
if __name__ == '__main__':
    aa=3
    sleep(3)
    random_int=0
    auto_click=True
    SLEEP_TIME_WHILE_RUN=3
    current_time=datetime.now()
    current_two = current_time + pd.DateOffset(minutes=3)
    interval_side = current_time + pd.DateOffset(seconds=10)
    interval_step = current_time + pd.DateOffset(seconds=5)
    interval_buff = current_time + pd.DateOffset(minutes=2)
    while True:


            if datetime.now() > interval_step:
                interval_step = datetime.now() + pd.DateOffset(seconds=5)
                random_int+=1
            
            
            if datetime.now() > interval_buff:
                interval_buff = datetime.now() + pd.DateOffset(minutes=2)
                AutoBuff()
          
            if auto_click and not keyboard.is_pressed('up')  \
                and not keyboard.is_pressed('down') \
                and not keyboard.is_pressed('alt') \
                and not keyboard.is_pressed('left') \
                and not keyboard.is_pressed('right'):

                next_side="left" if random_int % 2 == 0 else "right"
                th1=threading.Thread(target=press_button,args=[next_side,SLEEP_TIME_WHILE_RUN,1],daemon=True)
                th1.start()
                th1.join()
            if keyboard.is_pressed("="):
               exit()
            if keyboard.is_pressed("-"):
                AutoBuff()