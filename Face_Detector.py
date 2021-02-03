import cv2 
from random import randrange

#load some pre-trained data on face frontals 
trained_data=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

"""
#choose an image to detect 
img=cv2.imread('IMG.jpg')


#convert the image to grayscale
grayscaled_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Detect Faces
face_Coordinates=trained_data.detectMultiScale(grayscaled_img)

#Draw Rectangles around the face where (0,255,0) is a color and 2 is the thikness
for (x,y,w,h) in face_Coordinates:
 cv2.rectangle(img, (x,y), (x+w, y+h), (randrange(128,256), randrange(128,256), randrange(128,256)), 2)

#show the image 
cv2.imshow('the first image from python',img)
cv2.waitKey()
"""

#for webcam use

webcam=cv2.VideoCapture(0)

#Itereate over frames
while True:
    #read the current frame
    successful_frame_read,frame=webcam.read()
    #convert to grayscaled
    grayscaled_img=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #Detect Faces
    face_Coordinates=trained_data.detectMultiScale(grayscaled_img)
    #Draw Rectangles around the face where (0,255,0) is a color and 2 is the thikness
    for (x,y,w,h) in face_Coordinates:
     cv2.rectangle(frame, (x,y), (x+w, y+h), (randrange(128,256), randrange(128,256), randrange(128,256)), 2)

    #show the image 
    cv2.imshow('the first image from python',frame)
    kry=cv2.waitKey(1)

    #stop if the key is pressed
    if key==81 or key==113:
        break
        
#realese videocapture
webcam.realese()
 

print("code worked!!")