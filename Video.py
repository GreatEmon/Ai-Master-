import cv2

url = "http://192.168.0.2:8080/shot.jpg"


while True:
    vs = cv2.VideoCapture(url)
    _,img = vs.read()
    cv2.imshow("Video Capture",img)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break
vs.release()
cv2.destroyAllWindows()