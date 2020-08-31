#programming_fever
import cv2
import numpy as np
import pandas as pd
import pyautogui
import time

img_path = "d.png"
img = cv2.imread(img_path)
img=cv2.resize(img,(700,700)) #Maybe take away

score = 0
previous = 0
clicked = False
r = g = b = xpos = ypos = 0

#Reading csv file with pandas and giving names to each column
index=["color","color_name","hex","R","G","B"]
csv = pd.read_csv('colors.csv', names=index, header=None)

#function to calculate minimum distance from all colors and get the most matching color
def getColorName(R,G,B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R- int(csv.loc[i,"R"])) + abs(G- int(csv.loc[i,"G"]))+ abs(B- int(csv.loc[i,"B"]))
        if(d<=minimum):
            minimum = d
            cname = csv.loc[i,"color_name"]
    return cname

#function to get x,y coordinates of mouse double click
def draw_function(event, x,y,flags,param):
    global b,g,r,xpos,ypos, clicked, score, previous
    clicked = True
    xpos = x
    ypos = y
    b,g,r = img[y,x]
    b = int(b)
    g = int(g)
    r = int(r)

    if r != 4 or g != 255:
        previous = (r + g + b)
        #print(previous)

    if (r == 4 and g == 255) and (previous != 259): #Maybe change to rgb for more accuracy.
        score = score + 1
        previous = (r + g + b)
        #print(previous)
    print(score)

cv2.namedWindow('color detection by programming_fever')

while True: #change by putting an if statement inside.

    time.sleep(.07)
    x, y = pyautogui.position()

    #View The Positioning Of The Cursor.
    #posStr = "X: " + str(x).rjust(4) + "Y: " + str(y).rjust(4)
    #print(posStr, end = '')
    #print('\b' * len(posStr), end = '', flush = True)

    cv2.setMouseCallback('color detection by programming_fever',draw_function)

    cv2.imshow("color detection by programming_fever",img)


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

    if cv2.waitKey(20) & 0xFF ==27:
        break

cv2.destroyAllWindows()
