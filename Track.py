from Color import Color

"""This class represents a track between two 
different cities. Upon calling the constructor 
and specifying all the values, the track adds 
itself to two cities' list of tracks."""


class Track:
    def __init__(self, city1, city2, color, length):
        self.city1 = city1
        self.city2 = city2
        self.length = length
        city1.tracks.append(self)
        city2.tracks.append(self)
        if color == "WHITE":
            self.color = Color.WHITE
        elif color == "YELLOW":
            self.color = Color.YELLOW
        elif color == "BLUE":
            self.color = Color.BLUE
        elif color == "BLACK":
            self.color = Color.BLACK
        elif color == "RED":
            self.color = Color.RED
        elif color == "ORANGE":
            self.color = Color.ORANGE
        elif color == "PINK":
            self.color = Color.PINK
        elif color == "GREEN":
            self.color = Color.GREEN
