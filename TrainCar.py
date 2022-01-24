""" This class is redundant and does not need to be used in the game. A traincar is simply 4 points denoting its
location, and does not need to be represented by a class. The Track class has a list of train car coordinates,
which Game will scale and use to draw train cars on the field. The color of the train cars will be player's color. """


class TrainCar:
    TRAIN_CAR_LENGTH = 90
    TRAIN_CAR_WIDTH = 30

    def __init__(self, point1, point3):
        self.point1 = point1
        self.point3 = point3

        self.point2, self.point4 = self.find_rect_points(point1, point3)

    def find_rect_points(self, point1, point3):
        x1 = point1[0]
        y1 = point1[1]
        x3 = point3[0]
        y3 = point3[1]

        distance = ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** 0.5
        rotated = ((complex(x3 - x1, y3 - y1) * complex(TrainCar.TRAIN_CAR_LENGTH / distance,
                                                        -1 * TrainCar.TRAIN_CAR_WIDTH / distance) * (
                            TrainCar.TRAIN_CAR_LENGTH / distance)) + complex(x1, y1))

        point4 = rotated.real, rotated.imag

        rotated = ((complex(x1 - x3, y1 - y3) * complex(TrainCar.TRAIN_CAR_LENGTH / distance,
                                                        -1 * TrainCar.TRAIN_CAR_WIDTH / distance) * (
                            TrainCar.TRAIN_CAR_LENGTH / distance)) + complex(x3, y3))

        point2 = rotated.real, rotated.imag

        return [point2, point4]
