import cv2 as cv
from PIL import Image
import os
import numpy as np

lbph_face_classifier_path = "lbph_classifier.yml"
test_dir_images = "./train_images/yalafaces/test/"
show_image = False

lbph_face_classifier = cv.face.LBPHFaceRecognizer_create()
lbph_face_classifier.read(lbph_face_classifier_path)

all = 0
good = 0

for f in os.listdir(path=test_dir_images):
    test_image = test_dir_images + f
    image = Image.open(test_image).convert('L')
    image_np = np.array(image,'uint8')

    predictions = lbph_face_classifier.predict(image_np)
    expected_output = int(os.path.split(test_image)[1].split('.')[0].replace("subject"," "))
    
    print("Predykcja: ")
    print("Klasa: " + str(predictions[0]))
    print("Prawdziwa klasa: " + str(expected_output))
    print("P:" + str(predictions[1]))
    print("----------------------")

    all = all + 1
    if predictions[0] == expected_output:
        good = good + 1
    
    if show_image:
        cv.imshow(f, image_np)
        key_code = cv.waitKey(0)
        cv.destroyAllWindows()

print("Dokładność:"  + str(good/all))

