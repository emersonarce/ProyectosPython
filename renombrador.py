import os
import shutil
import datetime

def renombrar_archivos(directorio, extensiones=None, prefijo=None):
    """
    Renombra archivos en carpetas del directorio con un prefijo y número secuencial.
    :param directorio: Ruta de la carpeta principal.
    :param extensiones: Lista de extensiones a renombrar (o None para todas).
    :param prefijo: Prefijo personalizado o None para usar la fecha.
    :return: Lista con el reporte de archivos renombrados.
    """
    reporte = []
    if not prefijo:
        prefijo = datetime.datetime.now().strftime("%Y%m%d_")  # Ejemplo: 20250528_
    print(f"\n=== Iniciando renombramiento en: {directorio} ===")
    print(f"Usando prefijo: {prefijo}")
    
    for carpeta in os.listdir(directorio):
        carpeta_path = os.path.join(directorio, carpeta)
        if os.path.isdir(carpeta_path):
            print(f"Procesando carpeta: {carpeta_path}")
            archivos = [f for f in os.listdir(carpeta_path) if os.path.isfile(os.path.join(carpeta_path, f))]
            if extensiones:
                archivos = [f for f in archivos if os.path.splitext(f)[1].lower() in extensiones]
                print(f"Filtrando por extensiones: {extensiones}")
            else:
                print("Sin filtro de extensiones, procesando todos los archivos")
            for i, archivo in enumerate(archivos, 1):
                extension = os.path.splitext(archivo)[1].lower()
                nuevo_nombre = f"{prefijo}{i:03d}{extension}"
                try:
                    shutil.move(
                        os.path.join(carpeta_path, archivo),
                        os.path.join(carpeta_path, nuevo_nombre)
                    )
                    reporte.append(f"Renombrado: {carpeta}/{archivo} -> {nuevo_nombre}")
                    print(f"  Renombrado: {carpeta}/{archivo} -> {nuevo_nombre}")
                except Exception as e:
                    print(f"  Error al renombrar {archivo}: {e}")
                    reporte.append(f"Error al renombrar {carpeta}/{archivo}: {e}")
        else:
            print(f"Ignorado: {carpeta} (no es carpeta)")
    print("=== Renombramiento finalizado ===")
    return reporte