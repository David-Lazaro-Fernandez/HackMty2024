

import requests

payload = {}
headers = {"Accept":"*/*", "Connection":"keep-alive"}


url = "http://10.22.238.73:8000/v1/datastore/upload"
files=[
  ('file',('heatmap_new.mp4', open('./heatmap_new.mp4','rb'),'video/mp4'))
]

response = requests.request("POST", url, headers=headers, data=payload, files=files)
