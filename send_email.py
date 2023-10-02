import smtplib as smtp
import ssl
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "marioua289@gmail.com"
    password = os.getenv("PASSWORD")

    receiver = "marioua289@gmail.com"
    context = ssl.create_default_context()

    with smtp.SMTP_SSL(host=host, port=port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
