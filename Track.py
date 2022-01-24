import math

from City import City
from Player import Player
from Field import Field

"""This class represents a track between two different cities. Upon calling the constructor and specifying all the 
values, the track adds itself to two cities' list of tracks. """


class Track:
    def __init__(self, city1: City, city2: City, color: str, length: int, occupied_by: Player = None):
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
    def add_train_car(self, point1: [int, int], point3: [int, int]):
        # trig code that can be replaced with complex number code
        if point1[1] < point3[1]:
            rotation_angle = (math.atan(Field.TRAIN_CAR_LENGTH / Field.TRAIN_CAR_WIDTH)) - (
                math.atan((point3[0] - point1[0]) / (point3[1] - point1[1])))
            point2 = [(point1[0] + math.cos(rotation_angle) * Field.TRAIN_CAR_LENGTH),
                      (point1[1] + math.sin(rotation_angle) * Field.TRAIN_CAR_LENGTH)]
            point4 = [(point3[0] - math.cos(rotation_angle) * Field.TRAIN_CAR_LENGTH),
                      (point3[1] - math.sin(rotation_angle) * Field.TRAIN_CAR_LENGTH)]
        else:
            rotation_angle = (math.atan((point1[1] - point3[1]) / (point3[0] - point1[0]))) + (
                math.atan(Field.TRAIN_CAR_WIDTH / Field.TRAIN_CAR_LENGTH))
            point2 = [(point1[0] + Field.TRAIN_CAR_LENGTH * math.cos(rotation_angle)),
                      (point1[1] - Field.TRAIN_CAR_LENGTH * math.sin(rotation_angle))]
            point4 = [(point3[0] - Field.TRAIN_CAR_LENGTH * math.cos(rotation_angle)),
                      (point3[1] + Field.TRAIN_CAR_LENGTH * math.sin(rotation_angle))]
        # round all to integers
        point1[0] = int(point1[0])
        point1[1] = int(point1[1])
        point3[0] = int(point3[0])
        point3[1] = int(point3[1])
        point2[0] = int(point2[0])
        point2[1] = int(point2[1])
        point4[0] = int(point4[0])
        point4[1] = int(point4[1])
        self.train_cars.append([point1, point2, point3, point4])

    def __str__(self):
        return f"Track from {self.city1} to {self.city2} of color {self.color}"
