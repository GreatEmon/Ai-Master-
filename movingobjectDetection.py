import cv2 #image
import time #delay
import imutils #resize

url = "http://192.168.0.2:8080/shot.jpg"
cam = cv2.VideoCapture(url)  # Accessing camera -Initiate camera
time.sleep(1)  #1s of delay 

firstframe = None 
area = 500 #change in camera

while True:
    _,img = cam.read()  #read from camera
    text = "normal"
    img = imutils.resize(img,width=500)  #resize
    grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #convert to gray
    gaussianImg = cv2.GaussianBlur(grayImg,(21,21),0) #blur /smotothen
    
    if firstframe == None:
        firstframe = gaussianImg # capturing first frame
        continue
    
    imgDiff = cv2.absdiff(firstframe,gaussianImg) #Absolute Difference
    thresImg = cv2.threshold(imgDiff,25,255,cv2.THRESH_BINARY) # More accurate color
    thresImg = cv2.dilate(thresImg,None,iterations=2) #Find accurate difference - fill dot with color
    cnts= cv2.findContours(thresImg.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) #Find contours
    cnts = imutils.grab_contours(cnts) #Grabbing conturs
    
    for c in cnts:
        if cv2.contourArea(c) < area:
            continue
        (x,y,w,h) = cv2.boundingRect(c) #Getting rectangle details
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2) #drawing rectangle
        text = "moving"
        
    print(text)
    cv2.putText(img,text,(10,20),cv2.FONT_HERSHEY_COMPLEX_SMALL,0.5,(0,0,255),2) #Putting Text
    cv2.imshow("Video Capture",img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
cam.release()
cv2.destroyAllWindows()