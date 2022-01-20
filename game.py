import os
import pygame
from Field import *
from Button import Button
from Color import *;
# hide pygame welcome message
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

FPS = 15
DISPLAYX = 955
DISPLAYY = 682

ORIGINALX = 2941
ORIGINALY = 1958

CITY_COLOR = (219, 152, 99)
CITY_RADIUS = 10

FONT = "freesansbold.ttf"


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
    font = pygame.font.Font(FONT, 60)
    play_font = pygame.font.Font(FONT, 30)
    

    font_surface = font.render("Ticket to Ride", True, Color.COLOR_DICT.get("BLACK"))
    play_surface = play_font.render("Press P to Play", True, Color.COLOR_DICT.get("BLACK"))
   

    rect_font = font_surface.get_rect()
    play_rect_font = play_surface.get_rect()

    rect_font.center = ((DISPLAYX / 2), (DISPLAYY / 2))
    play_rect_font.center = ((DISPLAYX / 2), (DISPLAYY / 1.65))
    
    draw_game_area(screen)
    screen.blit(font_surface, rect_font)
    screen.blit(play_surface, play_rect_font)
    
    pygame.display.update()
    # game_loop(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_p:
                    screen.fill(Color.COLOR_DICT("WHITE"))
                    game_loop(screen)
                
            
        pygame.time.Clock().tick(FPS)
    
    pygame.display.update()

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

#Method for text
def text(text, font, screen):
    textsurface = font.render(text, True, Color.COLOR_DICT.get("BLACK"))
    return textsurface, textsurface.get_rect()

def displayScores(screen):
    title = pygame.font.Font(FONT, 60)
    title_surface = title.render("", True, Color.COLOR_DICT.get("BLACK"))
    # title_rect = 
    
    screen.blit(title_surface, title)

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
