import cv2
import os

# Detect object in video stream and detect human face by using Haarcascade Frontal Face classifiers
facial_detector = cv2.CascadeClassifier('C:/Users/Admin/AppData/Local/Programs/Python/Python37/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')

unique_face_id = input('Enter the unique id:')
# Start capturing the video
cam = cv2.VideoCapture(0)

# Initialize the sample face image
sampleNum=0

# Start looping
while (True):
    # Capture video frame
    ret, image_frame = cam.read()

    # Convert frame from RGB to grayscale image
    gray_image = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)

    # Detect frames of different sizes, list of faces rectangles
    faces = facial_detector.detectMultiScale(gray_image, 1.3, 5)

    # Loops for each faces
    for (a, b, w, h) in faces:
        # Crop the image frame into rectangle
        cv2.rectangle(image_frame, (a, b), (a + w, b + h), (0, 255, 0), 2)

        # Increment sample face image
        sampleNum = sampleNum + 1

    # Save the captured image into the datasets folder by using uique face id
    cv2.imwrite("DataSets/User." + unique_face_id + '.' + str(sampleNum) + ".jpg", gray_image[b:b + h, a:a + w])

    # It will show the bounded rectangle on the person's face
    cv2.imshow('Capture Image Frame', image_frame)

    # To stop taking video, press 'Enter'
    if cv2.waitKey(1) == 13:
        break

    # If image taken reach 50, it will automatically stop taking video and close the pop up
    elif sampleNum >= 50:
        print("Successfully Captured the images !!!")
        break

# Stop video
cam.release()

# Close all started windows
cv2.destroyAllWindows()
