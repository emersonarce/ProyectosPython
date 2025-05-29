import smtplib
from email.mime.text import MIMEText

def enviar_reporte_correo(remitente, contraseña, destinatario, reporte):
    """
    Envía un correo con el reporte de acciones.
    :param remitente: Correo del remitente (Gmail).
    :param contraseña: Contraseña de aplicación de Gmail.
    :param destinatario: Correo del destinatario.
    :param reporte: Lista con las líneas del reporte.
    :return: Mensaje de éxito o error.
    """
    cuerpo = "\n".join(reporte)
    msg = MIMEText(cuerpo)
    msg['Subject'] = "Reporte de Organización y Renombramiento"
    msg['From'] = remitente
    msg['To'] = destinatario

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(remitente, contraseña)
            server.sendmail(remitente, destinatario, msg.as_string())
        return "Correo enviado con el reporte."
    except Exception as e:
        return f"Error al enviar el correo: {e}"