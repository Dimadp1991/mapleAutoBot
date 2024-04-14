from time import sleep
import pydirectinput
import keyboard
import tkinter as tk
import threading

import pandas as pd
from datetime import datetime


# creating executable
# pyinstaller - -onefile --noconsole autoClick.py


class AutoPlayerReboot:

    def __init__(self) -> None:
        self.__window = tk.Tk()
        self.__start_program = True
        self.__auto_click = False
        self.__buff_press_key = None
        self.__attack_key = None
        self.__start_stop_key = None
        self.__buff_keys = None
        self.__intervals = {}
        self.__build_window()

    def __build_window(self):
        self.__window.geometry("500x300")
        photo = tk.PhotoImage(file="C:\\Users\\dimap\\Desktop\\AutoMSPlayer\\maplestory-256x256.png")
        self.__window.iconphoto(False, photo)
        self.__window.title("AutoMapleClicker")
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
        label_start_stop = tk.Label(text="Start\\Stop Attacking key")
        entry_start_stop = tk.Entry()
        label_start_stop.pack()
        entry_start_stop.pack()

        tk.Button(width="10", text="Start",
                  command=lambda: self.__run_auto_play(entry_buff, entry_attack, entry_start_stop,
                                                       entry_buff_keys)).pack()
        tk.Button(text="Cancel", command=lambda: self.__set_start_program(False)).pack()

        interval_keys_to_press = tk.Label(text="Start\\Stop Attacking key")
        entry_start_stop = tk.Entry()
        label_start_stop.pack()
        entry_start_stop.pack()
        move_interval_bool = tk.BooleanVar()
        move_interval_bool.set(False)
        move_interval_checkbox = tk.Checkbutton(self.__window, text="Use Movement", variable=move_interval_bool)
        move_interval_checkbox.pack()

        self.__window.mainloop()

    def __auto_buff(self, buff_list):
        for key in buff_list:
            th1 = threading.Thread(target=self.press_button, args=[key])
            th1.start()
            th1.join()
            sleep(2)

    def __set_start_program(self, val):
        self.__start_program = val

    def __add_interval(self, keys, timing):
        self.__intervals[keys] = timing

    def __run_auto_play(self, entry_buff, entry_attack, entry_start_stop, entry_buff_keys):
        self.__buff_press_key = entry_buff.get()
        self.__attack_key = entry_attack.get()
        self.__start_stop_key = entry_start_stop.get()
        self.__buff_keys = entry_buff_keys.get()
        running_intervals = []
        for keys, timing in self.__intervals:
            current_time = datetime.now()
            running_intervals.append(current_time + pd.DateOffset(seconds=timing))

        while True:
            if not self.__start_program:
                return
            if keyboard.is_pressed(self.__start_stop_key):
                if not self.__start_program:
                    return
                pydirectinput.keyUp(key=self.__attack_key)
                self.__auto_click = not self.__auto_click
                # print(f"auto click = {auto_click}")
                sleep(0.5)
            if keyboard.is_pressed(self.__buff_press_key):
                self.__auto_buff(self.__buff_keys)
            if self.__auto_click:
                pydirectinput.keyDown(key=self.__attack_key)

            self.__window.update()

    @staticmethod
    def press_button(key):
        pydirectinput.keyDown(key=key)
        pydirectinput.keyUp(key=key)

    @staticmethod
    def fast_step_with_tp(self, side, tp_key):
        pydirectinput.keyDown(key=side)
        pydirectinput.keyDown(key=tp_key)
        pydirectinput.keyUp(key=tp_key)
        pydirectinput.keyUp(key=side)

    @staticmethod
    def double_jump(self, side, jump_key):
        pydirectinput.keyDown(key=side)
        pydirectinput.keyDown(key=jump_key)
        pydirectinput.keyUp(key=jump_key)
        pydirectinput.keyDown(key=jump_key)
        pydirectinput.keyUp(key=jump_key)
        pydirectinput.keyUp(key=side)

    @staticmethod
    def regular_jump(self, side, jump_key):
        pydirectinput.keyDown(key=side)
        pydirectinput.keyDown(key=jump_key)
        pydirectinput.keyUp(key=jump_key)
        pydirectinput.keyUp(key=side)

    @staticmethod
    def move_to_side(self, side, time):
        pydirectinput.keyDown(key=side)
        sleep(time)
        pydirectinput.keyUp(key=side)


if __name__ == '__main__':
    AutoPlayerReboot()


#  attack 5 -> tp left 2