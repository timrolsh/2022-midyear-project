from ast import Or
import os
import pygame
from Field import Field
from Button import Button
from Color import Color
from Deck import Deck
from Player import Player
from Human import Human
# from Computer import Computer

# hide pygame welcome message
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

# define essential parameters for the game
original_image = pygame.image.load("board.jpg")
CITY_COLOR = (219, 152, 99)
CITY_RADIUS = 10
FONT = "freesansbold.ttf"
deck = Deck()
Players = []
COLORS = {"WHITE": (255, 255, 255), "YELLOW": (252, 239, 108), "BLUE": (67, 147, 242), "BLACK": (69, 70, 74),
          "RED": (201, 88, 80), "ORANGE": (214, 139, 84), "PINK": (201, 134, 175), "GREEN": (169, 195, 86),
          "GRAY": (128, 128, 128)}

# define original image dimensions
ORIGINAL_WIDTH = original_image.get_width()
ORIGINAL_HEIGHT = original_image.get_height()

"""THESE OPTIONS ARE CUSTOMIZABLE BY THE USER, GAME WILL PROPERLY SCALE TO THE DIMENSIONS SPECIFIED"""
FPS = 15
DISPLAY_WIDTH = 955
DISPLAY_HEIGHT = 636

def scale(point):
    scale_factor = DISPLAY_WIDTH/ORIGINAL_WIDTH
    if type(point)==int:
        return scale_factor*point
    else:
        return tuple(point[i]*scale_factor for i in range(len(point)))

"""Please define the players you want to play by calling the constructor for either human or player class, 
and then specifying a color from the colors dictionary provided of sample colors. Or, you can make your own color! 
Colors are represented by tuple values of three RGB values. """
PLAYERS = [Human(COLORS["BLUE"]), Human(COLORS["GREEN"])]


def draw_train_cars(screen):
    for track in Field.tracks_list:
        if (track.occupied_by!=None):
            for train_car in track.train_cars:
                pygame.draw.polygon(screen, track.occupied_by.color, (scale(train_car.point1), scale(train_car.point2), scale(train_car.point3), scale(train_car.point4)))

# pygame main loop
def game_loop(screen, debug, background):
    running = True
    player1_train_cards = deck.discard_train_cards(4)
    player2_train_cards = deck.discard_train_cards(4)
    top5_cards = deck.discard_train_cards(5)

    player1_destination_cards = deck.discard_destination_cards(3)
    player2_destination_cards = deck.discard_destination_cards(3)

    #setting the colors to red/blue manually for now
    player1 = PLAYERS[0]
    player2 = PLAYERS[1]
    
    player1.train_cards = player1_train_cards
    player2.train_cards = player2_train_cards
    
    player1.destination_cards = player1_destination_cards
    player2.destination_cards = player2_destination_cards
    
    screen.blit(background, (0, 0))
    current_turn = 0
    if (debug):
        print("Debug mode on")
        print("Player1 Train Cards: " + str(len(player1.train_cards)))
        print("Player2 Train Cards: " + str(len(player2.train_cards)))
        print("Train cards in deck: " + str(len(deck.train_cards)))

    # Before start: prompt player to keep at least 2 cards (discard at most one)
    # Idea: Show player 1 their destination cards then click
    # on one of them to discard OR click on separate button to not discard any.
    # ^do the same for player2

    color = player1.color
    while running:

        draw_train_cars(screen)

        turn_complete = False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                current_pos = pygame.mouse.get_pos()

                is_clicked = False
                for track in Field.tracks_list:
                    if track.occupied_by!=None:
                        continue
                    for train_car in track.train_cars:
                        if train_car.check_in_rectangle(tuple(i*(ORIGINAL_WIDTH/DISPLAY_WIDTH) for i in current_pos)):
                            is_clicked = True
                            break
                    if is_clicked:
                        break
                if is_clicked:
                    track.occupied_by = PLAYERS[current_turn]
                    turn_complete = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
                    player_card_tab(screen, background, current_turn)
                    

        # Change turns
        if (turn_complete):
            if current_turn == 0:
                current_turn = 1
            else:
                current_turn = 0
            color = PLAYERS[current_turn].color
            if (debug):
                print("Player: " + str(current_turn))
            
            #to be completed
            #player_prompt(PLAYERS[current_turn], screen, background, current_turn)
            

        draw_game_area(screen)
        display_scores(screen, player1, player2)
        pygame.display.update()

    pygame.quit()


