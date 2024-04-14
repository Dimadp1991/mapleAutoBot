import pyautogui
from time import sleep
import cv2
import numpy as np

sleep(2)
myScreenshot = pyautogui.screenshot()
myScreenshot.save('game_window_shot.png')

image_screen=cv2.imread(filename='game_window_shot.png',flags=cv2.IMREAD_UNCHANGED)
image_to_search=cv2.imread(filename='faceOnly.png',flags=cv2.IMREAD_UNCHANGED)

image_screen=cv2.cvtColor(image_screen, cv2.COLOR_BGR2GRAY)
image_to_search=cv2.cvtColor(image_to_search, cv2.COLOR_BGR2GRAY)

res=cv2.matchTemplate(image_screen,image_to_search,cv2.TM_CCOEFF_NORMED)
image_screen=cv2.imread(filename='game_window_shot.png',flags=cv2.IMREAD_UNCHANGED)
min_val,max_val,min_loc,max_loc=cv2.minMaxLoc(res)
# print(res)
w=image_to_search.shape[1]
h=image_to_search.shape[0]

# cv2.rectangle(image_screen,max_loc,(max_loc[0]+w,max_loc[1]+h),(0,255,255),2)
print("MAX VAL IS ", max_val)

threshold = 0.6
loc = np.where( res >= threshold) # filter the results
for pt in zip(*loc[::-1]): #pt marks the location of the match
    print(pt)
    cv2.rectangle(image_screen, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)


cv2.imshow('ScreenShot',image_screen)
cv2.waitKey()
cv2.destroyAllWindows()
# sleep(2)
# while True:
#     sleep(2)
#     res=pyautogui.locateOnWindow()
#     print(res)
#     if res != None:
#         pyautogui.moveTo(x=res.x,y=res.y)