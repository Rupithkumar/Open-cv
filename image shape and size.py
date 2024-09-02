import cv2 as cv
img=cv.imread("colour.jpeg",1)
print(img)
print(img.shape)
print(img.size)
cv.imshow("output",img)
cv.waitKey(20000)
cv.destroyAllWindows()