import pika
connection = pika.BlockingConnection(pika.ConnectionParameters('54.86.128.59', 5672, '/', 
pika.PlainCredentials("user", "password")))

channel = connection.channel()

def callback(ch, method, properties, body):
    print(f'{body}is received')

channel.basic_consume(queue="my_app", on_message_callback=callback, auto_ack=True)
channel.start_consuming()