import os, cv2
import numpy as np
from PIL import Image

facial_recognizer = cv2.face.LBPHFaceRecognizer_create()
facial_classifier=cv2.CascadeClassifier('C:/Users/Admin/AppData/Local/Programs/Python/Python37/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')

def get_Images_Labels(path):
    # get the path of all the files in the folder
    imageLocation = [os.path.join(path, f) for f in os.listdir(path)]

    # create empty face list
    faceSamples = []

    # create empty id list
    Ids = []

    # It will loop all the images through imagepath and loading the unique ids and the images
    for imageLoc in imageLocation:
        # loading the image and converting it to gray scale
        pilimages = Image.open(imageLoc).convert('L')

        # converting PIL images into the numpy array
        ImageArray = np.array(pilimages, 'uint8')

        # get the unique id from the images (split using "."so, we get 3 token (User,id,samplenumber))
        Id = int(os.path.split(imageLoc)[-1].split(".")[1])

        # Extract the face from the training dataset or training image
        faces = facial_classifier.detectMultiScale(ImageArray)

        # if face is there then append that in the list with the unique id
        for (a, b, w, h) in faces:
            faceSamples.append(ImageArray[b:b + h, a:a + w])
            Ids.append(Id)
    return faceSamples, Ids

faces,Ids = get_Images_Labels('DataSets')
facial_recognizer.train(faces, np.array(Ids))
print("Successfully trained the dataset!!!")
facial_recognizer.write('C:/Users/Admin/Desktop/trainerr/trainer.yml')