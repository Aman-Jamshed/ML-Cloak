import cv2
#This is my Webcam
cap=cv2.VideoCapture(0) #0 represents my webcam i.e its cap from my webcam

while cap.isOpened(): 
    ret, back = cap.read() #Here I am simply reading from my webcam
    if ret:
        #back is what the camera is reading
        # ret is what your camera is reading is succesful or not its generally true but one case when its false is when your camera isn't working
        cv2.imshow("image",back) #this is the camera popout means camera is showing
        if cv2.waitKey(5)==ord('q'): 
        #going to wait for 5ms and clck a picture then wait for 5ms
        #then again clck pic if you press q in between then it going to save the pic means and break out 
            #click and save the image
            cv2.imwrite('image.jpg',back)# saving back as the image of bg by name of image.jpg
            break

cap.release()
cv2.destroyAllWindows()

