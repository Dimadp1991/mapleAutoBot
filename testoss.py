from random import randint
from time import sleep
from pip import main
import pydirectinput
from  datetime import datetime
import pandas as pd
import keyboard
import threading

while True:
    if keyboard.is_pressed("x"):
        pydirectinput.keyUp("a") 
        pydirectinput.keyDown("alt") 
        sleep(0.2)
        pydirectinput.keyDown("n") 
        pydirectinput.keyUp("alt")
        pydirectinput.keyUp("n")


        