# Importamos las librerias necesarias
import http.client
import json
import clientServer
import threading
import sys

connected = False
conn = ''
headers = {
    'Content-type': 'application/json;charset=utf-8'
}
port = 8081

def set_connection(name):
    global conn
    conn = http.client.HTTPConnection("44.196.29.126:8000")
    message = json.dumps({
        "name": name,
        "port": port
    })
    conn.request("POST", "/", message.encode(), headers)
    response = conn.getresponse()
    print("-----%s online-----" % response.read(1000).decode())
    if response.status == 200:
        global connected
        connected = True

def send_msg(message):
    conn.request("POST", "/send", message.encode(), headers)
    response = conn.getresponse()

def disconnect(name):
    message = json.dumps({
        "name": name
    })
    conn.request("POST", "/exit", message.encode(), headers)
    response = conn.getresponse()

    print("-----%s-----" % response.read(1000).decode())

if __name__ == "__main__":
    client_server = threading.Thread(target=clientServer.main, args=(port,))
    client_server.daemon = True
    client_server.start()

    name = input('Enter your name: ')
    set_connection(name)

    while connected:
        msg = input('You: ')
        if msg != 'salir':
            msg= {
                'name': name,
                'msg': msg
            }
            send_msg(json.dumps(msg))
        else:
            connected = False
    disconnect(name)
    sys.exit()
