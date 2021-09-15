#Lo primero que hacemos es importar las librerias necesarias
from http.server import HTTPServer, BaseHTTPRequestHandler
import http.client
import json
from datetime import datetime

"""
 Creamos una clase a la cual yo llamare "HttpHandler" que heredara 
 los metodos de la clase BaseHTTPRequestHandler.
"""
clients  = []
headers = {
    'Content-type': 'application/json;charset=utf-8'
}


class HttpHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # <--- Gets the data itself
        if self.path == '/':
            self.connect()
        if self.path == '/send':
            self.send_msg()
        if self.path == '/exit':
            self.disconnect()

    def connect(self):
        content_length = int(self.headers['Content-Length'])
        post_data = json.loads(self.rfile.read(content_length).decode())
        for client in clients:
            conn = http.client.HTTPConnection("%s:%d" % (client['ip'],client['port']))
            conn.request("POST", "/connect", json.dumps(post_data).encode(), headers)
            response = conn.getresponse()
        clients.append({
            "name": post_data['name'],
            "ip": self.client_address[0],
            "port": post_data['port']
        })
        self.send_response(200)
        self.send_header('Content-type', 'application/json;charset=utf-8')
        self.end_headers()
        message = str(len(clients)-1).encode()
        self.wfile.write(message)

    def disconnect(self):
        content_length = int(self.headers['Content-Length'])
        post_data = json.loads(self.rfile.read(content_length).decode())
        i = -1
        for index, client in enumerate(clients):
            if client['name'] != post_data['name']:
                conn = http.client.HTTPConnection("%s:%d" % (client['ip'],client['port']))
                conn.request("POST", "/disconnect", json.dumps(post_data).encode(), headers)
                response = conn.getresponse()
            else:
                i = index
        clients.pop(i)
        self.send_response(200)
        self.send_header('Content-type', 'application/json;charset=utf-8')
        self.end_headers()
        message = "You've disconnected".encode()
        self.wfile.write(message)



    def send_msg(self):
        content_length = int(self.headers['Content-Length'])
        post_data = json.loads(self.rfile.read(content_length).decode())
        for client in clients:
            if client['name'] != post_data['name']:
                try:
                    conn = http.client.HTTPConnection("%s:%d" % (client['ip'],client['port']))
                    conn.request("POST", "/receive", json.dumps(post_data).encode(), headers)
                    response = conn.getresponse()
                except:
                    print("Message couldn't be sent to all users")
        self.send_response(200)
        self.send_header('Content-type', 'application/json;charset=utf-8')
        self.end_headers()
        self.wfile.write(response.read(1000))

if __name__ == "__main__":
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, HttpHandler)
    print("Server active...")
    httpd.serve_forever()
