import cv2 as cv
img =cv.imread("C:/Users/RUPITH KUMAR.N/Desktop/wallpaper/wallpaper5.jpg",0)
print(img)
cv.imshow("output",img)
cv.waitKey(2000)
cv.destroyAllWindows()