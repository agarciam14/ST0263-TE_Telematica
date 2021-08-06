import socket
import threading
import sys
import pickle

from msgs import send_msg, msg_service

host = "34.229.56.54"
port = 6000
name = ""

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((str(host), int(port)))

    msg_service = threading.Thread(target=msg_service, args=(s,))
    msg_service.daemon = True
    msg_service.start()
    name = input('Enter your name: ')
    while True:
        msg = input('You: ')
        if msg != 'salir':
            msg= {
                'name': name,
                'msg': msg
            }
            send_msg(s, msg)
        else:
            s.close()
            sys.exit()