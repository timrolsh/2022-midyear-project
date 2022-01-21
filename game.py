import os
import pygame
from Field import *
from Button import Button

# hide pygame welcome message
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

FPS = 15
DISPLAYX = 955
DISPLAYY = 682

ORIGINALX = 2941
ORIGINALY = 1958

CITY_COLOR = (219, 152, 99)
CITY_RADIUS = 10

TRAIN_CAR_WIDTH=30
TRAIN_CAR_LENGTH=90

def find_rect_points(point1, point3):
    global TRAIN_CAR_WIDTH
    global TRAIN_CAR_LENGTH
    
    x1=point1[0]
    y1 = point1[1]
    x3 = point3[0]
    y3 = point3[1]

    distance = ((x1-x3)**2+(y1-y3)**2)**0.5
    rotated = ((complex(x3-x1, y3-y1)*complex(TRAIN_CAR_LENGTH/distance, TRAIN_CAR_WIDTH/distance)*(TRAIN_CAR_LENGTH/distance))+complex(x1, y1))

    point4 = rotated.real, rotated.imag

    rotated = ((complex(x1-x3, y1-y3)*complex(TRAIN_CAR_LENGTH/distance, TRAIN_CAR_WIDTH/distance)*(TRAIN_CAR_LENGTH/distance))+complex(x3, y3))

    point2 = rotated.real, rotated.imag

    return [point2, point4]


# pygame main loop
def game_loop(screen):
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                current_pos = pygame.mouse.get_pos()
                if screen.get_at(current_pos) == CITY_COLOR:
                    for button in city_buttons:
                        if (button.x - 10) <= current_pos[0] <= (button.x + 10) and (button.y - 10) <= current_pos[1] \
                                <= (button.y + 10):
                            print(button)

        draw_game_area(screen)

        pygame.display.update()

    pygame.quit()


# run the gameloop
def start_screen(screen):
    # to do
    game_loop(screen)


first_creation_pass = True

city_buttons = []


# draw all the components of the game
def draw_game_area(screen):
    global first_creation_pass
    for city in Field.cities.keys():
        city = Field.cities[city]
        circle_x = float((DISPLAYX / ORIGINALX) * float(city.x))
        circle_y = float((DISPLAYY / ORIGINALY) * float(city.y))
        pygame.draw.circle(screen, CITY_COLOR, (circle_x, circle_y), CITY_RADIUS)
        if first_creation_pass:
            city_button = Button(circle_x, circle_y, 20, 20)
            city_buttons.append(city_button)
    first_creation_pass = False


def main():
    pygame.init()
    screen = pygame.display.set_mode([DISPLAYX, DISPLAYY])
    pygame.display.set_caption("Ticket to Ride")
    background = pygame.image.load("board.jpg")
    background = pygame.transform.scale(background, (DISPLAYX, DISPLAYY))
    screen.blit(background, (0, 0))
    while True:
        start_screen(screen)


if __name__ == '__main__':
    main()
