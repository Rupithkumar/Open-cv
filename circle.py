import cv2 as cv
img=cv.imread("robo.jpg",1)
img=cv.circle(img,(255,255),100,(0,0,255),4)
print(img)
cv.imshow("output",img)
cv.waitKey(2000)
cv.destroyAllWindows()