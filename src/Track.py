from src.City import City
from src.TrainCar import TrainCar

"""This class represents a track between two different cities. Upon calling the constructor and specifying all the 
values, the track adds itself to two cities' list of tracks. """


class Track:
    def __init__(self, city1: City, city2: City, color: str, length: int, occupied_by=None):
        self.city1 = city1
        self.city2 = city2
        self.city1.tracks.append(self)
        self.city2.tracks.append(self)
        self.length = length
        self.occupied_by = occupied_by
        self.train_cars = []
        self.color = color

    """Given two points, point1 and point3(opposite points of a rectangle), this method adds all four points of the 
    rectangle to the Track class's train_cars list """

    def add_train_car(self, point1: (int, int), point3: (int, int)):
        self.train_cars.append(TrainCar(point1, point3))

    def __str__(self):
        return f"Track from {self.city1} to {self.city2} of color {self.color} with length {self.length}"
