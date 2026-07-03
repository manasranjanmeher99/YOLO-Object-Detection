# YOLO11 Object Detection using OpenCV

A real-time object detection project built with **Ultralytics YOLO11**, **OpenCV**, and **Python**. This project demonstrates how to detect objects in images and videos using pretrained YOLO11 models and display bounding boxes, class labels, and confidence scores.

---

## 📌 Features

- Detect objects in images using YOLO11
- Detect objects in videos using OpenCV
- Display bounding boxes with class labels
- Show confidence scores for detected objects
- Supports all 80 COCO object classes
- Uses pretrained YOLO11 Nano model
- Easy to customize for your own videos or images

---

## 📂 Project Structure

```text
YOLO11-Object-Detection/
│
├── model/
│   ├── yolo11n.pt                 # YOLO11 Nano pretrained model
│   └── yolov8n.pt                 # YOLOv8 Nano pretrained model (optional)
│
├── video/
│   ├── video_sample1.mp4          # Sample input video
│   └── video_sample2.mp4          # Sample input video
│
├── runs/
│   └── detect/
│       └── predict/               # YOLO generated output (created automatically)
│
├── screenshot/                  
│   └── object_dectect.png         # Object detection screenshot
│
├── 1_yolo_check.py                # Verify Ultralytics installation and model loading
├── 2_yolo_check_image.py          # Object detection on an image
├── 3_yolo_opencv.py               # Real-time video object detection using OpenCV
│
├── coco.txt                       # COCO dataset class labels (80 classes)
│
├── README.md                      # Project documentation
├── requirements.txt               # Python dependencies
└── .gitignore                     # Git ignore rules
```

---

## 🛠️ Technologies Used

- Python 3.x
- OpenCV
- Ultralytics YOLO11
- NumPy
- PyTorch

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/manasranjanmeher99/YOLO11-Object-Detection.git
cd YOLO11-Object-Detection
```

### 2. Create a Virtual Environment

**Windows**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**Linux/macOS**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 📦 Required Packages

```
ultralytics
opencv-python
numpy
torch
torchvision
```

---

## 📥 Download the YOLO11 Model

Download the pretrained **YOLO11 Nano (`yolo11n.pt`)** model from the Ultralytics website and place it inside the `model/` directory.

```text
model/
└── yolo11n.pt
```

---

## 🚀 Usage

### 1. Verify YOLO Installation

```bash
python 1_yolo_check.py
```

This script checks whether the Ultralytics package is installed correctly and verifies that the model can be loaded.

---

### 2. Detect Objects in an Image

```bash
python 2_yolo_check_image.py
```

This script performs object detection on an image using the pretrained YOLO11 model.

---

### 3. Detect Objects in a Video

```bash
python 3_yolo_opencv.py
```

This script performs real-time object detection on a video using OpenCV and YOLO11.

Press **Q** to exit the video window.

---

## 🎯 Detection Output

The model detects objects and displays:

- Bounding boxes
- Object class names
- Confidence scores

Example:

```
Person 98.6%
Car 95.2%
Dog 91.8%
```

---

## 📁 Output Directory

When `save=True` is enabled, Ultralytics automatically stores the prediction results in:

```text
runs/
└── detect/
    └── predict/
```

---

## 📋 COCO Dataset Classes

The project uses the **COCO dataset**, which contains 80 common object categories, including:

- Person
- Bicycle
- Car
- Motorcycle
- Airplane
- Bus
- Train
- Truck
- Boat
- Dog
- Cat
- Horse
- Chair
- Laptop
- Cell Phone

and many more.

---

## 📸 Project Preview

### Input

- Image or video from the `video/` folder.

### Output

- Detected objects with bounding boxes, labels, and confidence scores.

![YOLO11 Object Detection](screenshot/object_detection.png)

---

## 🔮 Future Improvements

- Webcam object detection
- Real-time object tracking
- Custom dataset training
- Instance segmentation
- Pose estimation
- Face detection integration
- Vehicle counting
- Speed estimation

---

## 👨‍💻 Author

**Manas Ranjan Meher**

Feel free to connect and contribute to the project.

---


## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub.

---
