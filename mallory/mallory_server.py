from http.server import BaseHTTPRequestHandler, HTTPServer
from http.client import HTTPSConnection
from urllib import parse
import sys
import subprocess
from multiprocessing import Process

class Server(BaseHTTPRequestHandler):

    # GET request handler 
    def do_GET(self):
        # retrieve the path from the HTTP request
        path = self.path
        # retrieve the headers from the HTTP request
        headers = self.headers
        # retrieve the body from the HTTP request
        body = None
        
        if self.headers.get('content-length'):
            body = self.rfile.read(int(self.headers.get('content-length')))

        # send an HTTP request to another server and get the response
        conn = HTTPSConnection(headers['host'])
        method = 'GET'
        conn.request(method, path, body, headers)
        # and get the response back 
        res = conn.getresponse()
        conn.close()

        # set HTTP response status code and body
        self.send_response(201, 'Welcome to DarkLab')
        # set HTTP reponse headers
        self.send_header('Content-type','text/html')
        self.end_headers()

        return


    # POST request handler 
    def do_POST(self):
        path = self.path
        headers = self.headers
        body = None
        
        if self.headers.get('content-length'):
            body = self.rfile.read(int(self.headers.get('content-length')))

        # send an HTTP request to another server and get the response
        conn = HTTPSConnection(headers['host'])
        method = 'POST'
        conn.request(method, path, body, headers)

        res = conn.getresponse()
        conn.close()

        self.send_response(201, 'Welcome to DarkLab')
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        return
      
    # PUT request handler     
    def do_PUT(self):
        path = self.path
        headers = self.headers
        body = None
        
        if self.headers.get('content-length'):
            body = self.rfile.read(int(self.headers.get('content-length')))

        # send an HTTP request to another server and get the response
        conn = HTTPSConnection(headers['host'])
        method = 'PUT'
        conn.request(method, path, body, headers)

        res = conn.getresponse()
        conn.close()

        self.send_response(201, 'Welcome to DarkLab')
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        return
        

httpd = HTTPServer(('', 80), Server)
httpd.serve_forever()
