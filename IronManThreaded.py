from ast import While
from random import randint
from time import sleep
from pip import main
import pydirectinput
import pyautogui
from  datetime import datetime
import pandas as pd
import threading
import multiprocessing
import keyboard

def AutoBuff():
    pydirectinput.keyDown("t")
    sleep(2)
    pydirectinput.keyUp("t")
    pydirectinput.keyDown("shift")
    sleep(2)
    pydirectinput.keyUp("shift")


def hold_a_key(key="a"):
    while True:
        pydirectinput.keyDown(key)
        sleep(0.3)


def move_n_buff():
    random_int=0
    random_int_top=0
    AutoBuff()
    buff_interval = datetime.now() + pd.DateOffset(minutes=3)
    interval_up_down = datetime.now() + pd.DateOffset(seconds=6)
    while True:
        if datetime.now() > buff_interval:
            AutoBuff()
            buff_interval = datetime.now() + pd.DateOffset(minutes=3)

        side="left" if random_int % 2 == 0 else "right"
        up_down="up" if random_int_top % 2 == 0 else "down"

        interval_side = datetime.now() + pd.DateOffset(seconds=2)
        while datetime.now() < interval_side:
            pydirectinput.keyDown(side)
            sleep(0.8)
            pydirectinput.keyUp(side)
            if datetime.now() > interval_up_down:
                interval_up_down = datetime.now() + pd.DateOffset(seconds=6)
                pydirectinput.keyDown(up_down)
                sleep(0.3)
                pydirectinput.keyUp(up_down)

                random_int_top+=1   
        random_int+=1 

if __name__ == '__main__':
    sleep(3)
    m_n_buff=multiprocessing.Process(target=move_n_buff)
    attack_n_chill=multiprocessing.Process(target=hold_a_key)
    attack_n_chill.start()
    m_n_buff.start()
    while True:
        if keyboard.is_pressed("="):
            attack_n_chill.terminate()
            m_n_buff.terminate()
            sleep(0.5)
            while True:
                if keyboard.is_pressed("="):
                    sleep(0.5)
                    m_n_buff=multiprocessing.Process(target=move_n_buff)
                    m_n_buff.start()
                    attack_n_chill=multiprocessing.Process(target=hold_a_key)
                    attack_n_chill.start()
                    break





    