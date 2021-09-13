import pika
import json

connection = pika.BlockingConnection(pika.ConnectionParameters('54.86.128.59', 5672, '/', 
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