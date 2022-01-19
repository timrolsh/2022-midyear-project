import pygame, sys
from pygame.locals import *
# from City import *
# from Color import *
# # from Computer import *
# from Field import *
# from Goal import *
# from Human import *
# from Player import *
# from Track import *

FPS = 15
DISPLAYX = 1000
DISPLAYY = 600


pygame.init()
screen=pygame.display.set_mode([DISPLAYX, DISPLAYY])
pygame.display.set_caption("Ticket to Ride")
bg = pygame.image.load("board.jpg")
bg = pygame.transform.scale(bg, (1000, 600))

def game_loop():
    
    running = True
    while running:

       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_game_area()
        
        pygame.display.update()
        

    pygame.quit()
    
def start_screen():
    #to do
    game_loop()

def draw_game_area():
    screen.blit(bg, (0,0))
    #add appropriate overlays, buttons

def main():
    while True:
        start_screen()
        
        
main()


