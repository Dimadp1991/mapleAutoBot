from time import sleep
import pydirectinput
import keyboard
import tkinter as tk
import threading
global window
global start_program
import pandas as pd
from  datetime import datetime
import random
# creating executable
# pyinstaller --onefile --noconsole autoclick_interval_ver_avi01.py


def set_start_program(val):
    global start_program
    start_program = val
    # print(start_program)

def press_button(key):
    pydirectinput.keyDown(key=key)
    pydirectinput.keyUp(key=key)


def auto_clicker(press_key,min_time,max_time):
    sleep(3)
    global start_program
    start_program = True
    rand_buff_time=random.randint(int(min_time),int(max_time))
    print(f"random buff time is:{str(rand_buff_time)}")
    time_interval = datetime.now() + pd.DateOffset(seconds=int(rand_buff_time))
    while True:
        if not start_program: return
        if start_program and datetime.now() >= time_interval:
                sleep(0.5)
                pydirectinput.keyDown(press_key)
                sleep(3)
                pydirectinput.keyUp(press_key)
                rand_buff_time=random.randint(int(min_time),int(max_time))
                print(f"random buff time is:{str(rand_buff_time)}")
                time_interval = datetime.now() + pd.DateOffset(seconds=int(rand_buff_time))
        window.update()

if __name__ == '__main__':
    window = tk.Tk()
    window.geometry("500x300")
    window.title("AutoOneButtonClicker")
    label_key = tk.Label(text="Which Key")
    entry_key = tk.Entry()
    label_key.pack()
    entry_key.pack()
    label_min_time = tk.Label(text="MIN Time in seconds")
    entry_min_time = tk.Entry()
    label_min_time.pack()
    entry_min_time.pack()
    label_max_time = tk.Label(text="MAX Time in seconds")
    entry_max_time = tk.Entry()
    label_max_time.pack()
    entry_max_time.pack()

    tk.Button(text="Start Loop", command=lambda: auto_clicker(entry_key.get(),
                                                              entry_min_time.get(),entry_max_time.get())).pack()
    tk.Button(text="Cancel", command=lambda: set_start_program(False)).pack()

    window.mainloop()

