from flask import Flask

app = Flask(__name__)
import serial
import threading
import pyuac

from Models import serial_reader,repeat_socket
import routes

from flask_socketio import SocketIO

app.config['SECRET_KEY'] = 'secret!'




if __name__ == "__main__":
    #app.Serial_Reader = serial_reader("COM3")
    
    #x = threading.Thread(target=repeat_socket)
    #x.start(app)
    #app.socketio.run(app)
    app.run(debug=True)
    