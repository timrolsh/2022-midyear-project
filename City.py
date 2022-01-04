""" This class is used by the Field class
to store all the cities and their location,
as well as the tracks that the cities are
connected to. Data is read in from city_list.txt
"""


class City:
    def __init__(self, name, x, y):
        self.tracks = []
        self.name = name
        self.x = x
        self.y = y
