import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # red color
    lowRed = np.array([161, 155, 84])
    highRed = np.array([179, 255, 255])
    red_mask = cv2.inRange(hsv_frame, lowRed, highRed)
    red = cv2.bitwise_and(frame,frame,mask=red_mask)

    # Blue color
    lowBlue = np.array([94, 80, 2])
    highBlue = np.array([126, 255, 255])
    blue_mask = cv2.inRange(hsv_frame, lowBlue, highBlue)
    blue = cv2.bitwise_and(frame, frame, mask=blue_mask)

    # Green Color
    lowGreen = np.array([25, 52, 72])
    highGreen = np.array([102, 255, 255])
    green_mask = cv2.inRange(hsv_frame, lowGreen, highGreen)
    green = cv2.bitwise_and(frame, frame, mask=green_mask)

    # Every color except white
    low = np.array([0, 42, 0])
    high = np.array([179, 255, 255])
    mask = cv2.inRange(hsv_frame, low, high)
    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("web_cam", frame)
    # cv2.imshow("red mask", red)
    # cv2.imshow("blue mask", blue)
    # cv2.imshow("green mask", green)
    # cv2.imshow("no white", mask)

    key = cv2.waitKey(1)
    # if we press Esc the program gets terminated
    if key == 27:
        break
