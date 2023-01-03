import cv2 as cv
from PIL import Image
import os
import numpy as np
import shutil

"""
1 Stworzyć folder -> image_dir
2 Uruchomić ten program
3 Klikajac spacje przechodzimy do kolejnych ujęć
4 W ujęciach gdzie mamy znalezioną twarz (niebieski prostokąt), można kliknąć 's' i zapisze się zdjecie
5 Potrzeba mi dużo troche takich zdjec z twarza z roznych ujec, swiatla itd., na koniec spakować do rara i wrzucić na gita/msg
"""
image_dir = ".\\train_images\\new\\"

cam = cv.VideoCapture(0)
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')


# 0 - brak usera, 1 - Jakub, 2 - Kacper 
label = '2'

it = 0
while 1:
    it = it + 1  
    result, image = cam.read()
    copy = image.copy()
    
   
    if result:
        gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3,
                                              minNeighbors=3,
                                              minSize=(30, 30),
                                              flags=cv.CASCADE_SCALE_IMAGE)
        key_code = 0

        if len(faces) > 0:
            (x,y,w,h) = faces[0]
            cv.rectangle(image, (x,y), (x+w,y+h),(255,0,0),2)
            cv.imshow('Frame', image)
            key_code = cv.waitKey(0)

            if key_code & 0xFF == ord('s'):
                cv.destroyAllWindows()
                image_path = image_dir + "image_" + str(it) + "_class_" + label + ".png"
                cv.imwrite(image_path, copy)
        else:
            cv.imshow('Frame', image)
            key_code = cv.waitKey(0)


        if key_code & 0xFF == ord('q'):
            exit(0)


'''


allFileNames = os.listdir(path="./train_images/own")
np.random.shuffle(allFileNames)
train_FileNames, val_FileNames, test_FileNames = np.split(np.array(allFileNames), [int(len(allFileNames)*0.7), int(len(allFileNames)*0.85)] )
print('Total images: ', len(allFileNames))
print('Training: ', len(train_FileNames))
print('Validation: ', len(val_FileNames))
print('Testing: ', len(test_FileNames))

for name in train_FileNames:
    shutil.copy("./train_images/own/" + name, "D:\\materialy_pwr\\2 stopien\\sem2\\SysMultimedialne\\Projekt\\multimedia_project\\train_images\\own_dataset\\train")

for name in test_FileNames:
    shutil.copy("./train_images/own/" + name, "D:\\materialy_pwr\\2 stopien\\sem2\\SysMultimedialne\\Projekt\\multimedia_project\\train_images\\own_dataset\\test")

for name in val_FileNames:
    shutil.copy("./train_images/own/" + name, "D:\\materialy_pwr\\2 stopien\\sem2\\SysMultimedialne\\Projekt\\multimedia_project\\train_images\\own_dataset\\validate")    
'''