# run the gameloop
def start_screen(screen, background):
    font = pygame.font.Font(FONT, 60)
    play_font = pygame.font.Font(FONT, 30)

    draw_game_area(screen)
    draw_text("Ticket to Ride", font, "BLACK", screen, (DISPLAY_WIDTH / 2), (DISPLAY_HEIGHT / 2))
    draw_text("Press P to Play", play_font, "BLACK", screen, (DISPLAY_WIDTH / 2), (DISPLAY_HEIGHT / 1.65))

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_p:
                    game_loop(screen, True, background)

        pygame.time.Clock().tick(FPS)

    pygame.display.update()


def player_card_tab(screen, background, current_player):
    screen.blit(background, (0, 0))
    font = pygame.font.Font(FONT, 60)

    draw_game_area(screen)
    draw_text("Player " + str(current_player+1) + " Cards", font, "BLACK", screen, (DISPLAY_WIDTH / 2), (DISPLAY_HEIGHT / 2))

    pygame.display.update()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_TAB:
                    screen.blit(background, (0, 0))
                    running = False
                    

        pygame.time.Clock().tick(FPS)

    pygame.display.update()





first_creation_pass = True

city_buttons = []


# draw all the components of the game
def draw_game_area(screen):
    global first_creation_pass
    for city in Field.cities.keys():
        city = Field.cities[city]
        circle_x = float((DISPLAY_WIDTH / ORIGINAL_WIDTH) * float(city.x))
        circle_y = float((DISPLAY_HEIGHT / ORIGINAL_HEIGHT) * float(city.y))
        pygame.draw.circle(screen, CITY_COLOR, (circle_x, circle_y), CITY_RADIUS)
        if first_creation_pass:
            city_button = Button(circle_x, circle_y, 20, 20)
            city_buttons.append(city_button)
    first_creation_pass = False

def player_prompt(player, screen, background, current_turn):
    
    #Draw three buttons for options
    font = pygame.font.Font(FONT, 60)

    draw_game_area(screen)
    
    draw_text("Player " + str(current_turn+1) + " choose a move", font, "BLACK", screen, (DISPLAY_WIDTH / 2), (DISPLAY_HEIGHT / 2))

    pygame.display.update()
    
    #Create buttons later
    
    

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_TAB:
                    screen.blit(background, (0, 0))
                    running = False
                if event.key == pygame.K_1:
                    break
                if event.key == pygame.K_2:
                    #draw?
                    break
                if event.key == pygame.K_3:
                    break

        pygame.time.Clock().tick(FPS)

    pygame.display.update()
    draw_game_area(screen)
    


# Method for text
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, 1, Color.COLOR_DICT.get(color))
    rect = text_obj.get_rect()
    rect.center = (x, y)
    surface.blit(text_obj, rect)


def display_scores(screen, p1, p2):
    font = pygame.font.Font(FONT, 30)
    draw_text("Player 1: " + str(p1.score), font, "BLACK", screen, DISPLAY_WIDTH / 1.25, DISPLAY_HEIGHT / 1.25)
    draw_text("Player 2: " + str(p2.score), font, "BLACK", screen, DISPLAY_WIDTH / 1.25, DISPLAY_HEIGHT / 1.15)


def main():
    pygame.init()
    screen = pygame.display.set_mode([DISPLAY_WIDTH, DISPLAY_HEIGHT])
    pygame.display.set_caption("Ticket to Ride")
    background = pygame.image.load("board.jpg")
    background = pygame.transform.scale(background, (DISPLAY_WIDTH, DISPLAY_HEIGHT))
    screen.blit(background, (0, 0))
    while True:
        start_screen(screen, background)


if __name__ == '__main__':
    main()
