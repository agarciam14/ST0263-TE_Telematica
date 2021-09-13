from email import message
import pika
import smtplib, ssl
import json

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "agarciamessage@gmail.com"
password = "Agarciam14"

context = ssl.create_default_context()

connection = pika.BlockingConnection(pika.ConnectionParameters('54.86.128.59', 5672, '/', 
pika.PlainCredentials("user", "password")))

channel = connection.channel()

def callback(ch, method, properties, body):
    msg = json.loads(body.decode())
    task = msg['task']
    username = msg['username']
    email = msg['email']

    # ** The task should be done here

    message = f"The task {task}, requested by the user {username} has been completed"

    # Try to log in to server and send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, email, message)

channel.basic_consume(queue="my_app", on_message_callback=callback, auto_ack=True)
channel.start_consuming()