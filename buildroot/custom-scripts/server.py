from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import TCPServer
import os.path
import sys
class MyRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.path = '/index.html'
        return BaseHTTPRequestHandler.do_GET(self)

Handler = MyRequestHandler
server = TCPServer(('0.0.0.0', 8080), Handler)
server.serve_forever()
