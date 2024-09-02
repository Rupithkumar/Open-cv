import cv2 as cv
img=cv.imread("robo.jpg",1)
cv.line(img,(0,0),(200,200),(0,0,255),4)
print(img)
cv.imshow("output",img)
cv.waitKey(2000)
cv.destroyAllWindows()