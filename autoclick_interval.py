from time import sleep
import pydirectinput
import keyboard
import tkinter as tk
import threading
global window
global start_program
import pandas as pd
from  datetime import datetime
# creating executable
# pyinstaller --onefile --noconsole autoClick.py


def set_start_program(val):
    global start_program
    start_program = val
    # print(start_program)

def press_button(key):
    pydirectinput.keyDown(key=key)
    pydirectinput.keyUp(key=key)


def auto_clicker(press_key,time_interval):
    sleep(3)
    global start_program
    start_program = True
    current_time=datetime.now()
    time_interval = current_time + pd.DateOffset(minutes=float(time_interval))
    while True:
        if not start_program: return
        if start_program and datetime.now() >= time_interval:
                sleep(0.5)
                pydirectinput.keyDown(press_key)
                sleep(3)
                pydirectinput.keyUp(press_key)

        window.update()

if __name__ == '__main__':
    window = tk.Tk()
    window.geometry("500x300")
    photo = tk.PhotoImage(file = "C:\\Users\\dimap\\Desktop\\AutoMSPlayer\\maplestory-256x256.png")
    window.iconphoto(False,photo)
    window.title("AutoOneButtonClicker")
    label_key = tk.Label(text="Which Key")
    entry_key = tk.Entry()
    label_key.pack()
    entry_key.pack()
    label_time = tk.Label(text="Time in minutes")
    entry_time = tk.Entry()
    label_time.pack()
    entry_time.pack()

    tk.Button(text="Start Loop", command=lambda: auto_clicker(entry_key.get(),entry_time.get())).pack()
    tk.Button(text="Cancel", command=lambda: set_start_program(False)).pack()

    window.mainloop()

