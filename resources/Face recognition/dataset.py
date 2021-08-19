from imutils import paths
import face_recognition
import pickle
import time
import cv2
import os
 
print("Creating data set ...")

imagePaths = list(paths.list_images('Face')) # Replace 'Face' with your name if you want, but it should match the name of the folder containing your images

knownEncodings = []
knownNames = []

for (i, imagePath) in enumerate(imagePaths):

    name = imagePath.split(os.path.sep)[-2]

    image = cv2.imread(imagePath)
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    boxes = face_recognition.face_locations(rgb,model='hog')

    encodings = face_recognition.face_encodings(rgb, boxes)

    for encoding in encodings:
        knownEncodings.append(encoding)
        knownNames.append(name)

data = {"encodings": knownEncodings, "names": knownNames}

f = open("face_enc", "wb")
f.write(pickle.dumps(data))
f.close()

print()
print("Data set created")
time.sleep(3)
