from email import message
import pika
import smtplib, ssl
import json
import argparse

DEFAULT_IP_ADDRESS = '54.86.128.59'

parser = argparse.ArgumentParser(description=('Launch client'))

# Optional field.
parser.add_argument(
    '-i', '--ip_address', default=DEFAULT_IP_ADDRESS, required=False,
    help=("The RabbitMQ server elastic IP address, It's set by default as 54.86.128.59"))

args = parser.parse_args()

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "agarciamessage@gmail.com"
password = "Agarciam14"

context = ssl.create_default_context()

connection = pika.BlockingConnection(pika.ConnectionParameters(args.ip_address, 5672, '/',
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
