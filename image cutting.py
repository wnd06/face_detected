import cv2
import numpy as np
import os

path_dir = "summer"
file_list = os.listdir(path_dir)

file_name_list = []

for i in range(len(file_list)):
    file_name_list.append(file_list[i].replace(".jpg",""))
def Cutting_face_save(image, name):
    face_cascade = cv2.CascadeClassifier("./haarcascade_frontalface_default.xml")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        # cv2.rectangle(image, (x,y), (x+w, y+h), (255,0,0), 2)
        cropped = image[y: y+h, x: x+w]
        resize = cv2.resize(cropped, (180,180))

        cv2.imwrite(f"cutting_faces/summer/{name}.jpg", resize)

for name in file_name_list:
    img = cv2.imread("summer/" + name + ".jpg")
    #print(img)
    Cutting_face_save(img, name)












