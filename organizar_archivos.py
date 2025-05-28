import os
import shutil 

directorio = r"C:\Users\carlo\OneDrive\Escritorio\archivos de prueba python"

carpetas = {
    "Imagenes": [".jpg", ".png", ".gif"],
    "Documentos":[".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mov"]
}

#crea las carpetas si no existen (imagenes, documentos, videos)
for carpeta in carpetas:
    os.makedirs(os.path.join(directorio, carpeta), exist_ok=True)

for archivo in os.listdir(directorio):
    if os.path.isfile(os.path.join(directorio, archivo)):
        extension = os.path.splitext(archivo)[1].lower()
        for carpeta, extensiones in carpetas.items():
            if extension in extensiones:
                shutil.move(
                    os.path.join(directorio, archivo),
                    os.path.join(directorio, carpeta, archivo)
                )
                print(f"movido: {archivo} a {carpeta}")
print("¡Organización completa!")                