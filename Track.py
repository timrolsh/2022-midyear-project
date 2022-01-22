from City import City

"""This class represents a track between two 
different cities. Upon calling the constructor 
and specifying all the values, the track adds 
itself to two cities' list of tracks."""


class Track:
    def __init__(self, city1: City, city2: City, color: str, length: int, occupied_by: int=0):
        self.city1 = city1
        self.city2 = city2
        self.city1.tracks.append(self)
        self.city2.tracks.append(self)

        self.length = length

        #0 if not occupied, 1 if occupied by player1, and 2 if occupied by player2
        self.occupied_by = occupied_by

        self.train_cars = []
        self.color = color

    def __str__(self):
        return f"Track from {self.city1} to {self.city2} of color {self.color}"
