import pika
import json
import argparse

DEFAULT_IP_ADDRESS = '54.86.128.59'

parser = argparse.ArgumentParser(description=('Launch client'))

# Optional field.
parser.add_argument(
    '-i', '--ip_address', default=DEFAULT_IP_ADDRESS, required=False,
    help=("The RabbitMQ server elastic IP address, It's set by default as 54.86.128.59"))

args = parser.parse_args()

connection = pika.BlockingConnection(pika.ConnectionParameters(args.ip_address, 5672, '/', 
pika.PlainCredentials('user', 'password')))
channel = connection.channel()
tasks = ["Take data report", "Generate report", "Graph data", "Clear registry", "Terminate processes"]
print("Enter task to do...")
for i in range(len(tasks)):
    print(i,tasks[i])

task = input("task: ")
username = input("Enter username: ")
email = input("Enter email: ")

msg = json.dumps({
    'task': tasks[int(task)],
    'username': username,
    'email': email
}, default=str)

channel.basic_publish(exchange='my_exchange', routing_key='test', body= msg)
print("Runnning Client Application...")
print(" Task sent...!")

connection.close()
