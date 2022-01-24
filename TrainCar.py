from DisplayVars import DISPLAYX, ORIGINALX
class TrainCar():

    TRAIN_CAR_LENGTH = 90*(DISPLAYX/ORIGINALX)
    TRAIN_CAR_WIDTH =30*(DISPLAYX/ORIGINALX)

    def __init__(self, point1, point3):
        self.point1 = point1
        self.point3 = point3

        self.point2, self.point4 = self.find_rect_points(point1, point3)

    def find_rect_points(self, point1, point3):
        
        x1 = point1[0]
        y1 = point1[1]
        x3 = point3[0]
        y3 = point3[1]

        distance = ((x1-x3)**2+(y1-y3)**2)**0.5
        rotated = ((complex(x3-x1, y3-y1)*complex(TrainCar.TRAIN_CAR_LENGTH/distance, -1*TrainCar.TRAIN_CAR_WIDTH/distance)*(TrainCar.TRAIN_CAR_LENGTH/distance))+complex(x1, y1))

        point4 = rotated.real, rotated.imag

        rotated = ((complex(x1-x3, y1-y3)*complex(TrainCar.TRAIN_CAR_LENGTH/distance, -1*TrainCar.TRAIN_CAR_WIDTH/distance)*(TrainCar.TRAIN_CAR_LENGTH/distance))+complex(x3, y3))

        point2 = rotated.real, rotated.imag

        return [point2, point4]
    
