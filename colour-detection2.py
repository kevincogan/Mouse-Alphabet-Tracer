#programming_fever
import cv2
import numpy as np
import pandas as pd
import pyautogui
import time

img_path = "d.png"
img = cv2.imread(img_path)
img=cv2.resize(img,(700,700)) #Maybe take away

#Variables
score = 0
previous = 0
clicked = False
drawing = False
r = g = b = xpos = ypos = 0

#Drawing Function
def draw_circle_with_drag(event, x, y, flags, param):
    global center_coordinates, radius, thickness, color, drawing, img,score
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        center_coordinates = (x, y)
        radius = 15
        color = (0, 0, 255)
        thickness = -1

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            center_coordinates = (x, y)
            cv2.circle(img, center_coordinates, radius, color, thickness)
            score_function( event ,x, y, score, previous)
            print(center_coordinates)
            #print()
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.circle(img, center_coordinates, radius, color, thickness)
        print(score_function( event ,x, y, score, previous))


#function to get x,y coordinates
def score_function(event,x, y, score, previous):
    #global b,g,r,xpos,ypos, clicked, score, previous
    clicked = True
    xpos = x
    ypos = y
    b,g,r = img[y,x]
    b = int(b)
    g = int(g)
    r = int(r)

    print("Score_function: ",x,y)
    print(r,g,b)

    if r != 4 or g != 255:
        previous = (r + g + b)
        #print(previous)
        return score

    if (r == 4 and g == 255) and (previous != 259): #Maybe change to rgb for more accuracy.
        score = score + 1
        previous = (r + g + b)
        #print(previous)
        return score
    #print(score)
#########################252252252252##########################################################
cv2.namedWindow('Word Tracing Game')
#Colour Detector
cv2.setMouseCallback('Word Tracing Game',score_function)
#Drawing On Image Function
cv2.setMouseCallback('Word Tracing Game', draw_circle_with_drag)

while True:
    cv2.imshow('Word Tracing Game',img)
    if cv2.waitKey(20) & 0xFF ==27:
        break
    if cv2.waitKey(10) == 27:
        break

cv2.destroyAllWindows()

###################################################################################
    #if (clicked):

        #cv2.rectangle(image, startpoint, endpoint, color, thickness)-1 fills entire rectangle
    #    cv2.rectangle(img,(20,20), (750,60), (b,g,r), -1)

    #Creating text string to display( Color name and RGB values )
    #    text = getColorName(r,g,b) + ' R='+ str(r) +  ' G='+ str(g) +  ' B='+ str(b)

        #cv2.putText(img,text,start,font(0-7),fontScale,color,thickness,lineType )
    #    cv2.putText(img, text,(50,50),2,0.8,(255,255,255),2,cv2.LINE_AA)

    #    #For very light colours we will display text in black colour

    #    if(r+g+b>=600):
    #        cv2.putText(img, text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)

    #    clicked=False
