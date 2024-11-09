import cv2
import torch

model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    results = model(frame)

    results.render() 

    cv2.imshow('Webcam Live Feed with YOLOv5', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
