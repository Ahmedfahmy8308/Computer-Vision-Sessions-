import cv2
import os
import face_recognition
import numpy as np
import datetime

path = 'Faces'
images =[]
names=[]

mylist = os.listdir(path)

for img in mylist:
    curimage = cv2.imread(f"{path}/{img}")
    images.append(curimage)
    names.append(os.path.splitext(img)[0])

def encode (images):
    encodlist = []
    for img in images :
        imge = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(imge)[0]
        encodlist.append(encode)
    return encodlist
encodelist = encode(images)

def attend(name):
    with open ('Attendence.csv',"r+") as A :
        Datalist = A.readlines()
        namelist=[]
        for line in Datalist :
            name = line.split(',')[0]
            namelist.append(name)
        if name not in namelist:
            date = datetime.datetime.now()
            curtime = date.strftime('%H:%M:%S')
            A.writelines(f'\n{name} , {curtime}')

cap = cv2.VideoCapture(0)

while True :
    _ , img = cap.read()
    img = cv2.flip(img,1)

    imgr = cv2.resize(img , (0,0) , None ,0.25 , 0.25)
    imgr = cv2.cvtColor(imgr , cv2.COLOR_BGR2RGB)

    facecurframe = face_recognition.face_locations(imgr)
    encodecurframe = face_recognition.face_encodings(imgr ,facecurframe)

    for encodeface , faceloc in zip(encodecurframe ,facecurframe ):
        matches = face_recognition.compare_faces(encodelist , encodeface )
        facedis = face_recognition.face_distance(encodelist , encodeface)
        matcheindex = np.argmin(facedis)

        y1 , x2 , y2 , x1 = faceloc
        y1, x2, y2, x1 = (y1*4)-40  , (x2*4)+25 , (y2*4)+25 , (x1*4)-20
        cv2.rectangle(img , (x1 , y1) , (x2 , y2) , (0,255,0) , 2)
        cv2.rectangle(img , (x1,y2) ,(x2,y2+45) , (0,255,0) , -1)

        if matches[matcheindex]:
            name= names[matcheindex].upper()
            cv2.putText(img ,name ,(x1 +5,y2 +30 ) ,cv2.FONT_HERSHEY_COMPLEX ,.8,(0,0,0) , 2 )
            attend(name)


    cv2.imshow('frame' , img)
    if cv2.waitKey(1) == ord('q'):
        break









