import http.server
import socketserver

PORT=4444

class myHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        self.request.sendall(self.data.lower())
    
    def do_GET(self):
        header = "Content-Type: text/html\r\n"
        f = open('index.html', 'r')
        dataToSend = header
        for line in f:
            dataToSend = dataToSend + line
        self.request.sendall(dataToSend)

with socketserver.TCPServer(("", PORT), myHandler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
