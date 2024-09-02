import cv2 as cv
img =cv.imread("robo.jpg",0)
print(img)
cv.imshow("output",img)
cv.waitKey(2000)
cv.destroyAllWindows()