import cv2 as cv
cap=cv.VideoCapture(0)
while True:
    success,frame=cap.read()
    width=int(cap.get(3))
    height=int(cap.get(4))
    img=cv.line(frame,(0,0),(width,height),(0,0,255),10)
    img=cv.arrowedLine(img,(0,width),(height,0),(0,255,0),10)
    img=cv.rectangle(img,(200,200),(400,400),(0,0,255),10,cv.LINE_8)
    img=cv.circle(img,(200,200),30,(0,255,255),10)
    cv.imshow("output",img)
    if cv.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()
cv.destroyAllWindows()