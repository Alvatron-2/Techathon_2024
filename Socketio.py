import socketio
from aiohttp import web

class SocketIOServer(socketio.AsyncNamespace):
    def __init__(self):
        super().__init__()
        self.sio = socketio.AsyncServer()
        self.sio.register_namespace(self)
        self.app = web.Application()
        self.sio.attach(self.app)
        self.task = None

    def run(self):
        web.run_app(self.app, port=8080)

    def start(self):
        self.task = self.sio.start_background_task(self.run)
        

if __name__ == '__main__':
    server = SocketIOServer()
    server.start()
    print("Started!")
    # Continue executing code here
