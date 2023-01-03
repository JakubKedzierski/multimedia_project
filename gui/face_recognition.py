import cv2 as cv
from PIL import Image
import os
import numpy as np
import shutil

# LBH na całym obrazie


class FaceRecognizer():

    lbph_face_classifier = None
    face_cascade = None
    
    def __init__(self):
        self.lbph_face_classifier = cv.face.LBPHFaceRecognizer_create()
        self.lbph_face_classifier.read("lbph_classifier_own_only_face.yml")
        self.face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

    def live_recognition(self):
        cam = cv.VideoCapture(0)
        predictions = []

        while 1:  
            result, image = cam.read()
            cv.imshow('Rozpoznawanie twarzy', image)
            key_code = cv.waitKey(10)
            
            if key_code & 0xFF == ord(' '):
                image_copy = image.copy()
                if result:
                    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
                    faces_detected = self.face_cascade.detectMultiScale(gray, scaleFactor=1.3,
                                                        minNeighbors=3,
                                                        minSize=(30, 30),
                                                        flags=cv.CASCADE_SCALE_IMAGE)
                    if len(faces_detected) > 0:
                        (x,y,w,h) = faces_detected[0]
                        cv.rectangle(image_copy,(x,y),(x+w,y+h),(255,0,0),2)
                        crop_image = gray[y:y+h, x:x+w]
                        image_np = np.array(crop_image,'uint8')
                        predictions = self.lbph_face_classifier.predict(image_np)

                        print("Predykcja: ")
                        print("Klasa: " + str(predictions[0]))
                        print("P:" + str(predictions[1]))
                        print("----------------------")

                    else:
                        predictions = [0, 50]
                        print("Predykcja: ")
                        print("Klasa: " + str(0))
                        print("P: " + 'x')
                        print("----------------------")
                    
                    cv.imshow('Rozpoznawanie twarzy', image_copy)
                    key_code = cv.waitKey(0)
                    cv.destroyAllWindows()
                    break
                    
                else:
                    print("Something went wrong with camera\n")
        
        print("Koniec rozpoznawania twarzy")
        return predictions

    def test_image_recognition(self):
        test_image = './gui//test_data/' + 'image_1202_class_1.png'
        image = Image.open(test_image).convert('L')
        image_np_main = np.array(image,'uint8')
        faces_detected = self.face_cascade.detectMultiScale(image_np_main, scaleFactor=1.3,
                                            minNeighbors=3,
                                            minSize=(30, 30),
                                            flags=cv.CASCADE_SCALE_IMAGE)
        #expected_output = int(os.path.split(test_image)[1].split("_")[3].replace(".png"," "))
        predictions = []

        if len(faces_detected) > 0:
            (x,y,w,h) = faces_detected[0]
            cv.rectangle(image_np_main, (x,y),(x+w,y+h),(255,0,0),2)
            copy = image_np_main.copy()
            crop_image = copy[y:y+h, x:x+w]
            image_np = np.array(crop_image,'uint8')
            predictions = self.lbph_face_classifier.predict(image_np)

            print("Predykcja: ")
            print("Klasa: " + str(predictions[0]))
            #print("Prawdziwa klasa: " + str(expected_output))
            print("P:" + str(predictions[1]))
            print("----------------------")

        else:
            predictions = [0, 50]
            print("Predykcja: ")
            print("Klasa: " + str(0))
            #print("Prawdziwa klasa: " + str(expected_output))
            print("P: " + 'x')
            print("----------------------")


        cv.imshow("TEST", image_np_main)
        key_code = cv.waitKey(0)
        cv.destroyAllWindows()

        return predictions


