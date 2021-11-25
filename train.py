# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 18:26:05 2021

@author: Kurniawan Sudirman
"""
import mysql.connector
import cv2
import face_recognition
import os
from mtcnn.mtcnn import MTCNN
import numpy as np
import mysql_connector as sq
from datetime import datetime
from statistics import mode
import tensorflow as tf
path= 'image'
images = []
classNim=[]
myList=os.listdir(path)
print(myList)

for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    cl = os.path.splitext(cl)[0].split("_")
    classNim.append(cl[0])
print(classNim)
#getName=sq.getRowsAllSpecific(classNim)
#print(images)


def findEncodings(images):
    encodeList=[]
    for img in images:
        img= cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode= face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

def markAttendance(name):
    with open('Attendance1.csv','r+') as f:
        myDataList = f.readlines()
        nameList=[]
        
        print(myDataList)
        for line in myDataList:
            entry = line.split(",")
            nameList.append(entry[2])
        if name not in nameList :
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            dateString=now.strftime('%d-%m-%y')
            nim='80'
            status='masuk'
            f.writelines(f'\n{nim},{dateString},{name},{dtString},{status}')
def markAttendanceIntoDB(name,nim):
    status="masuk"
    now = datetime.now()
    dtString = now.strftime('%H:%M:%S')
    dateString=now.strftime('%d-%m-%y')
    sq.insertRow(nim,dateString,name,dtString,status)
    
    
#q@tf.function(experimental_relax_shapes = True)
def recognition_face(encodeFrame, faces):
    for encodeFace,faceLocation in zip(encodeFrame,faces):
        matches=face_recognition.compare_faces(encodeListKnown, encodeFace)
        #print(matches)
        faceDis=face_recognition.face_distance(encodeListKnown, encodeFace)
        print(faceDis)
        matchesIndex=np.argmin(faceDis)
        
        
        #name=getName[matchesIndex].upper()
        nim=classNim[matchesIndex]
        #print(name)
        y1,x2,y2,x1=faceLocation
        #x1,y1, width, height = faceLocation['box']
        #x2,y2 = x1 + width, y1 + height
        print(x1,y1,x2,y2)
        
        #markAttendance(name)
        print(matches)
    
        if faceDis[matchesIndex]>=0.6:
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(img,(x1,y2-20),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(img,"Unknown",(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),2)
        else :
            if matches[matchesIndex]:
                nameDb = sq.getRowsSpecific(nim).upper()
                trueName.append(nameDb)
                trueNim.append(nim)
                longY=20
                fScale=0.5
                difLong=y2-y1
                if difLong<=70:
                    longY=15
                    fScale=0.3
                cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
                cv2.rectangle(img,(x1,y2-longY),(x2,y2),(0,255,0),cv2.FILLED)
                cv2.putText(img,nameDb,(x1+6,y2-6),cv2.FONT_HERSHEY_SIMPLEX,fScale,(255,255,255),2)
                markAttendanceIntoDB(mode(trueName),mode(trueNim))
                if len(trueName)>=7:
                    trueName.clear()
                    trueNim.clear()
                print(trueName)    
#@tf.function(experimental_relax_shapes = True)
def switchValue(faces):
    w,x,y,z = faces['box']
    temp = w
    w = x
    x = x + temp
    y = y + w
    z = temp
    
    
major_version = int(tf.__version__.split(".")[0])
print(tf.__version__)
print(major_version)
if major_version >= 2:
    from tensorflow.python import _pywrap_util_port
    print("MKL enabled:", _pywrap_util_port.IsMklEnabled())
else:
    print("MKL enabled:", tf.pywrap_tensorflow.IsMklEnabled())   
    
encodeListKnown=findEncodings(images)
print("Encoding Complete")
#print(encodeListKnown)
trueName=[]
trueNim=[]
cap=cv2.VideoCapture(0)
#detector = MTCNN()

while True:
    success,img=cap.read()
    imgResize=cv2.resize(img,(0,0),None,0.25,0.25)
    imgResize=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    faces=face_recognition.face_locations(imgResize)
    #print(f"nfaces : {nfaces}")
    #faces = detector.detect_faces(imgResize)
    #print(f"print faces before : {faces}")
    #newFaces=[]
    #for value in faces:
   #     newFaces.append(value['box'])
    #print(newFaces)
    #faces = map(switchValue,faces)
   # print(f"print faces after : {faces}")
    encodeFrame=face_recognition.face_encodings(imgResize,faces)
    
    recognition_face(encodeFrame, faces)
        
    cv2.imshow('webcam',img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()