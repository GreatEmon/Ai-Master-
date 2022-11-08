import cv2 
img = cv2.imread("sample.jpg")
grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow("Test",grayImg)

cv2.waitKey(0)

cv2.destroyAllWindows()