import cv2 as c
img=c.imread("colour.jpeg",0)
print(img)
c.imshow("output",img)
c.waitKey(500000000)
c.imwrite("bw color.png".img)
c.destroyAllWindows()