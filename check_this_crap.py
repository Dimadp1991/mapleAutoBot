from http.client import OK
import threading
import mouse
import keyboard
from time import sleep

mouse_events = []

sleep(3)
mouse.hook(mouse_events.append)
keyboard.start_recording()

keyboard.wait("=")

mouse.unhook(mouse_events.append)
keyboard_events = keyboard.stop_recording()

#Keyboard threadings:
while not keyboard.is_pressed("-"):
    # keyboard.play(keyboard_events)
    mouse.play(mouse_events)

#Mouse threadings:

# m_thread = threading.Thread(target = lambda :)
# m_thread.start()

#waiting for both threadings to be completedaaaaaaaa
