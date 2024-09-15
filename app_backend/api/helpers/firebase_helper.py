import os
import asyncio
import mimetypes
import logging
import firebase_admin
from io import BytesIO
from firebase_admin import credentials, storage

logger = logging.getLogger(__name__)

class FireStore():
    def __init__(self):
        cred = credentials.Certificate("./creds.json")  # Ruta a tu archivo JSON de credenciales
        firebase_admin.initialize_app(
            cred, {
                'apiKey': "AIzaSyApQfwkPEIfUeNWrYPeVwTg7wZ9gzwslk8",
                'authDomain': "hackmty24-a5a62.firebaseapp.com",
                'projectId': "hackmty24-a5a62",
                'storageBucket': "hackmty24-a5a62.appspot.com",
                'messagingSenderId': "988136450566",
                'appId': "1:988136450566:web:46b6653e3467ce034e3187",
                'measurementId': "G-4WVVD8JFZE"
            }
        )
    
    async def upload_file(self, file_object, unique_id: str):
        mimetypes.init()
        file_name = file_object.filename
        file_type = mimetypes.guess_type(file_name)[0].split('/')[0]

        bucket = storage.bucket()
        blob = bucket.blob(f'{unique_id}/{file_type}/{file_name}')  # Guarda el archivo en la carpeta con el ID único}')
        blob.upload_from_string(file_object.file.read(), content_type=file_object.content_type)

        logger.info(f'File {file_name} uploaded to Firebase storage.')
    
    async def get_file(self, file_name: str, file_type: str, unique_id: str):
        file_buffer = BytesIO()

        bucket = storage.bucket()
        blob = bucket.blob(f'{unique_id}/{file_type}/{file_name}')
        blob.download_to_file(file_buffer)
        
        return file_buffer

    async def list_files(self, unique_id: str):
        bucket = storage.bucket()
        blobs = bucket.list_blobs(prefix=f'{unique_id}/')

        return [blob.name.split('/')[-1] for blob in blobs]


firebase = FireStore()