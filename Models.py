import json

class Payload(object):
    def __init__(self, j):
        self.__dict__ = json.loads(j)

class flood_reading:
    def __init__(self,title,subtitle,message):
        self.title = title
        self.subtitle = subtitle
        self.message = message