from time import sleep
import pydirectinput
import keyboard
import tkinter as tk

global window
global start_program


def AutoBuff():
    pydirectinput.keyDown("c")
    sleep(2)
    # pydirectinput.keyDown("d")
    # sleep(2)
    pydirectinput.keyDown("v")
    sleep(3)
    # pydirectinput.keyDown("n")
    # sleep(3)


def set_start_program(val):
    global start_program
    start_program = val
    print(start_program)


def auto_clicker(buff_key, attack_key, start_stop_key):
    global start_program
    auto_click = False
    start_program = True
    while True:
        if not start_program: return
        if keyboard.is_pressed(start_stop_key):
            if not start_program: return
            pydirectinput.keyUp(attack_key)
            auto_click = not auto_click
            # print(f"auto click = {auto_click}")
            sleep(0.5)
        if keyboard.is_pressed(buff_key):
            # print(f"buffing...")
            AutoBuff()
        if auto_click:
            pydirectinput.keyDown(attack_key)
        window.update()


if __name__ == '__main__':
    window = tk.Tk()
    window.geometry("500x200")
    label_buff = tk.Label(text="Buff key")
    entry_buff = tk.Entry()
    label_buff.pack()
    entry_buff.pack()
    label_attack = tk.Label(text="attack key")
    entry_attack = tk.Entry()
    label_attack.pack()
    entry_attack.pack()
    label_start_stop = tk.Label(text="Start\Stop key")
    entry_start_stop = tk.Entry()
    label_start_stop.pack()
    entry_start_stop.pack()

    tk.Button(text="Start Loop", command=lambda: auto_clicker(entry_buff.get(), entry_attack.get(),
                                                              entry_start_stop.get())).pack()
    tk.Button(text="Cancel", command=lambda: set_start_program(False)).pack()

    window.mainloop()
