from City import City
from Track import Track


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
    for line in track_lines:
        data = line.split(", ")
        cities[data[0]].tracks.append(Track(cities[data[0]], cities[data[1]], data[2], int(data[3])))
        cities[data[1]].tracks.append(Track(cities[data[1]], cities[data[0]], data[2], int(data[3])))
    tracks_list_file.close()

    def __init__(self):
        """"""
