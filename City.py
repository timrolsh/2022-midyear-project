""" This class is used by the Field class
to store all the cities and their location,
as well as the tracks that the cities are
connected to. Data is read in from city_list.txt
"""


class City:
    """
    Represents a city in ticket to ride. Contains a list of outgoing tracks from the city, the name of the city,
    and the x and y coordinates of the city on the board.
    """

    def __init__(self, name: str, x: int, y: int):
        self.tracks = []
        self.name = name
        self.x = x
        self.y = y

    def __str__(self):
        return f"City {self.name}"
