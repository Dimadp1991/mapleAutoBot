from time import sleep
import pydirectinput
from datetime import datetime
import pandas as pd
import keyboard
import threading


def AutoBuff():
    pydirectinput.keyDown("c")
    sleep(3)





def FeedPet():
    press_button("insert")
    sleep(1)
    press_button("insert")


def press_button(key):
    pydirectinput.keyDown(key=key)
    pydirectinput.keyUp(key=key)

def press_button_hold(key,sec):
    pydirectinput.keyDown(key=key)
    sleep(sec)
    pydirectinput.keyUp(key=key)

def fast_step(side, how_many):
    for i in range(how_many):
        pydirectinput.keyDown(key=side)
        # pydirectinput.keyDown(key='x')
        # pydirectinput.keyUp(key='x')
        sleep(1.5)
        pydirectinput.keyUp(key=side)

def press_hold(key,sec):
        th1=threading.Thread(target=press_button_hold,args=[key,sec])
        th1.start()
        th1.join()


def fast_step_with_jump(side, how_many):
    for i in range(how_many):
        pydirectinput.keyDown(key=side)
        # pydirectinput.keyDown(key='alt')
        # pydirectinput.keyUp(key='alt')
        pydirectinput.keyDown(key='x')
        pydirectinput.keyUp(key='x')
        # pydirectinput.keyDown(key='alt')
        # pydirectinput.keyUp(key='alt')

        pydirectinput.keyUp(key=side)


if __name__ == '__main__':

    TELEPORTS_TO_SIDE = 1
    INTERVAL_JUMP_UP = 7
    INTERVAL_ATTACK_SEC = 8
    INTERVAL_CHANGE_SIDE_SEC = 20
    TIME_TO_BUFF_IN_MINUTES = 2
    sygnus_buff = datetime.now() + pd.DateOffset(minutes=10)
    sleep(3)
    random_int = 0
    while True:
        sleep(3)
        AutoBuff()
        # AutoSell()
        run_auto_player = True
        current_time = datetime.now()
        current_two = current_time + pd.DateOffset(minutes=TIME_TO_BUFF_IN_MINUTES)
        interval_side = current_time + pd.DateOffset(seconds=INTERVAL_CHANGE_SIDE_SEC)
        interval_step = current_time + pd.DateOffset(seconds=INTERVAL_ATTACK_SEC)
        tele_up_step = current_time + pd.DateOffset(seconds=INTERVAL_JUMP_UP)

        job_five_skill = current_time + pd.DateOffset(seconds=11)

        feed_pet_interval = current_time + pd.DateOffset(minutes=10)

        while datetime.now() < current_two:
            # if datetime.now() >= interval_side:                   
            #     random_int+=1
            #     interval_side = datetime.now() + pd.DateOffset(seconds=INTERVAL_CHANGE_SIDE_SEC)
            #     pydirectinput.keyUp("a")
            #     fast_step("left" if random_int % 2 == 0 else "right",TELEPORTS_TO_SIDE)

            # if datetime.now() > tele_up_step:
            #     random_int += 1
            #     pydirectinput.keyUp("a")

            #     # fast_step_with_jump("up",1)
            #     # fast_step_with_jump("up" if random_int % 2 == 0 else "down",2 if random_int % 2 == 0 else 1)
            #     fast_step_with_jump("up" if random_int % 2 == 0 else "down", 1)
            #     tele_up_step = datetime.now() + pd.DateOffset(seconds=INTERVAL_JUMP_UP)

            # if datetime.now() > feed_pet_interval:
            #     FeedPet()
            #     feed_pet_interval = datetime.now() + pd.DateOffset(minutes=10)
            if not keyboard.is_pressed('up') and not keyboard.is_pressed('down') and not keyboard.is_pressed('alt') and not keyboard.is_pressed('left') and not keyboard.is_pressed('right'):
                # if datetime.now() > job_five_skill:
                #     pydirectinput.keyUp("a")
                #     pydirectinput.keyDown("f")
                #     pydirectinput.keyUp("f")
                #     job_five_skill = datetime.now() + pd.DateOffset(seconds=11)
                
                # if datetime.now() > sygnus_buff:
                #     pydirectinput.keyUp("a")
                #     pydirectinput.keyDown("n")
                #     sleep(2)
                #     pydirectinput.keyUp("n")
                #     sygnus_buff = datetime.now() + pd.DateOffset(minutes=10)


                # pydirectinput.keyDown("a")
                # pydirectinput.keyUp("a")
                pydirectinput.keyDown("d")
                # pydirectinput.keyUp("d")
                pydirectinput.keyDown("f")
                # pydirectinput.keyUp("f")cadfadfadfadfadfadfadfadfadf
                # sleep(0.5)
                if keyboard.is_pressed("="):
                    sleep(0.5)
                    while True:
                        if keyboard.is_pressed("="):
                            sleep(0.5)
                            break
