import cv2
from ultralytics import YOLO
import time

from backports import lzma

from ultralytics.utils.plotting import Annotator

import logging

import requests


url = "http://10.22.238.73:8000/v1/video/download?file_name=rossi CEO.mp4"

payload = {}
headers = {"Accept":"*/*"}

response = requests.request("GET", url, headers=headers, data=payload)

with open('input.mp4', 'wb') as f:
    f.write(response.content)




# Initialize models
pre_model_body = YOLO("yolov8n.pt")
pre_model_body.export(format="openvino")
model = YOLO("yolov8n_openvino_model/", task='detect')

pre_model_face = YOLO("yolov8n-face.pt")
pre_model_face.export(format="openvino")
model_face = YOLO("yolov8n-face_openvino_model/", task='detect')

cap = cv2.VideoCapture("input.mp4")
assert cap.isOpened(), "Error reading video file"

w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))

# Set up logging
logging.basicConfig(
    filename='detection_logs.log',  # Log file name
    level=logging.INFO,  # Log level
    format='%(asctime)s - %(message)s',  # Log format with timestamp
    datefmt='%Y-%m-%d %H:%M:%S',  # Date format
)

# Video writer
video_writer = cv2.VideoWriter("results.mp4", cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))

frame_number = 0  # Initialize frame number counter
detection_times = {}  # Dictionary to track detection start times

while cap.isOpened():
    success, im0 = cap.read()
    if success:
        frame_number += 1
        cv2.putText(im0, str(frame_number), (35,35), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 17), 1, lineType=cv2.LINE_AA)
        
        results = model.track(im0, persist=True)
        results_face = model_face(im0)

        current_time = time.time()  # Get current time
        
        for r in results:
            annotator = Annotator(im0, font_size=0.000000003)
            boxes = r.boxes

            for box in boxes:
                b = box.xyxy[0].tolist()
                c = box.cls
                id = int(box.id[0])  # Detected ID
                c_c = int(c[0])

                # Calculate bounding box dimensions
                xmin, ymin, xmax, ymax = round(b[0], 1), round(b[1], 1), round(b[2], 1), round(b[3], 1)
                cord_a = (int(xmin), int(ymin))
                cord_b = (int(xmax), int(ymax))

                # If ID is detected for the first time, store its start time
                if id not in detection_times:
                    detection_times[id] = current_time
                    detection_duration = 0.0
                else:
                    # Calculate how long the ID has been detected
                    detection_duration = current_time - detection_times[id]
                    logging.info(f"ID: {id}, Detected for {detection_duration:.2f} seconds")

                # Add the ID and detection time to the video output
                vals = f"ID: {id}, Time: {detection_duration:.2f}s"
                font_scale = 0.4
                font_thickness = 1
                font = cv2.FONT_HERSHEY_SIMPLEX
                color = (0, 255, 17)
                position = (int(b[0]), int(b[1] - 5))  # Position text above the box
                cv2.putText(im0, vals, position, font, font_scale, color, font_thickness, lineType=cv2.LINE_AA)
                cv2.rectangle(im0, cord_a, cord_b, color, font_thickness)

        im0 = annotator.result()
        video_writer.write(im0)
    else:
        break

cap.release()
video_writer.release()

url = "http://10.22.238.73:8000/v1/datastore/upload"
files=[
  ('file',('results.mp4',open('results.mp4','rb'),'application/octet-stream'))
]

response = requests.request("POST", url, headers=headers, data=payload, files=files)