import pydirectinput
import keyboard
from time import sleep






def auto_buff(buff_keys):
    for key in buff_keys:
        pydirectinput.keyDown(key=key)
        sleep(2)
        pydirectinput.keyUp(key=key)




start_stop_key="="
attack_key="a"
buff_press_key="-"
buff_keys="cn"


auto_click=False

pydirectinput.PAUSE=0.06

while True:
    if keyboard.is_pressed(start_stop_key):
        sleep(0.3)
        pydirectinput.keyUp(attack_key)
        auto_click = not auto_click

    if keyboard.is_pressed(buff_press_key):
        auto_buff(buff_keys)

    if auto_click and not keyboard.is_pressed('left') and not keyboard.is_pressed('right') \
    and not keyboard.is_pressed('up') and not keyboard.is_pressed('down') and not keyboard.is_pressed('alt'):
        pydirectinput.keyDown(key=attack_key)
    else:
        pydirectinput.keyUp(key=attack_key)

