import pyautogui
import cv2
import numpy as np
from time import sleep
import pydirectinput
import math

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
        
        return self.x - other_point.x
    
    def distance_to_y(self, other_point):
        if not isinstance(other_point, Point):
            raise ValueError("Can only calculate distance to another Point object")
        
        return self.y - other_point.y
    
    def __repr__(self):
        return f"Point({self.x}, {self.y})"

def get_position_from_minimap():

    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    cv2.imwrite("in_memory_to_disk.png", image)

    mapsize_short=5, 50, 120, 100 
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
    v = cv2.add(v, -100)

    # Merge the channels back together
    adjusted_hsv = cv2.merge([h, s, v])

    # Convert the adjusted HSV image back to BGR
    adjusted_image = cv2.cvtColor(adjusted_hsv, cv2.COLOR_HSV2BGR)

    # Convert BGR to HSV
    hsv = cv2.cvtColor(adjusted_image, cv2.COLOR_BGR2HSV)

    # Define range of yellow color in HSV
    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([30, 255, 255])
    
    

    # Threshold the HSV image to get only yellow colors
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Iterate through contours and filter for smaller contours (dots)
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 29:  # Adjust the area threshold as needed
            cv2.drawContours(adjusted_image, [contour], -1, (0, 255, 255), 2)  # Draw contour on original image
            moments = cv2.moments(contour)
            
            # Calculate the centroid of the contour
            if moments["m00"] != 0:
                cX = int(moments["m10"] / moments["m00"])
                cY = int(moments["m01"] / moments["m00"])
                
                p=Point(x=cX,y=cY)
                # Print the position of the detected yellow dot
                print(f"({p.x},{p.y}) ")
                # return p
            
            
    cv2.imshow('Centered Image', adjusted_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

get_position_from_minimap()

# while True: 
#     get_position_from_minimap()
#     sleep(5)


# print(Point(400,274).distance_to_x(Point(469, 274)))
