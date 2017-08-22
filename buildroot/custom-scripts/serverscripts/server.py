from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import TCPServer
import time
import psutil
import platform
import os.path
import sys


class MyRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        
        current_time = time.localtime()
        elapsed_time = time.localtime(time.time() - server_start)
        cpu_usage = psutils.cpu_percent()
        memory_usage = psutil.virtual_memory()
        
        process_list = []

        for process in psutil.process_iter():
            try:
                process_info = process.as_dict(attrs=['pid', 'name'])
                process_list.append(process_info)
            except psutil.NoSuchProcess:
                pass
        



        self.path = '/index.html'
        return BaseHTTPRequestHandler.do_GET(self)



server_start = time.time()
processor = platform.processor()
linux = platform.linux_distribution()

Handler = MyRequestHandler
server = TCPServer(('0.0.0.0', 8080), Handler)
server.serve_forever()
