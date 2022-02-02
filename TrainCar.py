class TrainCar:

    TRAIN_CAR_LENGTH = 93
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
                                                        -1*TrainCar.TRAIN_CAR_WIDTH / distance) * (
            TrainCar.TRAIN_CAR_LENGTH / distance)) + complex(x1, y1))

        point4 = rotated.real, rotated.imag

        rotated = ((complex(x1 - x3, y1 - y3) * complex(TrainCar.TRAIN_CAR_LENGTH / distance,
                                                        -1*TrainCar.TRAIN_CAR_WIDTH / distance) * (
            TrainCar.TRAIN_CAR_LENGTH / distance)) + complex(x3, y3))

        point2 = rotated.real, rotated.imag

        return [point2, point4]

    def check_in_rectangle(self, point):
        pairs = [(self.point4, self.point1), (self.point1, self.point2),
                 (self.point2, self.point3), (self.point3, self.point4)]

        """
        not_outside = True
        for point1, point2 in pairs:
            x_point = point[0]
            y_point = point[1]
            x_1, y_1 = point1
            x_2, y_2 = point2

            coeff1 = -1*(y_2-y_1)
            coeff2 = x_2-x_1
            coeff3 = -1*(coeff1 * x_1 + coeff2 * y_1)

            is_outside = coeff1*x_point+coeff2*y_point+coeff3
            if is_outside<0:
                not_outside = False
        """
        total_area = 0
        x_3, y_3 = point
        for point1, point2 in pairs:
            x_1, y_1 = point1
            x_2, y_2 = point2
            triangle_area = abs(
                (0.5)*(x_1*(y_2-y_3)+x_2*(y_3-y_1)+x_3*(y_1-y_2)))
            total_area += triangle_area

        return abs(total_area-self.TRAIN_CAR_LENGTH*self.TRAIN_CAR_WIDTH) <= 20
