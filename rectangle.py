import cv2 as cv
img=cv.imread("robo.jpg")
img=cv.rectangle(img,(100,100),(255,255),(0,0,255),4)
print(img)
cv.imshow("output",img)
cv.waitKey(2000)
cv.destroyAllWindows()