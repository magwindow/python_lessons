from socketserver import StreamRequestHandler, TCPServer
from functools import partial

class EchoHandler(StreamRequestHandler):
    def handle(self):
        for line in self.rfile:
            self.wfile.write(b'GOT:' + line)
            

class EchoHandler(StreamRequestHandler):
    # ack – это добавленный обязательный именованный аргумент.
    # *args, **kwargs – это любые обычные предоставленные параметры
    # (которые переданы)
    def __init__(self, *args, ack, **kwargs):
        self.ack = ack
        super().__init__(*args, **kwargs)
    
    def handle(self):
        for line in self.rfile:
            self.wfile.write(self.ack + line)



server = TCPServer(('', 15000), partial(EchoHandler, ack=b'RECEIVED:'))
# server = TCPServer(('', 15000), lambda *args, **kwargs: EchoHandler(*args, ack=b'RECEIVED:', **kwargs))
server.serve_forever()