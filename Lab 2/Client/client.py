# Importamos las librerias necesarias
import http.client
import json
import clientServer
import threading
import sys
import argparse

DEFAULT_IP_ADDRESS = '44.196.29.126'
DEFAULT_PORT = '8000'

parser = argparse.ArgumentParser(description=('Launch client'))

# Optional field.
parser.add_argument(
    '-i', '--ip_address', default=DEFAULT_IP_ADDRESS, required=False,
    help=("The Server elastic IP address, It's set by default as 44.196.29.126"))

parser.add_argument(
    '-p', '--port', default=DEFAULT_PORT, required=False, type=int,
    help=("The Client server port, It's set by default as 8000"))

args = parser.parse_args()

connected = False
conn = ''
headers = {
    'Content-type': 'application/json;charset=utf-8'
}

def set_connection(name):
    global conn
    conn = http.client.HTTPConnection(f"{args.ip_address}:8000")
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
    client_server = threading.Thread(target=clientServer.main, args=(args.port,))
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
