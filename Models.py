import json
import serial
import threading

from flask_socketio import SocketIO, emit

class Payload(object):
    def __init__(self, j):
        self.__dict__ = json.loads(j)


class flood_reading:
    def __init__(self,title,subtitle,message):
        self.title = title
        self.subtitle = subtitle
        self.message = message

def read_from_port(ser):
    while True:
        reading = ser.readline().decode()
        print(reading)


class serial_reader:
    def __init__(self,port_name):
        ser = serial.Serial(port_name,9600)


        thread = threading.Thread(target=read_from_port,
                                   args=(ser,))
        thread.start()

switch = -1
def handle_my_custom_event(json,switch):
    emit('my response', str(switch))
    print(str(switch))

def repeat_socket(app):
    switch = 1
    app.socketio = SocketIO(app)
    print("repeat socket is running")
    while True:
        #("Nothing for now",switch)
        switch *=-1
        print(str(switch))