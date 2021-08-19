# Project python file

import pygame
from pygame import mixer
import face_recognition
import imutils
import pickle
import time
import cv2
import serial                                     
import pyautogui
import random
import os
import sys

z = 0
l1 = 0
s1 = 0

Arduino_Serial = serial.Serial('COM9',9600)       # Initialize serial and Create Serial port object called Arduino_Serial

def write_read(x) :
    
    x=str(x)
    Arduino_Serial.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = str(Arduino_Serial.readline())
    print(data)

def verifyFace() : # face recognition function

    global z

    z = 0
    
    cascPathface = os.path.dirname(
     cv2.__file__) + "/data/haarcascade_frontalface_alt2.xml"

    faceCascade = cv2.CascadeClassifier(cascPathface)
    
    data = pickle.loads(open('face_enc', "rb").read())
 
    print("Streaming started")
    video_capture = cv2.VideoCapture(0)

    while True:

        ret, frame = video_capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(60, 60),flags=cv2.CASCADE_SCALE_IMAGE)

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        encodings = face_recognition.face_encodings(rgb)
        names = []

        for encoding in encodings:

            matches = face_recognition.compare_faces(data["encodings"], encoding)

            name = "Unknown"

            if True in matches:


                matchedIdxs = [i for (i, b) in enumerate(matches) if b]
                counts = {}

                for i in matchedIdxs:

                    name = data["names"][i]

                    counts[name] = counts.get(name, 0) + 1

                name = max(counts, key=counts.get)

                z = 1
 
            names.append(name)

            for ((x, y, w, h), name) in zip(faces, names):


                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, name+' .Press q', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)
                
        cv2.imshow("Frame", frame)
    
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    time.sleep(5)

    video_capture.release()
    cv2.destroyAllWindows()


def verifySecurity() :
    
    verifyFace()
    
    if z == 1 :

        pygame.init()
        y = mixer.Sound("identity_verified.mp3") # Paste The audio file location 
        y.play() 

    elif z == 0 :

        pygame.init()
        y = mixer.Sound("identity_unverified.mp3") 
        y.play() 
        sys.exit()

def playMusic() :
    
    pygame.init()
    ys = mixer.Sound("spectre.mp3") 
    ys.play()


def toggleLights() : # toggles secondary lights

    global l1

    l1 = not l1
    
    if l1 == 0 :

        write_read(0)

    elif l1 == 1 :

        write_read(1)


def choiceSelect(i) :

    
    if i == 1 : # check face for security
    
        verifySecurity()
        
    elif i == 2 : # secondary lights

        toggleLights()

    elif i == 3 : # plays a random track from folder

        playMusic()

a = 1

while 1:
    
    incoming_data = str (Arduino_Serial.readline()) # read the serial data and print it as line
    print(incoming_data)                           # print the incoming Serial data

    if 'security' in incoming_data:

        verifySecurity()

    if 'next' in incoming_data:                    # if incoming data is 'next'

        if a == 1 :

            # play voice (create new .py file to initialize audio)
            pygame.init()
            y = mixer.Sound("verify_security.mp3") 
            y.play()
            z = 0
            a += 1 

        elif a == 2 :

            # play voice (create new .py file to initialize audio)
            pygame.init()
            y = mixer.Sound("lights.mp3") 
            y.play()
            a += 1 

        elif a == 3 :

            # play voice (create new .py file to initialize audio)
            pygame.init()
            y = mixer.Sound("music_q.mp3") 
            y.play()
            a += 1 

        elif a > 3 :

           a = 1              
        
    if 'select' in incoming_data:                # if incoming data is 'select'

        choiceSelect(a-1)   

        
    incoming_data = "";                            # clears the data
