from time import sleep
import pydirectinput
import keyboard
import tkinter as tk
import threading

global window
global start_program
import pandas as pd
from datetime import datetime

# creating executable
# pyinstaller --onefile --noconsole autoClick.py


def auto_buff(buff_keys):
    for key in buff_keys:
        pydirectinput.keyDown(key=key)
        sleep(2)
        pydirectinput.keyUp(key=key)


def set_start_program(val):
    global start_program
    start_program = val
    print(start_program)


def press_button(key):
    pydirectinput.keyDown(key=key)
    pydirectinput.keyUp(key=key)


def auto_clicker(buff_press_key, main_attack_key, aoe_attack_key,change_attack_key, start_stop_key, buff_keys):
    global start_program
    auto_click = False
    start_program = True
    attack_key=main_attack_key
    while True:
        # if cancel is pressed program will stop running
        if not start_program:
            return

        if keyboard.is_pressed(start_stop_key):
            sleep(0.3)
            pydirectinput.keyUp(attack_key)
            auto_click = not auto_click

        if keyboard.is_pressed(buff_press_key):
            auto_buff(buff_keys)

        if keyboard.is_pressed(change_attack_key):
            sleep(0.3)
            pydirectinput.keyUp(attack_key)
            attack_key= main_attack_key if attack_key == aoe_attack_key else aoe_attack_key

        if (
            auto_click
            and not keyboard.is_pressed("left")
            and not keyboard.is_pressed("right")
            and not keyboard.is_pressed("up")
            and not keyboard.is_pressed("down")
            and not keyboard.is_pressed("alt")
        ):
            pydirectinput.keyDown(key=attack_key)
        else:
            pydirectinput.keyUp(key=attack_key)

        window.update()


if __name__ == "__main__":
    pydirectinput.PAUSE = 0.06

    window = tk.Tk()
    window.geometry("500x300")
    label_buff = tk.Label(text="Buff key")
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
    aoe_label_attack = tk.Label(text="aoe attack key")
    aoe_entry_attack = tk.Entry()
    aoe_label_attack.pack()
    aoe_entry_attack.pack()
    change_attack = tk.Label(text="change attack key")
    entry_change_attack = tk.Entry()
    change_attack.pack()
    entry_change_attack.pack()
    label_start_stop = tk.Label(text="Start\Stop key")
    entry_start_stop = tk.Entry()
    label_start_stop.pack()
    entry_start_stop.pack()

    tk.Button(
        text="Start Loop",
        command=lambda: auto_clicker(
            entry_buff.get(),
            entry_attack.get(),
            aoe_entry_attack.get(),
            entry_change_attack.get(),
            entry_start_stop.get(),
            entry_buff_keys.get(),
        ),
    ).pack()
    tk.Button(text="Cancel", command=lambda: set_start_program(False)).pack()

    # tk.Button(text="Start Loop", command=lambda: auto_clicker("-","a",
    #                                                           "=", "c")).pack()
    # tk.Button(text="Cancel", command=lambda: set_start_program(False)).pack()

    window.mainloop()
