from City import City
from Track import Track


class Field:

    def __init__(self):
        self.cities = {}
        city_list = open("data/city_list.txt")
        tracks_list = open("data/tracks_list.txt")
        for line in city_list:
            data = line.split(", ")
            self.cities[data[0]] = City(data[0], data[1], data[2])
        city_list.close()
        for line in tracks_list:
            data = line.split()
            self.cities[data[0]].tracks.append(Track(data[0], data[1], data[2], data[3]))
            self.cities[data[1]].tracks.append(Track(data[1], data[0], data[2], data[3]))
