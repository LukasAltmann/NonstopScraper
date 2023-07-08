from json import JSONEncoder


class Event:
    def __init__(self, title, place, time):
        self.title = title
        self.place = place
        self.time = time


class EventEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
