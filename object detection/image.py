import cv2
from ultralytics import YOLO
import os

os.system('python -W ignore yolov8n.pt > /dev/null 2>&1')

model = YOLO('yolov8n.pt')  # Use a lighter YOLOv5 variant

path = "./trail/image7.jpg"
webcam = False

image = cv2.imread(path)

width, height = 1080, 720  # Set the desired width and height
image_resized = cv2.resize(image, (width, height))


# cv2.imshow("img", image)
results = model(image_resized, show = True)
cv2.waitKey(0)
     
# Release the video capture and close OpenCV windows
# cap.release()
cv2.destroyAllWindows()
