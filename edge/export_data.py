import requests

payload = {}
headers = {"Accept":"*/*", "Connection":"keep-alive"}


url = "http://10.22.238.73:8000/v1/datastore/upload"
files=[
  ('file',('detection_logs.log', open('./detection_logs.log','rb'),'text/plain'))
]
response = requests.request("POST", url, headers=headers, data=payload, files=files)