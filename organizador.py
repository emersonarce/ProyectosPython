import os
import shutil

def organizar_archivos(directorio, carpetas):
    """
    Organiza archivos en carpetas según su extensión.
    :param directorio: Ruta de la carpeta a organizar.
    :param carpetas: Diccionario con nombres de carpetas y listas de extensiones.
    :return: Lista con el reporte de archivos movidos.
    """
    reporte = []
    print(f"\n=== Iniciando organización en: {directorio} ===")
    print(f"Carpetas y extensiones definidas: {carpetas}")

    if not os.path.exists(directorio):
        print(f"Error: El directorio {directorio} no existe.")
        return reporte

    for carpeta, exts in carpetas.items():
        carpeta_path = os.path.join(directorio, carpeta)
        os.makedirs(carpeta_path, exist_ok=True)
        print(f"\nProcesando carpeta: {carpeta} con extensiones: {exts}")
        archivos_procesados = 0
        for archivo in os.listdir(directorio):
            archivo_path = os.path.join(directorio, archivo)
            if os.path.isfile(archivo_path):
                extension = os.path.splitext(archivo)[1].lower()
                print(f"  Archivo: {archivo}, Extensión: {extension}")
                if extension in exts:
                    destino = os.path.join(carpeta_path, archivo)
                    try:
                        shutil.move(archivo_path, destino)
                        reporte.append(f"Movido: {archivo} a {carpeta}")
                        print(f"    Movido: {archivo} a {carpeta}")
                        archivos_procesados += 1
                    except Exception as e:
                        print(f"    Error al mover {archivo}: {e}")
                        reporte.append(f"Error al mover {archivo} a {carpeta}: {e}")
                else:
                    print(f"    Ignorado: {archivo} (extensión no coincide con {exts})")
            else:
                print(f"  Ignorado: {archivo} (no es un archivo)")
        print(f"Total de archivos procesados para {carpeta}: {archivos_procesados}")
    print("=== Organización finalizada ===")
    return reporte