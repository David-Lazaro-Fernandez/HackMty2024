import cv2
from backports import lzma
from ultralytics import YOLO, solutions


import requests


url = "http://10.22.238.73:8000/v1/video/download?file_name=rossi CEO.mp4"

payload = {}
headers = {"Accept":"*/*", "Connection":"keep-alive"}

response = requests.request("GET", url, headers=headers, data=payload)

with open('input.mp4', 'wb') as f:
    f.write(response.content)



pre_model = YOLO("yolov8n.pt")
pre_model.export(format="openvino")
model = YOLO("yolov8n_openvino_model/", task='detect')




cap = cv2.VideoCapture("input.mp4")
assert cap.isOpened(), "Error reading video file"
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))

# Video writer
video_writer = cv2.VideoWriter("heatmap_new.mp4", cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))

# Init heatmap
heatmap_obj = solutions.Heatmap(
    colormap=cv2.COLORMAP_PARULA,
    view_img=True,
    shape="circle",
    names=model.names,
)

while cap.isOpened():
    success, im0 = cap.read()
    if not success:
        print("Video frame is empty or video processing has been successfully completed.")
        break
    tracks = model.track(im0, persist=True, show=False)

    im0 = heatmap_obj.generate_heatmap(im0, tracks)
    video_writer.write(im0)

cap.release()
video_writer.release()

