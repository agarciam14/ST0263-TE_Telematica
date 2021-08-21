import socket
import threading
import sys

from msgs import msg_to_all

host = "localhost"
port = 6000

clients = []

def acceptConnection(s):
    while True:
        try:
            conn, addr = s.accept()
            conn.setblocking(False)
            clients.append(conn)
        except:
            pass

def send_messages():
    while True:
        if len(clients) > 0:
            for c in clients:
                try:
                    data = c.recv(1024)
                    if data:
                        msg_to_all(clients,data,c)
                except:
                    pass

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((str(host), int(port)))
    s.listen(10)
    s.setblocking(False)

    accept = threading.Thread(target=acceptConnection, args=(s,))
    messages = threading.Thread(target=send_messages)
    
    accept.daemon = True
    accept.start()

    messages.daemon = True
    messages.start()

    while True:
        msg = input('->')
        if msg == 'salir':
            sock.close()
            sys.exit()

