from ultralytics import YOLO
import numpy

model= YOLO("yolov8n.pt", "v8")  # load a pretrained model (recommended for training)

detection_output = model.predict(source=r"C:\Users\ASUS\Downloads\images (2).jpeg", show=True, conf=0.5, save=True)  # predict on an image

print(detection_output)  # print results

