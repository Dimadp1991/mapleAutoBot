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


global side
global auto_click_a
global fixed_spot_pos

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

def get_position_from_minimap()->Point:

    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    cv2.imwrite("in_memory_to_disk.png", image)

    # mapsize_short=5, 100,160,100
    # mapsize_short=5, 100,120,70 bb map 
    # mapsize_short=5, 40,160,70 # rto43
    # mapsize_short=5, 40,110,70 # bbs
    # mapsize_short=5, 40,110,90 # bbs
    mapsize_short=5, 40,150,110
    # mapsize_short=5, 50,160,100 #tiger ridge
    # mapsize_short=10, 100,100,30 #fdh
    # mapsize_short=5, 50,160,100 #fes 2
    # mapsize_short=5, 50,160,100
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

def press_button(key,how_many=10):
    pydirectinput.PAUSE=0.05
    for _ in range(how_many):
        pydirectinput.keyDown(key)
        pydirectinput.keyUp(key)


def auto_buff():
    pydirectinput.keyDown("c")
    sleep(2.5)
    pydirectinput.keyUp("c")
    pydirectinput.keyDown("v")
    sleep(1.5)
    pydirectinput.keyUp("v")




def fix_current_position(fixed_spot_pos,current_pos,side):
    # + = right
    # - = left
    RUN_TIME=0.5
    KIZUZ=100
    ATTACK_SIDE="right"
    moved=False
    while current_pos.x  <= fixed_spot_pos.x -KIZUZ or current_pos.x  >= fixed_spot_pos.x +KIZUZ:
        if current_pos.x  <= fixed_spot_pos.x -KIZUZ:
            pydirectinput.keyUp(side)   
            pydirectinput.keyUp(side)   
            side="right"
            pydirectinput.keyDown(side)
            sleep(RUN_TIME)
            pydirectinput.keyUp(side)
            moved=True



        if current_pos.x  >= fixed_spot_pos.x +KIZUZ:
            pydirectinput.keyUp(side)   
            pydirectinput.keyUp(side)   
            side="left"
            pydirectinput.keyDown(side)
            sleep(RUN_TIME)
            pydirectinput.keyUp(side)
            moved=True
            


        
        current_pos=get_position_from_minimap()
    
    if moved:
        pydirectinput.keyDown(ATTACK_SIDE)  #attack side to face mobs when attacking
        sleep(0.2)
        pydirectinput.keyUp(ATTACK_SIDE)    


    # pydirectinput.keyUp(side)   
    # pydirectinput.keyUp(side)

        






def run_test_one_line_map():
    fixed_spot_pos=Point(75,62)
    
    pydirectinput.PAUSE=0.06
    pydirectinput.FAILSAFE=False
    sleep(3)
    
    interval_stuck = datetime.now() + pd.DateOffset(minutes=1.3)
    interval_buff = datetime.now() + pd.DateOffset(minutes=3)
    interval_move = datetime.now() + pd.DateOffset(seconds=10)
    interval_cap_pos = datetime.now() + pd.DateOffset(seconds=2)
    auto_click_a = True
    side="right"
    attack_key="d"
    speed_pixels =150
    attack_th = None
    fix_applied=False  
    random_int=0
    current_pos=get_position_from_minimap()
    while True:
        if auto_click_a and datetime.now() >= interval_buff:
          pydirectinput.keyUp(side)   
          pydirectinput.keyUp(attack_key)   
          auto_buff()  
          interval_buff = datetime.now() + pd.DateOffset(minutes=3)
        
        if datetime.now() >= interval_cap_pos:  
            # pydirectinput.keyUp(attack_key)    
            # pydirectinput.keyUp(attack_key)    
            current_pos=get_position_from_minimap()
            fix_current_position(fixed_spot_pos,current_pos,side)
                
            interval_cap_pos = datetime.now() + pd.DateOffset(seconds=2)
        
        
            # if  datetime.now() >= interval_stuck:
            #     pydirectinput.keyUp(attack_key)
            #     pydirectinput.keyUp(attack_key)
            #     sleep(0.5)
            #     pydirectinput.keyDown("right")
            #     pydirectinput.keyUp("right")
            #     pydirectinput.keyDown("left")
            #     pydirectinput.keyUp("left")
            #     interval_stuck = datetime.now() + pd.DateOffset(minutes=1.3)


        # if auto_click_a and \
        #     not keyboard.is_pressed('up')  \
        #     and not keyboard.is_pressed('down') \
        #     and not keyboard.is_pressed('alt') \
        #     and not keyboard.is_pressed('left') \
        #     and not keyboard.is_pressed('right'):    
                    
        pydirectinput.keyDown(attack_key)  

            
        
        # print(get_position_from_minimap())
        if keyboard.is_pressed("="):
            if  attack_th:
                    attack_th.join()
                    attack_th=None
            pydirectinput.keyUp(attack_key)
            auto_click_a = not auto_click_a
            auto_pick_up= False
            print("auto_pick_up: ",auto_pick_up)
            print("= Clicked status is: ",auto_click_a)
            sleep(2)
        if keyboard.is_pressed("]"):
            fixed_spot_pos=get_position_from_minimap()
            print(f"new position set to {fixed_spot_pos} ")

        if keyboard.is_pressed("-"):
            attack_key= "d" if  attack_key=="a" else "a"
            print(f"attack  key is {attack_key} ")


run_test_one_line_map()