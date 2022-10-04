import pydirectinput
import keyboard
from time import sleep

def fast_step_with_jump(side,how_many):
    
  for i in range(how_many):  
        pydirectinput.keyDown(key=side)
        pydirectinput.keyDown(key='alt')
        pydirectinput.keyUp(key='alt')
        
        pydirectinput.keyDown(key='alt')
        pydirectinput.keyUp(key='alt')
        
        pydirectinput.keyUp(key=side)

while True:
    if keyboard.is_pressed('='):
        fast_step_with_jump('up',1)