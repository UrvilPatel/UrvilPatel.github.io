import cv2
import xlwrite
import time

start = time.time()
time_period = 10

facial_classifier = cv2.CascadeClassifier('C:/Users/Admin/AppData/Local/Programs/Python/Python37/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
facial_recognizer = cv2.face.LBPHFaceRecognizer_create()
facial_recognizer.read('C:/Users/Admin/Desktop/trainerr/trainer.yml')

Id=0;
dict = {

}

cam = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_DUPLEX

# Start looping
while True:
    # Capture video frame
    ret, image_frame = cam.read();

    # Convert frame from RGB to grayscale image
    gray_image = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY);

    # Detect frames of different sizes, list of faces rectangles
    faces = facial_classifier.detectMultiScale(gray_image, 1.2, 5);

    # Loops for each faces
    for (a, b, w, h) in faces:
        #crop the image into rectangle and draw a outline surrounded by the face
        cv2.rectangle(image_frame, (a, b), (a + w, b + h), (0, 255, 0), 2);

        #predicting user ID and accuracy of the face
        Id, accuracy = facial_recognizer.predict(gray_image[b:b + h, a:a + w])

        if (accuracy < 60):

            if (Id == 1):
                Id = "Jhanvi"
                if ((str(Id)) not in dict):
                    #mark the attedance in the excel sheet
                    filename = xlwrite.make_sheet('attendance', 'classA_sheet', 1, Id, 'yes');
                    dict[str(Id)] = str(Id);

            elif (Id == 3):
                Id = "Urvil"
                if ((str(Id)) not in dict):
                    filename = xlwrite.make_sheet('attendance', 'classA_sheet', 3, Id, 'yes');
                    dict[str(Id)] = str(Id);

            elif (Id == 5):
                Id = "Maulik"
                if ((str(Id)) not in dict):
                    filename = xlwrite.make_sheet('attendance', 'classA_sheet', 5, Id, 'yes');
                    dict[str(Id)] = str(Id);
        else:
            Id = "Unknown"
        #writing the user name in the screen below the face
        cv2.putText(image_frame, str(Id), (a, b + h), font, 1, (0, 0, 255), 2)
    cv2.imshow('Capture Image Frame', image_frame);

    if time.time() > start + time_period:
        break;
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break;

# Stop video
cam.release()

# Close all started windows
cv2.destroyAllWindows()