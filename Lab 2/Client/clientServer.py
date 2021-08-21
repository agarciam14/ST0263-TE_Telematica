#Lo primero que hacemos es importar las librerias necesarias
from http.server import HTTPServer, BaseHTTPRequestHandler
import http.client
import json
from datetime import datetime

clients = []
headers = {
    'Content-type': 'application/json;charset=utf-8'
}

class HttpHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        if self.path == '/receive':
            self.receive()
        if self.path == '/connect':
            self.connect()
        if self.path == '/disconnect':
            self.disconnect()

    def connect(self):
        content_length = int(self.headers['Content-Length'])
        post_data = json.loads(self.rfile.read(content_length).decode())
        print("\r-----%s is now online-----\nYou: " % (post_data['name']), end='')
        self.send_response(200)
        self.send_header('Content-type', 'application/json;charset=utf-8')
        self.end_headers()
        self.wfile.write("message received".encode())

    def disconnect(self):
        content_length = int(self.headers['Content-Length'])
        post_data = json.loads(self.rfile.read(content_length).decode())
        print("\r-----%s has disconected-----\nYou: " % (post_data['name']), end='')
        self.send_response(200)
        self.send_header('Content-type', 'application/json;charset=utf-8')
        self.end_headers()
        self.wfile.write("message received".encode())


    def receive(self):
        content_length = int(self.headers['Content-Length'])
        post_data = json.loads(self.rfile.read(content_length).decode())
        print("\r%s: %s\nYou: " % (post_data['name'], post_data['msg']), end='')
        self.send_response(200)
        self.send_header('Content-type', 'application/json;charset=utf-8')
        self.end_headers()
        self.wfile.write("message received".encode())

    def log_message(self, format, *args):
        pass
    
def main(port):
    server_address = ('', port)
    httpd = HTTPServer(server_address, HttpHandler)
    httpd.serve_forever()
