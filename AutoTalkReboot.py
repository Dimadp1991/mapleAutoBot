from time import sleep
import pydirectinput
from datetime import datetime
import pandas as pd
import keyboard
import threading
while True:
    if keyboard.is_pressed("y"):
        pydirectinput.keyUp("a")
        sleep(0.5)
        while True:
            pydirectinput.keyDown("y")
            pydirectinput.keyUp("y")
            if keyboard.is_pressed("y"):
                sleep(0.5)
                break  