#!/usr/bin/env python3
from http.server import HTTPServer, SimpleHTTPRequestHandler
from socketserver import ThreadingMixIn
import sys
import os
import re
import urllib.parse

HOST = os.getenv("HOST", "127.0.0.1")
PORT = int(os.getenv("PORT", 1338)) # for local development on another port than docker

class TaskHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # if self.path == "/":
        self.path = "index.html"
        return SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = urllib.parse.parse_qs(post_data.decode('utf-8'))
        
        print("Received POST data:", data)

        response = "<html><body><h1>Hack-a-Calc Boundary Escapade</h1><h2>Result:</h2><ul>"
        for key, value in data.items():
            if key == "calculation":
                output = self.calculator(value[0])
                if output is None:
                    return
                print(output)
                response += f"<li>{value[0]} = {output}</li>"
                break
            else: response += "no data"
        response += "</ul></body></html>"

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.send_header("User-Agent", "ZmxhZ3t0aGF0X3dhc19lYXN5fQo=")
        self.end_headers()
        self.wfile.write(response.encode('utf-8'))

    def calculator(self, input):
        # Regular expression to allow only arithmetic operations and numbers
        if not re.match(r'^[\d&-|+^*/().]{3,50}$', input):
            print()
            self.fail()
            return

        try:
            result = eval(input)
            print("Result:", result)
            return result
        except Exception as e:
            print("Error:", e)
            self.fail()

    def fail(self):
        self.send_response(400)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        response = "<html><body>Invalid input. Please enter a valid calculation.</body></html>"
        self.wfile.write(response.encode('utf-8'))

class ThreadedTCPServer(ThreadingMixIn, HTTPServer):
    allow_reuse_address = True

if __name__ == "__main__":
    server = ThreadedTCPServer((HOST, PORT), TaskHandler)
    
    try:
        print(f"Starting server on port {PORT}...")
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server...")
    finally:
        server.server_close()
