import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.template.loader import render_to_string
from django.conf import settings

def enviar_correo(destinatario, asunto, plantilla, contexto):
    email_emisor = settings.DEFAULT_FROM_EMAIL
    
    # Renderizar el contenido HTML de la plantilla
    html_content = render_to_string(plantilla, contexto)
    
    # Configuración del correo electrónico
    msg = MIMEMultipart()
    msg['From'] = email_emisor
    msg['To'] = destinatario
    msg['Subject'] = asunto

    # Adjuntar el contenido HTML
    msg.attach(MIMEText(html_content, 'html'))
    
    # Configurar la conexión segura con el servidor de correo saliente (SMTP server)
    server = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
    server.starttls()
    server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)

    # Enviar el correo electrónico
    server.sendmail(email_emisor, destinatario, msg.as_string())
    server.quit()  # Terminar la conexión
    
    # Alerta de correo enviado
    print("Mensaje enviado correctamente.")
