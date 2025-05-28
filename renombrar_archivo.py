import os
import shutil

directorio = r"C:\Users\carlo\OneDrive\Escritorio\archivos de prueba python"
prefijo = input("Igrese el prefijo para los archivos (ej. '2025_'):")

#obtiene la lista de archivos
archivos = [f for f in os.listdir(directorio) if os.path.isfile(os.path.join(directorio, f))]

#renombra los archivos 
for i, archivo in enumerate(archivos, 1):
    #obtiene la extension y el nombre base 
    nombre_base, extension = os.path.splitext(archivo)
    #crea el nuevo nombre con prefijo y número (por ejemplo, 2025_001_foto.jpg)
    nuevo_nombre = f"{prefijo}{i:03d}{extension}"
    #rutas completas 
    ruta_antigua = os.path.join(directorio, archivo)
    ruta_nueva = os.path.join(directorio, nuevo_nombre)
    #renombra el archivo 
    shutil.move(ruta_antigua, ruta_nueva)
    print(f"Renombrado: {archivo} ->{nuevo_nombre}")
    print("¡Renombramiento completo!")