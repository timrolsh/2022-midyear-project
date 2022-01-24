from City import City
from Track import Track


class Field:
    cities = {}
    tracks_list = []
    city_list_file = open("data/city_list.txt")
    tracks_list_file = open("data/tracks_list.txt")

    # go through every line in the file of cities and their corresponding coordinates on the
    for line in city_list_file:
        data = line.split(", ")
        cities[data[0]] = City(data[0], int(data[1]), int(data[2]))
    city_list_file.close()

    # create last_track variable to store last track read from file
    last_track = None
    # go through each line in the line of tracks
    for line in tracks_list_file:
        data = line.split(": ")
        # if the line is declaring info about a specific track
        if len(data) == 1:
            data = line.split(", ")
            track = Track(cities[data[0]], cities[data[1]], data[2], int(data[3]))
            tracks_list.append(track)
            last_track = track
        # otherwise, the line must be declaring a traincar with two given points
        else:
            coordinates = data[1].split(", ")
            last_track.add_train_car([data[0], data[1]], [data[2], data[3]])

    tracks_list_file.close()
