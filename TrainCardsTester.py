import math
import time

import pygame

game_width = 1280
game_height = 720

pygame.init()
original_image = pygame.image.load("board.jpg")
image_surface = pygame.transform.scale(
    original_image, (game_width, game_height))
display = pygame.display.set_mode(
    (image_surface.get_width(), image_surface.get_height()))
display.blit(image_surface, (0, 0))
image_scale_width = game_width / original_image.get_width()
image_scale_height = game_height / original_image.get_height()
car_length = 90
car_width = 30
tracks_list = open("data/tracks_list.txt")
for line in tracks_list:
    temp_line = line.split(": ")
    if temp_line[0] == "traincar":
        temp_line = temp_line[1].split(", ")
        ab = [float(temp_line[0]), float(temp_line[1])]
        cd = [float(temp_line[2]), float(temp_line[3])]
        if ab[0] > cd[0]:
            temp = ab
            ab = cd
            cd = temp
        if ab[1] < cd[1]:
            rotation_angle = (math.atan(car_length / car_width)) - \
                (math.atan((cd[0] - ab[0]) / (cd[1] - ab[1])))
            point2 = [(ab[0] + math.cos(rotation_angle) * car_length),
                      (ab[1] + math.sin(rotation_angle) * car_length)]
            point4 = [(cd[0] - math.cos(rotation_angle) * car_length),
                      (cd[1] - math.sin(rotation_angle) * car_length)]
        else:
            rotation_angle = (math.atan(
                (ab[1] - cd[1]) / (cd[0] - ab[0]))) + (math.atan(car_width / car_length))
            point2 = [(ab[0] + car_length * math.cos(rotation_angle)),
                      (ab[1] - car_length * math.sin(rotation_angle))]
            point4 = [(cd[0] - car_length * math.cos(rotation_angle)),
                      (cd[1] + car_length * math.sin(rotation_angle))]
        ab[0] = int(ab[0] * image_scale_width)
        ab[1] = int(ab[1] * image_scale_height)
        cd[0] = int(cd[0] * image_scale_width)
        cd[1] = int(cd[1] * image_scale_height)
        point2[0] = int(point2[0] * image_scale_width)
        point2[1] = int(point2[1] * image_scale_height)
        point4[0] = int(point4[0] * image_scale_width)
        point4[1] = int(point4[1] * image_scale_height)
        pygame.draw.polygon(display, (0, 0, 255), [ab, point2, cd, point4])

pygame.display.update()
time.sleep(100)
