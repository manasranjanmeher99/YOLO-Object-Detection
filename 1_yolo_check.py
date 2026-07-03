import ultralytics
import torch

ultralytics.checks()  # check environment and dependencies

from ultralytics import YOLO
model= YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)
