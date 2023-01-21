import requests 


URL = "https://learnpythonthehardway.org/python3/languages.txt"
response = requests.get(URL) # decarga la informacion desde la URL
print(response)
open("languages.txt", "wb").write(response.content)

# pregunta: ¿donde lo va a guardar?
    # respuesta: lo guarda en el mismo directorio que mi script de python

# felicidades: logré descargar un archivo txt desde una URL usando python.

def downloader(online_path, file_name_user):
    URL = online_path 
    response = requests.get(URL)
    open(file_name_user, "wb").write(response.content)
# NOTA: EL NOMBRE DEL ARCHIVO DEBE CONTENER LA EXTENSION PARA PODER SER ABIERTO. !!!

downloader('https://www.elsoldetijuana.com.mx/incoming/7h4hk6-kesikesiperrito.jpg/alternates/LANDSCAPE_768/Kesikesiperrito.jpg'
, 'perrito_meme')


# entonces el codigo inicial lo puedo meter en una función para
# 1. ejecutarla en el momento que yo quiera 
# 2. llamarla cuantas veces yo quiera para archivos distintos. 