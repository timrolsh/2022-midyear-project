import pygame, sys
from pygame.locals import *
# from City import *
# from Color import *
# # from Computer import *
from Field import *
# from Goal import *
# from Human import *
# from Player import *
# from Track import *

FPS = 15
DISPLAYX = 1051
DISPLAYY = 750

ORIGINALX = 2941
ORIGINALY = 1958

CITY_COLOR = (219,152,99,1)

pygame.init()
screen=pygame.display.set_mode([DISPLAYX, DISPLAYY])
pygame.display.set_caption("Ticket to Ride")
bg = pygame.image.load("board.jpg")
bg = pygame.transform.scale(bg, (DISPLAYX, DISPLAYY))



def game_loop():
    
    running = True
    while running:

       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if screen.get_at(pygame.mouse.get_pos()) == CITY_COLOR:
                    


        draw_game_area()
        
        pygame.display.update()
        

    pygame.quit()
    
def start_screen():
    #to do
    game_loop()

def draw_game_area():
    screen.blit(bg, (0,0))
    for city in Field.cities.keys():
        city = Field.cities[city]
        pygame.draw.circle(screen, CITY_COLOR, (float(DISPLAYX/ORIGINALX) * float(city.x), float((DISPLAYY/ORIGINALY)) * float(city.y)), 10) 

def main():
    while True:
        start_screen()
        
        
main()


