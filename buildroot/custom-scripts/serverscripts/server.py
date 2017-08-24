from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import TCPServer
import time
import psutil
import platform
import os.path
import sys
import re

class MyRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        
        current_time = time.localtime()
        elapsed_time = time.localtime(time.time() - server_start)
        cpu_usage = psutil.cpu_percent()
        memory_usage = psutil.virtual_memory()
        
        process_list = ''
    
        for process in psutil.process_iter():
            try:
                process_info = process.as_dict(attrs=['pid', 'name'])
                process_list += "PID " + str(process_info['pid']) + " " + "NAME " + process_info['name'] + "\n"
            except psutil.NoSuchProcess:
                pass
        self.path = '/index.html'
        index_file = open('.'+self.path)
        f = index_file.read()
        re.sub("<H1>Process List</H1>(.+)</P>","<P>"+ process_list  , f)
        re.sub("<H1>System Time</H1>(.+)</P>","<P>"+ current_time  , f)
        re.sub("<H1>System Uptime</H1>(.+)</P>","<P>"+elapsed_time  , f)
        re.sub("<H1>Processor Model</H1>(.+)</P>","<P>"+processor  , f)
        re.sub("<H1>Processor Usage</H1>(.+)</P>","<P>"+cpu_usage  , f)
        re.sub("<H1>Total Ram</H1>(.+)</P>","<P>"+memory_usage  , f)
        re.sub("<H1>System Version</H1>(.+)</P>","<P>"+linux  , f)
        
        index_file.close()
        index_file = open('.'+self.path, 'w')
        index_file.write(f)
        index_file.close()
        print("connection recieved")

        return BaseHTTPRequestHandler.do_GET(self)

re.DOTALL = True
server_start = time.time()
processor = platform.processor()
linux = platform.linux_distribution()

Handler = MyRequestHandler
server = TCPServer(('0.0.0.0', 8094), Handler)
server.serve_forever()
