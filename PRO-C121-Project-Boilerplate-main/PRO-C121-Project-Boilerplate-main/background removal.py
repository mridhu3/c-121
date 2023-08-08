# import cv2 to capture videofeed
import cv2

import numpy as np

# attach camera indexed as 0
camera = cv2.VideoCapture(0)

# setting framewidth and frameheight as 640 X 480
camera.set(3 , 640)
camera.set(4 , 480)

# loading the space image
space = cv2.imread('space element.jpg')

# resizing the space image as 640 X 480
space = cv2.resize(space , (640 , 480))

while True:

   
    status , frame = camera.read()

    if status:

        # flip it
        frame = cv2.flip(frame , 1)

        # converting the image to RGB for easy processing
        frame_rgb = cv2.cvtColor(frame , cv2.COLOR_BGR2RGB)

        # creating thresholds
        lower_bound = np.array([100,100,100])
        upper_bound = np.array([255,255,255])

        # thresholding image
        mask = cv2.inRange(frame_rgb, lower_bound, upper_bound)

        # inverting the mask
        mask = cv2.bitwise_not(mask)

        
        person = cv2.bitwise_and(frame, frame , mask = mask)

        
        final_image = np.where(person  ==  0 , space , person)

        
        cv2.imshow('frame' , final_image)

        
        code = cv2.waitKey(1)
        if code  ==  32:
            break


camera.release()
cv2.destroyAllWindows()