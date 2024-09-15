import firebase_admin
from firebase_admin import credentials, storage
import os

# Inicializa la app de Firebase
def initialize_firebase():
    cred = credentials.Certificate("./creds.json")  # Ruta a tu archivo JSON de credenciales
    firebase_admin.initialize_app(cred, {
        'apiKey': "AIzaSyApQfwkPEIfUeNWrYPeVwTg7wZ9gzwslk8",
        'authDomain': "hackmty24-a5a62.firebaseapp.com",
        'projectId': "hackmty24-a5a62",
        'storageBucket': "hackmty24-a5a62.appspot.com",
        'messagingSenderId': "988136450566",
        'appId': "1:988136450566:web:46b6653e3467ce034e3187",
        'measurementId': "G-4WVVD8JFZE"
    })

# Función para subir un archivo (audio/video) a una carpeta con un ID único
def upload_file_to_firebase(file_path, unique_id, file_type):
    bucket = storage.bucket()
    blob = bucket.blob(f'{unique_id}/{file_type}/{os.path.basename(file_path)}')  # Guarda el archivo en la carpeta con el ID único
    blob.upload_from_filename(file_path)
    print(f'File {file_path} uploaded to Firebase storage.')

# Función para descargar un archivo desde Firebase
def retrieve_file_from_firebase(unique_id, file_name, file_type, download_path):
    bucket = storage.bucket()
    blob = bucket.blob(f'{unique_id}/{file_type}/{file_name}')
    blob.download_to_filename(download_path)
    print(f'File {file_name} downloaded from Firebase to {download_path}.')


def upload_video():   
    # Subir archivo
    file_path = './16.mp4'  # Ruta del archivo que quieres subir
    unique_id = '12345'  # Este sería el ID único
    file_type = 'videos'  # Puede ser 'audio' o 'videos' dependiendo del tipo de archivo
    upload_file_to_firebase(file_path, unique_id, file_type)
    

def get_video():
     # Recuperar archivo
    file_name = 'video.mp4'  # El nombre del archivo en Firebase
    download_path = 'ruta/a/descargar/video.mp4'  # Ruta donde se guardará el archivo descargado
    retrieve_file_from_firebase(unique_id, file_name, file_type, download_path)
    
# Función para subir un audio
def upload_audio():   
    file_path = './audio.mp3'  # Ruta del archivo que quieres subir
    unique_id = '67890'  # Este sería el ID único
    file_type = 'audio'  # Subir a la carpeta de 'audio'
    upload_file_to_firebase(file_path, unique_id, file_type)

# Función para recuperar un audio
def get_audio():
    unique_id = '67890'  # ID único del audio
    file_name = 'audio.mp3'  # El nombre del archivo en Firebase
    file_type = 'audio'
    download_path = './descargado_audio.mp3'  # Ruta donde se guardará el archivo descargado
    retrieve_file_from_firebase(unique_id, file_name, file_type, download_path)

    
# Ejemplo de uso
if __name__ == "__main__":
    initialize_firebase()

    upload_video()
