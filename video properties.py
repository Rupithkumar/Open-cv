import  cv2 as cv
cap=cv.VideoCapture(0)
print('width: ',cap.get(cv.CAP_PROP_FRAME_WIDTH))
print('heigth: ',cap.get(cv.CAP_PROP_FRAME_HEIGHT))
cap.set(3,3000)
cap.set(4,2000)
while True:
    success,frame=cap.read()
    cv.imshow('output',frame)

    if cv.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()
cv.destroyAllWindows()