from ultralytics import YOLO
import cv2
import cvzone
import math
import numpy as np
import os

cap = cv2.VideoCapture(0)
# cap = "trail.mp4"
cap.set(3, 1920)
cap.set(4, 1080)


model = YOLO('yolov5su.pt') 

classNames = ["person", "bicycle", "call", "motorbike", "aeroplane", "bus", "train", "truck", "boat","traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat","dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "Umbrella","handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat","baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup","fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli","carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "potted plant", "bed","diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone","microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors","teddy bear", "hair drier", "toothbrush"]

person_detected = False

def get_unique_filename(filename):
    counter = 1
    while os.path.exists(filename):
        filename = f"Dict_Img/person_detected_{counter}.jpg"
        counter += 1
    return filename

while True:
    success, img = cap.read()
    results = model(img,stream=True)
    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            # cv2.rectangle(img, (x1,y1), (x2,y2), (255, 0, 255),3)
            w, h = x2-x1,y2-y1
            cvzone.cornerRect(img, (x1,y1,w,h))
            conf = float(math.ceil((box.conf [0] *100))/100)
            # print(conf)

            cls = int(box.cls[0])

            cvzone.cornerRect(img, (x1,y1 ,w, h))
            currentClass = classNames[cls]
            cvzone.putTextRect(img,f' {currentClass} {conf}', (max(0, x1),max(35 ,y1)))
            # cvzone.putTextRect(img,f' {classNames[cls]} {conf}', (max(0, x1),max(35 ,y1)))
            if currentClass == "person" and not person_detected :
                filename = get_unique_filename("Dict_Img/person_detected_0.jpg")
                # filename = get_unique_filename("Dict_Img/", "person_detected_0")
                # cv2.imwrite(filename, img)
                person_detected = True
            elif  not classNames[cls] == "person":
                person_detected = False


    cv2.imshow("Image", img)
    cv2.waitKey(1)