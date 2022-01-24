from City import City
from Track import Track
from TrainCar import TrainCar
from DisplayVars import DISPLAYX, ORIGINALX

class Field:

    cities = {}
    city_list_file = open("data/city_list.txt")
    tracks_list_file = open("data/tracks_list.txt")

    city_lines = city_list_file.read().split('\n')
    for line in city_lines:
        data = line.split(", ")
        cities[data[0]] = City(data[0], int(data[1]), int(data[2]))  # cast the coordinates to integers since they
        # come out of line.split as strings
    city_list_file.close()

    track_lines = tracks_list_file.read().split('\n')
    tracks_list = []

    #go through each line in the line of tracks
    for line in track_lines:

        #if the line is a train car, get the coordinates of the train car and append them to the current track
        if line[0:5]=="train":
            current_train_car = line.split(': ')[1]
            coordinates = current_train_car.split(', ')
            point1 = (int(coordinates[0])*(DISPLAYX/ORIGINALX), int(coordinates[1])*(DISPLAYX/ORIGINALX))
            point3 = (int(coordinates[2])*(DISPLAYX/ORIGINALX), int(coordinates[3])*(DISPLAYX/ORIGINALX))
            train_car_object = TrainCar(point1, point3)
            track.train_cars.append(train_car_object)
        else:
            #otherwise, create a new track object that the next train cars will be added to
            data = line.split(", ")
            track = Track(cities[data[0]], cities[data[1]], data[2], int(data[3]))
            tracks_list.append(track)

    tracks_list_file.close()

    def __init__(self):
        """"""
