import requests

def download_public_file_from_google_drive(url, destination):
    file_id = url.split('/')[5]
    
    download_url = f"https://drive.google.com/uc?export=download&id={file_id}"

    response = requests.get(download_url, stream=True)
    
    if response.status_code == 200:
        with open(destination, "wb") as f:
            for chunk in response.iter_content(32768):
                if chunk:
                    f.write(chunk)
        print(f"Archivo descargado y guardado en {destination}")
    else:
        print(f"Error al descargar el archivo. Código de estado: {response.status_code}")

file_url = "https://drive.google.com/file/d/1xN2GmprxZq_HNzFTB3Cz7lta-Q55dR9X/view"
download_public_file_from_google_drive(file_url, "archivo_descargado.m4a")
