import cv2 as cv
img1=cv.imread('colour.jpeg')
img2=cv.imread('robo.jpg')
img3=cv.resize(img1,(512,512))
img4=cv.resize(img2,(512,512))
img=cv.addWeighted(img3,.5,img4,.5,0)
cv.imshow('output',img)
cv.waitKey(0)
cv.destroyAllWindows()