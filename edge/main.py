import cv2
from backports import lzma
from ultralytics import YOLO, solutions
from ultralytics.utils.plotting import Annotator
import time
import logging




pre_model_body = YOLO("yolov8n.pt")
pre_model_body.export(format="openvino")
model = YOLO("yolov8n_openvino_model/", task='detect')

pre_model_face = YOLO("yolov8n-face.pt")
pre_model_face.export(format="openvino")
model_face = YOLO("yolov8n-face_openvino_model/", task='detect')


cap = cv2.VideoCapture("ross.mp4")
assert cap.isOpened(), "Error reading video file"

w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))


logging.basicConfig(
    filename='detection_logs.log',  # Log file name
    level=logging.INFO,  # Log level
    format='%(asctime)s - %(message)s',  # Log format with timestamp
    datefmt='%Y-%m-%d %H:%M:%S',  # Date format
)

# Video writer
video_writer = cv2.VideoWriter("peopletracks.avi", cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))


frame_number = 0  # Initialize frame number counter


while cap.isOpened():
    success, im0 = cap.read()
    if success:

        frame_number += 1
        cv2.putText(im0, str(frame_number), (35,35),  cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 17), 1, lineType=cv2.LINE_AA)
        
        results = model.track(im0, persist=True)
        results_face = model_face(im0)

        
        for r in results:

            annotator = Annotator(im0, font_size=0.000000003)

            boxes = r.boxes

            for box in boxes:
                b = box.xyxy[0].tolist()
                c = box.cls
                id = int(box.id[0])
                c_c = int(c[0])
                
                #print(box)
                xmin, ymin, xmax, ymax = round(b[0],1), round(b[1],1), round(b[2],1), round(b[3],1)
                x = xmax-xmin
                y = ymax-ymin
                cord_a = (int(xmin), int(ymin))
                cord_b = (int(xmax), int(ymax))

                vals = f"ID: {id}"

                # Log the detection with frame number and bounding box
                logging.info(f"Frame: {frame_number}, ID: {id}, Bounding Box: [{xmin}, {ymin}, {xmax}, {ymax}], Class: {c}")


                vals = str(id)
                # Add custom smaller text using cv2.putText directly
                font_scale = 0.4  # Reduce this for smaller text
                font_thickness = 1
                font = cv2.FONT_HERSHEY_SIMPLEX
                color = (0, 255, 17)  # Blue color for text
                position = (int(b[0]), int(b[1] - 5))  # Position text above the box
                cv2.putText(im0, vals, position, font, font_scale, color, font_thickness, lineType=cv2.LINE_AA)
                cv2.rectangle(im0, cord_a, cord_b, color, font_thickness)

                #annotator.box_label(b, vals, font_scale=0.4, font_thickness=1)
                #annotator.box_label(b, vals)
        
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
    #tracks = model.track(im0, persist=True, show=False)

    #im0 = heatmap_obj.generate_heatmap(im0, tracks)
    #video_writer.write(im0)

cap.release()
video_writer.release()
