import os
from organizador import organizar_archivos
from renombrador import renombrar_archivos
from enviador_correo import enviar_reporte_correo

def main():
    # Configuración inicial
    directorio = r"C:\Users\carlo\OneDrive\Escritorio\archivos de prueba python"  # Cambia esta ruta
    carpetas = {
        "Imagenes": [".jpg", ".jpeg", ".png", ".gif"],  # Añadimos .jpeg
        "Documentos": [".pdf", ".docx", ".txt"],
        "Videos": [".mp4", ".mov"]
    }
    todas_extensiones = [ext for exts in carpetas.values() for ext in exts]
    reporte = []

    print(f"Directorio configurado: {directorio}")
    print(f"Extensiones disponibles: {', '.join(todas_extensiones)}")
    if not os.path.exists(directorio):
        print(f"Error: El directorio {directorio} no existe. Crea la carpeta y añade archivos.")
        return

    # Pregunta si quiere organizar
    organizar = input("¿Organizar archivos por extensión? (s/n): ").lower() == "s"
    if organizar:
        print(f"Organizando archivos en {directorio}")
        reporte.extend(organizar_archivos(directorio, carpetas))

    # Pregunta si quiere renombrar
    renombrar = input("¿Renombrar archivos? (s/n): ").lower() == "s"
    if renombrar:
        extensiones_input = input("Ingresa las extensiones a renombrar (ej. .jpg,.png) o presiona Enter para todas: ")
        if extensiones_input:
            extensiones = [ext.lower().strip() for ext in extensiones_input.split(",")]
            for ext in extensiones:
                if ext not in todas_extensiones:
                    print(f"Advertencia: La extensión {ext} no está en las categorías definidas.")
        else:
            extensiones = todas_extensiones
            print("Renombrando todos los archivos en las carpetas.")
        usar_fecha = input("¿Usar prefijo con fecha automática? (s/n): ").lower() == "s"
        prefijo = None if usar_fecha else input("Ingresa el prefijo para los archivos (ej. '2025_'): ")
        reporte.extend(renombrar_archivos(directorio, extensiones, prefijo))

    # Pregunta si quiere enviar correo
    enviar_correo = input("¿Enviar reporte por correo? (s/n): ").lower() == "s"
    if enviar_correo:
        remitente = input("Ingresa tu correo (Gmail): ")
        contraseña = input("Ingresa tu contraseña de aplicación: ")
        destinatario = input("Ingresa el correo del destinatario: ")
        resultado_correo = enviar_reporte_correo(remitente, contraseña, destinatario, reporte)
        reporte.append(resultado_correo)

    # Muestra el reporte
    print("\nReporte final:")
    for linea in reporte:
        print(linea)

if __name__ == "__main__":
    main()