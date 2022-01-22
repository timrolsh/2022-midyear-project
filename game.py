import os
import pygame
from Field import *
from Button import Button
from Color import *
from Deck import *
from Player import *
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
def game_loop(screen, debug, background):
    running = True
    
    
    #GAME SETUP
    deck = Deck()
    current_turn = 0
    
    player1_train_cards = deck.discard_train_card(4)
    player2_train_cards = deck.discard_train_card(4)
    top5_cards = deck.discard_train_card(5)
    
    player1_destination_cards = deck.discard_destination_cards(3)
    player2_destination_cards = deck.discard_destination_cards(3)
    
    player1 = Player(player1_train_cards, player1_destination_cards)
    player2 = Player(player2_train_cards, player2_destination_cards)
    
    screen.blit(background, (0, 0))
    if (debug):
        print("Debug mode on")
        print("Player1 Train Cards: " + str(len(player1.train_cards)))
        print("Player2 Train Cards: " + str(len(player2.train_cards)))
        print("Train cards in deck: " + str(len(deck.train_cards)))
    
    #Before start: prompt player to keep at least 2 cards (discard at most one)
    #Idea: Show player 1 their destination cards then click 
    # on one of them to discard OR click on separate button to not discard any.
    #^do the same for player2
    while running:
        
        
        
        turn_complete = False
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
                    player1_card_tab(screen, background)
        
        
        #Change turns
        if (turn_complete):      
            if current_turn == 0:
                current_turn = 1
            else:
                current_turn = 0
            if (debug):
                print("Player: " + str(current_turn))
            
        
        
            
                

        draw_game_area(screen)
        display_scores(screen, player1, player2)
        pygame.display.update()

    pygame.quit()


# run the gameloop
def start_screen(screen, background):
    font = pygame.font.Font(FONT, 60)
    play_font = pygame.font.Font(FONT, 30)
    
    draw_game_area(screen)
    draw_text("Ticket to Ride", font, "BLACK", screen, (DISPLAYX / 2), (DISPLAYY / 2))
    draw_text("Press P to Play", play_font, "BLACK", screen, (DISPLAYX / 2), (DISPLAYY / 1.65))
    
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

def player1_card_tab(screen, background):
    screen.blit(background, (0, 0))
    font = pygame.font.Font(FONT, 60)
    
    draw_game_area(screen)
    draw_text("Player 1 Cards", font, "BLACK", screen, (DISPLAYX / 2), (DISPLAYY / 2))
    
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
                    player2_card_tab(screen, background)
                
            
        pygame.time.Clock().tick(FPS)
    
    pygame.display.update()

def player2_card_tab(screen, background):
    font = pygame.font.Font(FONT, 60)
    
    draw_game_area(screen)
    draw_text("Player 2 Cards", font, "BLACK", screen, (DISPLAYX / 2), (DISPLAYY / 2))
    
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
        circle_x = float((DISPLAYX / ORIGINALX) * float(city.x))
        circle_y = float((DISPLAYY / ORIGINALY) * float(city.y))
        pygame.draw.circle(screen, CITY_COLOR, (circle_x, circle_y), CITY_RADIUS)
        if first_creation_pass:
            city_button = Button(circle_x, circle_y, 20, 20)
            city_buttons.append(city_button)
    first_creation_pass = False
    

#Method for text
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, 1, Color.COLOR_DICT.get(color))
    rect = text_obj.get_rect()
    rect.center = (x, y)
    surface.blit(text_obj, rect)
    
def display_scores(screen, p1, p2):
    font = pygame.font.Font(FONT, 30)
    draw_text("Player 1: " + str(p1.score), font, "BLACK", screen, DISPLAYX / 1.25, DISPLAYY / 1.25)
    draw_text("Player 2: " + str(p2.score), font, "BLACK", screen, DISPLAYX / 1.25, DISPLAYY / 1.15)

def main():
    pygame.init()
    screen = pygame.display.set_mode([DISPLAYX, DISPLAYY])
    pygame.display.set_caption("Ticket to Ride")
    background = pygame.image.load("board.jpg")
    background = pygame.transform.scale(background, (DISPLAYX, DISPLAYY))
    screen.blit(background, (0, 0))
    while True:
        start_screen(screen, background)


if __name__ == '__main__':
    main()
