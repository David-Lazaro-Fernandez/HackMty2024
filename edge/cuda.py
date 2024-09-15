import cv2
import logging
import time
from openvino.runtime import Core  # Import OpenVINO Runtime for device selection

# Setup logging
logging.basicConfig(
    filename='detection_logs.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)

# Initialize the OpenVINO Core to load models on specific devices
core = Core()

# Load the models and specify the device to use (GPU for Intel Arc)
model_path_body = "yolov8n_openvino_model/model.xml"
model_path_face = "yolov8n-face_openvino_model/model.xml"

# Load the models on the GPU (Intel Arc)
model_body = core.compile_model(model_path_body, "GPU")  # Specify 'GPU' device
model_face = core.compile_model(model_path_face, "GPU")  # Specify 'GPU' device

# Open the video file
cap = cv2.VideoCapture("ross.mp4")
assert cap.isOpened(), "Error reading video file"

w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))

# Video writer
video_writer = cv2.VideoWriter("cudaout.avi", cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))

frame_number = 0  # Initialize frame number counter

while cap.isOpened():
    success, im0 = cap.read()
    if success:
        frame_number += 1
        cv2.putText(im0, str(frame_number), (35, 35), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 17), 1, lineType=cv2.LINE_AA)
        
        # Perform inference using the GPU-loaded models
        results_body = model_body([im0])
        results_face = model_face([im0])

        # Process body detections
        for r in results_body:
            annotator = Annotator(im0, font_size=0.000000003)
            boxes = r.boxes

            for box in boxes:
                b = box.xyxy[0].tolist()
                c = box.cls
                id = int(box.id[0])
                xmin, ymin, xmax, ymax = round(b[0], 1), round(b[1], 1), round(b[2], 1), round(b[3], 1)
                cord_a = (int(xmin), int(ymin))
                cord_b = (int(xmax), int(ymax))
                vals = f"ID: {id}"

                logging.info(f"Frame: {frame_number}, ID: {id}, Bounding Box: [{xmin}, {ymin}, {xmax}, {ymax}], Class: {c}")
                cv2.putText(im0, vals, (int(b[0]), int(b[1]) - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 17), 1, cv2.LINE_AA)
                cv2.rectangle(im0, cord_a, cord_b, (0, 255, 17), 1)

        # Process face detections
        for face in results_face:
            boxes = face.boxes
            for box in boxes:
                b = box.xyxy[0].tolist()
                xmin, ymin, xmax, ymax = int(b[0]), int(b[1]), int(b[2]), int(b[3])
                cord_a = (int(xmin), int(ymin))
                cord_b = (int(xmax), int(ymax))
                cv2.rectangle(im0, cord_a, cord_b, (0, 255, 17), 1)

        im0 = annotator.result()
        video_writer.write(im0)
    else:
        break

cap.release()
video_writer.release()

