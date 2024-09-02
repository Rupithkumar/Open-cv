import cv2 as cv
img1=cv.imread('colour.jpeg')
img2=cv.imread('robo.jpg')
img3=cv.resize(img1,(512,512))
img4=cv.resize(img2,(512,512))
dst=cv.add(img3,img4)
cv.imshow('output',dst)
cv.waitKey(0)
cv.destroyAllWindows()