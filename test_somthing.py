import pydirectinput
import keyboard
from time import sleep

# def fast_step_with_jump(side,how_many):
    
#   for i in range(how_many):  
#         pydirectinput.keyDown(key=side)
#         pydirectinput.keyDown(key='alt')
#         pydirectinput.keyUp(key='alt')
        
#         pydirectinput.keyDown(key='alt')
#         pydirectinput.keyUp(key='alt')
        
#         pydirectinput.keyUp(key=side)

# while True:
#     if keyboard.is_pressed('='):
#         fast_step_with_jump('up',1)
sleep(2)
# pydirectinput.keyDown(key="a")
# pydirectinput.keyDown(key="a")
# pydirectinput.keyDown(key="a")
# pydirectinput.keyUp(key="a")
# sleep(0.5)
# pydirectinput.keyDown(key="right")
# pydirectinput.keyUp(key="right")
# pydirectinput.keyDown(key="a")
# pydirectinput.keyDown(key="a")
# pydirectinput.keyDown(key="a")
# pydirectinput.keyUp(key="a")
# sleep(0.5)
# pydirectinput.keyDown(key="left")
# pydirectinput.keyUp(key="left")


# pydirectinput.keyDown("space")
# sleep(4)
# pydirectinput.keyDown("space")
# sleep(4)
# pydirectinput.keyDown("a")
# pydirectinput.keyUp("a")
# pydirectinput.keyDown("a")
# pydirectinput.keyUp("a")
# pydirectinput.keyDown("a")
# pydirectinput.keyUp("a")


# for i in range(3): 
#     pydirectinput.keyDown("right")
#     pydirectinput.keyDown("alt")
#     sleep(0.2)
#     pydirectinput.keyDown("x")
#     pydirectinput.keyUp("alt")
#     pydirectinput.keyUp("x")
#     pydirectinput.keyUp("right")




sleep(3)

pydirectinput.keyDown("enter")
sleep(1)
pydirectinput.keyUp("enter")

pydirectinput.keyDown("shift")
sleep(1)
pydirectinput.keyDown("2")
sleep(1)
pydirectinput.keyUp("shift")
sleep(1)
pydirectinput.keyUp("2")

pydirectinput.keyDown("m")
sleep(1)
pydirectinput.keyUp("m")

pydirectinput.keyDown("i")
sleep(1)
pydirectinput.keyUp("i")

pydirectinput.keyDown("u")
sleep(1)
pydirectinput.keyUp("u")

pydirectinput.keyDown("enter")
sleep(1)
pydirectinput.keyUp("enter")


sleep(2)
pydirectinput.moveTo(x=760, y=375)
sleep(2)
pydirectinput.click()
sleep(1)
pydirectinput.keyDown("enter")
sleep(1)
pydirectinput.keyUp("enter")
sleep(1)
pydirectinput.keyDown("esc")
sleep(1)
pydirectinput.keyUp("esc")