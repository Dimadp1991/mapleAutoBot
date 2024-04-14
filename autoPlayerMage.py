from time import sleep
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
    # pydirectinput.keyDown("n")
    # sleep(3)
    # pydirectinput.keyDown("n")
    # sleep(3)


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

def press_button(key):
    pydirectinput.keyDown(key=key)
    sleep(0.5)
    pydirectinput.keyUp(key=key)

def fast_step(side,how_many):
  for i in range(how_many):  
    th1=threading.Thread(target=press_button,args=[side])
    th2=threading.Thread(target=press_button,args=['x'])
    th1.start()
    th2.start()
    th1.join()
    th2.join()
    # sleep(0.25)
    # pydirectinput.keyUp(side)
    # pydirectinput.keyDown("left" if side == "right" else "right" )
    # pydirectinput.keyUp("left" if side == "right" else "right" )
if __name__ == '__main__':
    pydirectinput.PAUSE=0.06
    sleep(3)
    random_int=0
    while True:
        # sleep(3)
        auto_click=True
        current_time=datetime.now()
        AutoBuff()
        current_two = current_time + pd.DateOffset(minutes=2)
        interval_side = current_time + pd.DateOffset(seconds=10)
        interval_step = current_time + pd.DateOffset(seconds=5)
        while datetime.now()< current_two:
            if datetime.now() > interval_step:
                # fast_step("left" if random_int % 2 == 0 else "right",1)
                fast_step("left",1)
                interval_step = datetime.now() + pd.DateOffset(seconds=4)
                # random_int+=1

          
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