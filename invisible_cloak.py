import cv2
import numpy as np

cap=cv2.VideoCapture(0)
back = cv2.imread('./image.jpg')

#hsv=hue--hue represents the color, saturation represents what amount to which the color mixed with white color
    #value represents to what amount the color is mixed with the black color
    #why using hsv not rgb??
    #bcoz hsv models describes the colors as how the human eye tends to see the colors or a mixture of colors and how much intensity is being projected on an object
    #rgb describes the color as the combination of primary colors

while cap.isOpened():
    #take each frame
    ret, frame = cap.read() #frame is what camera is reading
    

    if ret:
        #how do we convert rgb into hsv
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        #cv2.imshow("hsv", hsv)
        #how to get hsv value
        #lower:hue-10,100,100, higher:h+10,255,255
        red = np.uint8([[[0,0,255]]]) #bgr value of red
        hsv_red  = cv2.cvtColor(red, cv2.COLOR_BGR2HSV)
        # get hsv value of red from bgr
        #print(hsv_red)

       # threshold the hsv value to get only red colors
       #below are ranges for red color and i want whatever color fall in between the ranges to remove
        l_red = np.array([0,100,100])
        u_red = np.array([10,255,255])

        #here we are detecting only the red and turning it into white white as ignoring others and tuning into blck
        mask= cv2.inRange(hsv, l_red, u_red) #only color which lying in this range take only those colors and ignore other colors
        #cv2.imshow("mask", mask)

        #all things red and ignore others things
        part_1 = cv2.bitwise_and(back, back, mask=mask) #bitwiseand just replacing the value hidden by red cloth with what is in bg and everythin is black other tha red only red chnges to bg image
        #cv2.imshow("part_1", part_1)
        
        mask = cv2.bitwise_not(mask)#doing opposite of mask ignoring red and detecting other things

        #all the things which are not red we need to display them also bcos so far its just ignoring things(trun into blck) which are not red and masking only red part with bg image
        #all things not red
        part_2 = cv2.bitwise_and(frame,frame, mask=mask)
        #cv2.imshow("mask", part_2)

        cv2.imshow("cloak",part_1+part_2)

        if cv2.waitKey(5)==ord('q'): 
            break


cap.release()
cv2.destroyAllWindows()
