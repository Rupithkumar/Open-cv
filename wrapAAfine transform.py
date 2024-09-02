import cv2 as cv
import numpy as np

image=cv.imread('robo.jpg')
height,width=image.shape[:2]
quater_height=height/4
quater_width=width/4
T=np.float32([[1,0,quater_width],[0,1,quater_height]])
img_translation=cv.warpAffine(image,T,(width,height))
cv.imshow('originalimage',image)
cv.imshow('transition_image',img_translation)
cv.waitKey(0)
cv.destroyAllWindows()