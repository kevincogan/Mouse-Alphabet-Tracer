import cv2
import pyautogui
import time

img = cv2.imread("d.png")

# variables
drawing = False

def draw_circle_with_drag(event, x, y, flags, param):
    global center_coordinates, radius, thickness, color, drawing, img
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

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.circle(img, center_coordinates, radius, color, thickness)

cv2.namedWindow('Word Tracing Game')
cv2.setMouseCallback('Word Tracing Game', draw_circle_with_drag)

while True:
    cv2.imshow('Word Tracing Game', img)
    if cv2.waitKey(10) == 27:
        break
cv2.destroyAllWindows()
