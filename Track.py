from City import City
from Color import Color

"""This class represents a track between two 
different cities. Upon calling the constructor 
and specifying all the values, the track adds 
itself to two cities' list of tracks."""


class Track:
    def __init__(self, city1: City, city2: City, color: str, length: int, occupied: bool=False):
        self.city1 = city1
        self.city2 = city2
        self.length = length
        self.occupied = occupied
        self.color = Color.COLOR_DICT[color]
