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
# pyinstaller - -onefile --noconsole autoClick.py


def auto_buff(buff_list):
    for key in buff_list:
        th1=threading.Thread(target=press_button,args=[key])
        th1.start()
        th1.join()
        sleep(2)


def set_start_program(val):
    global start_program
    start_program = val
    print(start_program)

def press_button(key):
    pydirectinput.keyDown(key=key)
    pydirectinput.keyUp(key=key)


def auto_clicker(buff_press_key,attack_key, start_stop_key, buff_keys):
    random_int=0
    global start_program
    auto_click = False
    start_program = True
    current_time=datetime.now()
    buff_interval = current_time + pd.DateOffset(minutes=3)
    while True:
        if not start_program: return
        if keyboard.is_pressed(start_stop_key):
            if not start_program: return
            pydirectinput.keyUp(attack_key)
            auto_click = not auto_click
            # print(f"auto click = {auto_click}")
            sleep(0.5)
        if keyboard.is_pressed(buff_press_key):
            pydirectinput.keyUp(key=attack_key)
            auto_buff(buff_keys)
        if auto_click:
            if not keyboard.is_pressed('up')  \
            and not keyboard.is_pressed('down') \
            and not keyboard.is_pressed('alt') \
            and not keyboard.is_pressed('left') \
            and not keyboard.is_pressed('right'):

   
                # pydirectinput.keyDown("left" if random_int % 2 == 0 else "right")
                # pydirectinput.keyUp("left" if random_int % 2 == 0 else "right")
                # sleep(0.15)
                pydirectinput.keyDown(key=attack_key)
                # pydirectinput.keyUp(key=attack_key)
                # sleep(0.35)
                # random_int+=1
     
            else:
                pydirectinput.keyUp(key=attack_key)
        window.update()


if __name__ == '__main__':
    window = tk.Tk()
    window.geometry("500x300")
    photo = tk.PhotoImage(file = "C:\\Users\\dimap\\Desktop\\AutoMSPlayer\\maplestory-256x256.png")
    window.iconphoto(False,photo)
    window.title("AutoMapleClicker")
    label_buff = tk.Label(text="Activate Buff key")
    entry_buff = tk.Entry()
    label_buff.pack()
    entry_buff.pack()
    label_buff_keys = tk.Label(text="buff keys")
    entry_buff_keys = tk.Entry()
    label_buff_keys.pack()
    entry_buff_keys.pack()
    label_attack = tk.Label(text="attack key")
    entry_attack = tk.Entry()
    label_attack.pack()
    entry_attack.pack()
    label_start_stop = tk.Label(text="Start\Stop Attacking key")
    entry_start_stop = tk.Entry()
    label_start_stop.pack()
    entry_start_stop.pack()

    # tk.Button(width="10",text="Start", command=lambda: auto_clicker(entry_buff.get(), entry_attack.get(),
    #                                                           entry_start_stop.get(), entry_buff_keys.get())).pack()
    # tk.Button(text="Cancel", command=lambda: set_start_program(False)).pack()

    tk.Button(text="Start Loop", command=lambda: auto_clicker("-","a",
                                                              "=", "c")).pack()
    tk.Button(text="Cancel", command=lambda: set_start_program(False)).pack()

    window.mainloop()
