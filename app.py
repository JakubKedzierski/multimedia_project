import cv2 as cv
  
cam = cv.VideoCapture(0)
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

while 1:  
    result, image = cam.read()
    if result:
        gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        
        for (x,y,w,h) in faces:
            cv.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)

        cv.imshow('img', image)
        key_code = cv.waitKey(0)
        cv.destroyAllWindows()
        
        if key_code & 0xFF == ord('q'):
            break

        
    
    else:
        print("Something went wrong with camera\n")