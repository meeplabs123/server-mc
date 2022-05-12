# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import sys
import subprocess

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>Server Is Up</title></head>", "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>Server IP:   " + sys.argv[1] + "</p>", "utf-8"))
        self.wfile.write(bytes("<p>MCSrvStatus:   https://mcsrvstat.us/server/" + sys.argv[1] + "</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))
    subprocess.Popen("python3 discord/main.py \"" + sys.argv[1] + "\"", stdout=subprocess.PIPE, shell=True)

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
