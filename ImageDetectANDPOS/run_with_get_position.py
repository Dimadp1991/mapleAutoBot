import pyautogui
import cv2
import numpy as np
from time import sleep
import pydirectinput
import math
import keyboard
from datetime import datetime
import pandas as pd
import threading


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def distance_to(self, other_point):
        if not isinstance(other_point, Point):
            raise ValueError("Can only calculate distance to another Point object")
        
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

    
    def distance_to_x(self, other_point):
        if not isinstance(other_point, Point):
            raise ValueError("Can only calculate distance to another Point object")
        print(self.x,other_point.x)
        return self.x - other_point.x
    
    def distance_to_y(self, other_point):
        if not isinstance(other_point, Point):
            raise ValueError("Can only calculate distance to another Point object")
        
        return   other_point.y-self.y
    
    def __repr__(self):
        return f"Point({self.x}, {self.y})"

def get_position_from_minimap():

    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    cv2.imwrite("in_memory_to_disk.png", image)


    mapsize_short=20, 50,130,60
    # mapsize_wide=5, 50, 250, 120 
    x, y, w, h = mapsize_short  # Example coordinates; adjust as needed

    # Crop the region of interest
    cropped_image = image[y:y+h, x:x+w]

    # Display the cropped image
    # cv2.imshow('Cropped Image', cropped_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Optionally, save the cropped image
    cv2.imwrite('cropped_image.png', cropped_image)

    zoom_factor = 8  # Increase this value to zoom in more
    zoomed_roi = cv2.resize(cropped_image, None, fx=zoom_factor, fy=zoom_factor, interpolation=cv2.INTER_LINEAR)

    hsv_image = cv2.cvtColor(zoomed_roi, cv2.COLOR_BGR2HSV)

    # Split the HSV image into individual channels
    h, s, v = cv2.split(hsv_image)

    # Adjust the HSV values
    # For example, increase Hue by 10, Saturation by 20, and Value by 30
    # h = cv2.add(h,10)
    # s = cv2.add(s, 40)
    v = cv2.add(v, -140)

    # Merge the channels back together
    adjusted_hsv = cv2.merge([h, s, v])

    # Convert the adjusted HSV image back to BGR
    adjusted_image = cv2.cvtColor(adjusted_hsv, cv2.COLOR_HSV2BGR)

    # Convert BGR to HSV
    hsv = cv2.cvtColor(adjusted_image, cv2.COLOR_BGR2HSV)



    # Define range of yellow color in HSV
    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([30, 255, 255])
    
    # ------------------------------------------------------------------------
    
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

    # Apply morphological operations to reduce noise
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw contours on the original image
    for contour in contours:
        # Filter contours by area to remove small artifacts
        area = cv2.contourArea(contour)
        if area > 500:  # Adjust the threshold based on your needs
            # Approximate the contour to reduce the number of points
            epsilon = 0.02 * cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, epsilon, True)

            # Draw the contour in yellow color
            cv2.drawContours(adjusted_image, [approx], -1, (0, 255, 255), 4)
            moments = cv2.moments(contour)
            
            # Calculate the centroid of the contour
            if moments["m00"] != 0:
                cX = int(moments["m10"] / moments["m00"])
                cY = int(moments["m01"] / moments["m00"])
                
                p=Point(x=cX,y=cY)
                # Print the position of the detected yellow dot
                # print(f"({p.x},{p.y}) ")
                return p
            
            
#     cv2.imshow('Centered Image', adjusted_image)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

# get_position_from_minimap()

# while True: 
#     get_position_from_minimap()
#     sleep(5)



def press_button(key,how_many=10):
    pydirectinput.PAUSE=0.05
    for _ in range(how_many):
        pydirectinput.keyDown(key)
        pydirectinput.keyUp(key)


def run_test_one_line_map():
        
    pydirectinput.PAUSE=0.06
    pydirectinput.FAILSAFE=False
    sleep(3)

    left_dot= Point(143,152) 
    right_dot= Point(823,175) 
    
    interval_move = datetime.now() + pd.DateOffset(seconds=5)
    auto_click_a = True
    side="right"
    attack_key="a"
    speed_pixels =150
    attack_th = None
    while True:
        # if auto_click_a and datetime.now() >= interval_move:
            # attack_th=StoppableThread(target=press_button,args=[attack_key],daemon=True)
            # attack_th.start()
        current_pos=get_position_from_minimap()
        if not attack_th:   
            # print("starting thread") 
            attack_th=threading.Thread(target=press_button,args=[attack_key],daemon=True)
            attack_th.start()


        # pydirectinput.keyUp(attack_key)   
        # pydirectinput.keyUp(attack_key)  
        if current_pos.x -speed_pixels <= left_dot.x:
            sleep(0.5)
            attack_th.join()
            attack_th=None
            pydirectinput.keyUp(side)   
            pydirectinput.keyUp(side)   
            side="right"
    

        if current_pos.x+speed_pixels >= right_dot.x:
            sleep(0.5)
            attack_th.join()
            attack_th=None
            pydirectinput.keyUp(side)   
            pydirectinput.keyUp(side)   
            side="left"   
        pydirectinput.keyDown(side)
        pydirectinput.keyDown("a")      
        pydirectinput.keyDown("space")    
        pydirectinput.keyUp("a") 
        pydirectinput.keyDown("space")    
  
                     
        
        # print(get_position_from_minimap())
        if keyboard.is_pressed("="):
            
            pydirectinput.keyUp(attack_key)
            auto_click_a = not auto_click_a
            auto_pick_up= False
            print("auto_pick_up: ",auto_pick_up)
            print("= Clicked status is: ",auto_click_a)
        if keyboard.is_pressed("]"):
            auto_pick_up= not auto_pick_up
            print("auto_pick_up: ",auto_pick_up)

        if keyboard.is_pressed("-"):
            attack_key= "d" if  attack_key=="a" else "a"
            print(f"attack  key is {attack_key} ")


run_test_one_line_map()