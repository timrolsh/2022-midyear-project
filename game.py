import os
#hide pygame welcome message
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame, sys
from pygame.locals import *
# from City import *
# from Color import *
# # from Computer import *
from Field import *
from IntervalQuadTree import IntervalQuadTree
from Button import Button
# from Goal import *
# from Human import *
# from Player import *
# from Track import *

FPS = 15
DISPLAYX = 955
DISPLAYY = 682

ORIGINALX = 2941
ORIGINALY = 1958

CITY_COLOR = (219,152,99,1)
CITY_RADIUS=10

buttons = []

city_quad_tree = IntervalQuadTree()


#pygame main loop
def game_loop(screen):
    
    running = True
    while running:

       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                current_pos = pygame.mouse.get_pos()
                print(current_pos[0], current_pos[1])
                print(city_quad_tree.search_interval(current_pos[0], current_pos[1]))
            

        draw_game_area(screen)
        
        pygame.display.update()
        

    pygame.quit()

#run the gameloop
def start_screen(screen):
    #to do
    game_loop(screen)

first_pass = True

#draw all the components of the game
def draw_game_area(screen):
    global first_pass
    for city in Field.cities.keys():
        city = Field.cities[city]
        circle_x = float((DISPLAYX/ORIGINALX) * float(city.x))
        circle_y = float((DISPLAYY/ORIGINALY) * float(city.y))
        pygame.draw.circle(screen, CITY_COLOR, (circle_x, circle_y), CITY_RADIUS) 
        if first_pass:
            button = Button(circle_x, circle_y, 20, 20)
            city_quad_tree.add_interval(button)
    first_pass=False
        

def main():
    pygame.init()
    screen=pygame.display.set_mode([DISPLAYX, DISPLAYY])
    pygame.display.set_caption("Ticket to Ride")
    background = pygame.image.load("board.jpg")
    background = pygame.transform.scale(background, (DISPLAYX, DISPLAYY))
    screen.blit(background, (0,0))
    while True:
        start_screen(screen)
        
if __name__=='__main__':   
    main()


