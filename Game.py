import os

import pygame

from Button import Button
from CardButton import CardButton
from Color import Color
from Deck import Deck
from Field import Field
from Human import Human
from RectButton import RectButton
from UnionFind import UnionFind

# from Computer import Computer

# hide pygame welcome message
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

# define essential parameters for the game
board_image = pygame.image.load("images/board.jpg")
start_screen_image = pygame.image.load("images/startscreen.png")

CITY_COLOR = (219, 152, 99)
CITY_RADIUS = 10
FONT = "fonts/titlefont.ttf"
BUTTON_FONT = "fonts/buttonfont.ttf"
deck = Deck()

# define original image dimensions
ORIGINAL_WIDTH = board_image.get_width()
ORIGINAL_HEIGHT = board_image.get_height()

"""THESE OPTIONS ARE CUSTOMIZABLE BY THE USER, GAME WILL PROPERLY SCALE TO THE DIMENSIONS SPECIFIED"""
FPS = 15
DISPLAY_WIDTH = 955
DISPLAY_HEIGHT = 636

"""Please define the players you want to play by calling the constructor for either human or player class, 
and then specifying a color from the colors dictionary provided of sample colors. Or, you can make your own color! 
Colors are represented by tuple values of three RGB values. """
PLAYERS = [Human(Color.COLOR_DICT["BLUE"]), Human(Color.COLOR_DICT["GREEN"])]


def scale(point):
    scale_factor = DISPLAY_WIDTH / ORIGINAL_WIDTH
    if type(point) == int:
        return scale_factor * point
    else:
        return tuple(point[i] * scale_factor for i in range(len(point)))


def draw_train_cars(screen):
    for track in Field.tracks_list:
        if (track.occupied_by != None):
            for train_car in track.train_cars:
                pygame.draw.polygon(screen, track.occupied_by.color, (
                    scale(train_car.point1), scale(train_car.point2), scale(train_car.point3), scale(train_car.point4)))


# pygame main loop
def game_loop(screen, debug, background, rules):
    # this function puts 4 traincards into the players
    global track
    running = True
    player1_train_cards = deck.discard_train_cards(4)
    player2_train_cards = deck.discard_train_cards(4)

    player1_destination_cards = deck.discard_destination_cards(3)
    player2_destination_cards = deck.discard_destination_cards(3)

    # setting the colors to red/blue manually for now
    player1 = PLAYERS[0]
    player2 = PLAYERS[1]
    PLAYERS[0].color = "BLUE"
    PLAYERS[1].color = "GREEN"

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

    wooden_button = pygame.image.load("images/woodenbutton.png")
    wooden_button_hover = pygame.image.load("images/woodenbuttonhover.png")

    wooden_button = pygame.transform.scale(wooden_button, (int(DISPLAY_WIDTH / 9),
                                                           int(DISPLAY_HEIGHT / 15)))

    wooden_button_hover = pygame.transform.scale(wooden_button_hover,
                                                 (int(DISPLAY_WIDTH / 9),
                                                  int(DISPLAY_HEIGHT / 15)))

    train_card_button = RectButton(int(DISPLAY_WIDTH / 10),
                                   int(DISPLAY_HEIGHT / 1.175),
                                   int(DISPLAY_WIDTH / 9),
                                   int(DISPLAY_HEIGHT / 15),
                                   "RED",
                                   pygame.font.Font(BUTTON_FONT, 13), "Draw", screen, "BLACK", True, "Train Cards",
                                   wooden_button)

    destination_card_button = RectButton(int(DISPLAY_WIDTH / 4),
                                         int(DISPLAY_HEIGHT / 1.175),
                                         int(DISPLAY_WIDTH / 9),
                                         int(DISPLAY_HEIGHT / 15),
                                         "RED",
                                         pygame.font.Font(BUTTON_FONT, 13), "Destination", screen, "BLACK", True,
                                         "Cards", wooden_button)

    help_button_image = pygame.image.load("images/helpbutton.png")
    help_button_hover_image = pygame.image.load("images/helpbuttonhover.png")

    help_button = RectButton(50, 40, 42, 40, None, None, None, screen, None, None, None, help_button_image)

    train_card_button.draw()
    destination_card_button.draw()
    help_button.draw()
    color = player1.color

    final_turn = False
    final_started_by = None

    while running:

        if final_turn==True:
            # give the player's another turn?
            if (final_started_by == current_turn):
                break

        turn_complete = False

        # check button hover
        if train_card_button.rect.collidepoint(pygame.mouse.get_pos()):
            train_card_button.image = wooden_button_hover
        else:
            train_card_button.image = wooden_button

        if destination_card_button.rect.collidepoint(pygame.mouse.get_pos()):
            destination_card_button.image = wooden_button_hover
        else:
            destination_card_button.image = wooden_button

        if help_button.rect.collidepoint(pygame.mouse.get_pos()):
            help_button.image = help_button_hover_image
        else:
            help_button.image = help_button_image

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                current_pos = pygame.mouse.get_pos()

                is_clicked = False
                for track in Field.tracks_list:
                    if track.occupied_by != None:
                        continue
                    for train_car in track.train_cars:
                        if train_car.check_in_rectangle(
                                tuple(i * (ORIGINAL_WIDTH / DISPLAY_WIDTH) for i in current_pos)):
                            is_clicked = True
                            break
                    if is_clicked:
                        break
                if is_clicked:
                    success = buy_track(PLAYERS[current_turn], track)
                    if (success):
                        turn_complete = True

                if train_card_button.rect.collidepoint(current_pos):
                    train_card_button.is_clicked = True
                if destination_card_button.rect.collidepoint(current_pos):
                    destination_card_button.is_clicked = True
                if help_button.rect.collidepoint(current_pos):
                    help_button.is_clicked = True

                if train_card_button.is_clicked:
                    train_card_button.is_clicked = False
                    is_change_turn = draw_train_card_screen(screen, current_turn)
                    if (is_change_turn == True):
                        turn_complete = True

                if destination_card_button.is_clicked:
                    destination_card_button.is_clicked = False
                    has_been_drawn = draw_destination_card_screen(screen, current_turn)
                    if has_been_drawn:
                        turn_complete = True
                if help_button.is_clicked:
                    help_button.is_clicked = False
                    help_screen(screen, rules)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
                    player_card_tab(screen, background, current_turn)
                elif event.key == pygame.K_h:
                    help_screen(screen, rules)
                elif event.key == pygame.K_t:
                    is_change_turn = draw_train_card_screen(screen, current_turn)
                    if (is_change_turn == True):
                        turn_complete = True
                elif event.key == pygame.K_d:
                    has_been_drawn = draw_destination_card_screen(screen, current_turn)
                    if has_been_drawn:
                        turn_complete = True        

        # Change turns
        if (turn_complete):
            if PLAYERS[current_turn].trains<=2:
                final_turn = True
                if final_started_by is None:
                    final_started_by = current_turn
            if current_turn == 0:
                current_turn = 1
            else:
                current_turn = 0
            color = PLAYERS[current_turn].color
            if (debug):
                print("Player: " + str(current_turn))

            # to be completed
            # player_prompt(PLAYERS[current_turn], screen, background, current_turn)

        screen.blit(background, (0, 0))
        draw_game_area(screen)
        train_card_button.draw()
        destination_card_button.draw()
        help_button.draw()
        display_scores(screen, current_turn)
        draw_train_cars(screen)

        text_font = pygame.font.Font(FONT, 20)

        # temporary, replace with buttons in the future
        draw_text("'TAB' - train cards/claim track", text_font, "RED", screen, DISPLAY_WIDTH / 1.4, 50)
        # draw_text("'H' - Help", text_font, "RED", screen, DISPLAY_WIDTH / 1.62, 75)
        pygame.display.update()

    winner = calculate_end_scores()
    game_end_screen(winner, screen, background)

    pygame.quit()


def game_end_screen(winner, screen, background):
    screen.fill((234, 221, 202))

    confetti_image = pygame.image.load("images/confetti_image.jpg")
    confetti_image = pygame.transform.scale(confetti_image, (int(DISPLAY_WIDTH)/1.1, int(DISPLAY_HEIGHT)+10))
    confetti_image.set_alpha(128)
    screen.blit(confetti_image, (DISPLAY_WIDTH/2-confetti_image.get_width()/2, DISPLAY_HEIGHT/2-confetti_image.get_height()/2))

    font = pygame.font.Font(FONT, 60)
    play_font = pygame.font.Font(FONT, 30)
    if type(winner)==list:
        text = "IT IS A TIE"
    else:
        text = f"Winner: {winner.color}"
    draw_text(text, font, "BLACK", screen, (DISPLAY_WIDTH / 2), (DISPLAY_HEIGHT / 2))

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_p:
                    game_loop(screen, False, background)

        pygame.display.update()

        pygame.time.Clock().tick(FPS)


def buy_track(player, track):
    try:
        if track.occupied_by != None:
            print(f"Track has already been claimed by player {track.occupied_by.color}")
            return False
        elif player.trains<track.length:
            print(f"Player doesn't have enough train cars to by this track")
        else:
            player.claim_tracks(track)
            return True
    except Exception as e:
        print("Player doesn't have enough train cards to claim that track.")
        return False


def help_screen(screen, rules):
    screen.fill(Color.COLOR_DICT.get("WHITE"))
    title_font = pygame.font.Font(FONT, 60)
    text_font = pygame.font.Font(FONT, 20)

    # draw_text("Ticket to Ride", font, "BLACK", screen, (DISPLAY_WIDTH / 2), (DISPLAY_HEIGHT / 2))

    # draw_text("Rules", title_font, "RED", screen, (DISPLAY_WIDTH / 2), 100)
    screen.blit(rules, (0, 0))
    draw_text("Press 'ESC' to exit this tab", text_font, "RED", screen, (DISPLAY_WIDTH / 1.2), (DISPLAY_HEIGHT / 20))
    pygame.display.update()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    running = False

        pygame.time.Clock().tick(FPS)

        pygame.display.update()


def draw_rectangles(screen, train_cards, current_x, current_y, rect_width, rect_height):
    x_increment = rect_width + DISPLAY_WIDTH * 0.032
    y_increment = rect_height + DISPLAY_HEIGHT * 0.021

    rectangles = []

    for train_card in train_cards:

        current_x += x_increment
        if (DISPLAY_WIDTH - current_x <= x_increment):
            current_y += y_increment
            current_x = x_increment
        if (train_card.color == "RAINBOW"):
            color = (180, 180, 180)
        else:
            color = Color.COLOR_DICT[train_card.color]
        card_button = CardButton(x=current_x, y=current_y, width=rect_width, height=rect_height, color=color,
                                 screen=screen, train_card=train_card)
        if card_button.train_card.is_clicked:
            card_button.draw_with_border()
        else:
            card_button.draw()
        rectangles.append(card_button)

    return rectangles


# returns true if a player successfully selects their train cards
def player_card_tab(screen, background, current_player):
    player = PLAYERS[current_player]

    font = pygame.font.Font(FONT, 60)

    screen.fill((234, 221, 202))

    pygame.display.update()

    rect_width = DISPLAY_WIDTH * 0.06
    rect_height = DISPLAY_HEIGHT * 0.19

    current_x = 0
    current_y = DISPLAY_HEIGHT * 0.016

    rectangles = draw_rectangles(screen, player.train_cards, current_x, current_y, rect_width, rect_height)

    draw_text("Player " + str(current_player + 1) + " Cards", font, "BLACK", screen, (DISPLAY_WIDTH / 2),
              (DISPLAY_HEIGHT / 2))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE or event.key == pygame.K_m:
                    running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                current_pos = pygame.mouse.get_pos()
                for card_button in rectangles:
                    if (card_button.point_in_rect(current_pos)):
                        if card_button.train_card.is_clicked:
                            card_button.train_card.is_clicked = False
                            player.clicked_cards.remove(card_button.train_card)
                            card_button.draw()
                            if len(player.clicked_cards)==0:
                                player.current_card_color = None
                        else:
                            if card_button.train_card.color!="RAINBOW" and player.current_card_color is None:
                                player.current_card_color = card_button.train_card.color
                            if card_button.train_card.color==player.current_card_color or card_button.train_card.color=="RAINBOW":
                                card_button.train_card.is_clicked = True
                                player.clicked_cards.add(card_button.train_card)
                                card_button.draw_with_border()

        pygame.display.update()
        pygame.time.Clock().tick(FPS)


def draw_train_card_screen(screen, current_turn):
    screen.fill((234, 221, 202))
    player = PLAYERS[current_turn]

    font = pygame.font.Font(FONT, 60)
    text_font = pygame.font.Font(FONT, 25)

    draw_text("Player " + str(current_turn + 1), font, "BLACK", screen, (DISPLAY_WIDTH / 2), (DISPLAY_HEIGHT / 2))
    draw_text("Draw Train Cards", font, "BLACK", screen, (DISPLAY_WIDTH / 2), (DISPLAY_HEIGHT / 1.5))
    draw_text("Press 'ESC' to exit this tab", text_font, "RED", screen, (DISPLAY_WIDTH / 2), (DISPLAY_HEIGHT / 1.3))
    pygame.display.update()

    train_cards = deck.discard_train_cards(7)
    train_cards[5].face_down = True
    train_cards[6].face_down = True

    rect_width = DISPLAY_WIDTH * 0.06
    rect_height = DISPLAY_HEIGHT * 0.19

    current_x = 0
    current_y = DISPLAY_HEIGHT * 0.016

    rectangles = draw_rectangles(screen, train_cards, current_x, current_y, rect_width, rect_height)

    wooden_button = pygame.image.load("images/woodenbutton.png")
    wooden_button = pygame.transform.scale(wooden_button, (int(DISPLAY_WIDTH / 9), int(DISPLAY_HEIGHT / 15)))
    wooden_button_hover = pygame.image.load("images/woodenbuttonhover.png")
    wooden_button_hover = pygame.transform.scale(wooden_button_hover,
                                                 (int(DISPLAY_WIDTH / 9), int(DISPLAY_HEIGHT / 15)))

    submit_button = RectButton(int(DISPLAY_WIDTH / 10),
                               int(DISPLAY_HEIGHT / 1.175),
                               int(DISPLAY_WIDTH / 9),
                               int(DISPLAY_HEIGHT / 15),
                               "RED",
                               pygame.font.Font(BUTTON_FONT, 13), "Submit", screen, "BLACK", True, "Selection",
                               wooden_button)

    submit_button.draw()
    num_cards_selected = 0

    running = True
    while running:

        if submit_button.rect.collidepoint(pygame.mouse.get_pos()):
            submit_button.image = wooden_button_hover
        else:
            submit_button.image = wooden_button

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE or event.key == pygame.K_m:
                    for card in train_cards:
                        card.is_clicked = False
                        card.face_down = False
                    deck.add_train_cards_back(train_cards, top_five=True)

                    running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:

                current_pos = pygame.mouse.get_pos()
                for card_button in rectangles:
                    if card_button.train_card.face_down:
                        color = "BROWN"
                    else:
                        color = card_button.train_card.color
                    if (card_button.point_in_rect(current_pos)):
                        if card_button.train_card.is_clicked:
                            if color == "RAINBOW":
                                num_cards_selected -= 2
                            else:
                                num_cards_selected -= 1
                            card_button.train_card.is_clicked = False
                            card_button.draw()
                        elif num_cards_selected == 0 or (num_cards_selected == 1 and color != "RAINBOW"):
                            card_button.train_card.is_clicked = True
                            card_button.draw_with_border()
                            if (not card_button.train_card.face_down) and card_button.train_card.color == "RAINBOW":
                                num_cards_selected += 2
                            else:
                                num_cards_selected += 1

                if submit_button.rect.collidepoint(current_pos):
                    not_selected = []
                    for card in train_cards:
                        card.face_down = False
                        if card.is_clicked:
                            card.is_clicked = False
                            player.train_cards.append(card)
                        else:
                            not_selected.append(card)
                    deck.add_train_cards_back(not_selected, top_five=True)
                    running = False
                    if (len(not_selected) != len(train_cards)):
                        return True

        submit_button.draw()
        pygame.time.Clock().tick(FPS)

        pygame.display.update()


def draw_destination_card_screen(screen, current_turn):
    screen.fill(Color.COLOR_DICT.get("WHITE"))
    player = PLAYERS[current_turn]

    button_font = pygame.font.Font(BUTTON_FONT, 15)
    font = pygame.font.Font(FONT, 60)
    text_font = pygame.font.Font(FONT, 25)

    def draw_title():
        draw_text("Player " + str(current_turn + 1), font, "BLACK", screen, (DISPLAY_WIDTH / 2), (DISPLAY_HEIGHT / 10))
        draw_text("Draw Destination Cards", font, "BLACK", screen, (DISPLAY_WIDTH / 2), (DISPLAY_HEIGHT / 5))
        

    draw_title()
    draw_text("Press 'ESC' to exit this tab", text_font, "RED", screen, (DISPLAY_WIDTH / 2),
                  (DISPLAY_HEIGHT / 3.75))
    pygame.display.update()

    card_ranges = []

    def draw_table(x, y, width, height, size):

        new_ranges = []
        current_card = 0
        for y_val in range(y, y + size[1], height):
            row_rect = 1
            for x_val in range(x, x + size[0], width):
                if row_rect==1:
                    text = player.destination_cards[current_card].start.name
                elif row_rect==2:
                    text = player.destination_cards[current_card].end.name
                elif row_rect==3:
                    text = f"{player.destination_cards[current_card].points} pts"
                text_surface = button_font.render(text, True, Color.COLOR_DICT["BLACK"])
                table_rect = pygame.draw.rect(screen, Color.COLOR_DICT["BLACK"], [x_val, y_val, width, height], 1)
                text_rect = text_surface.get_rect(center=table_rect.center)
                screen.blit(text_surface, text_rect)
                row_rect+=1
            
            new_ranges.append([player.destination_cards[current_card], x, x + width, y_val, y_val + height])
            new_ranges.append([player.destination_cards[current_card], x, x + width * 2, y_val, y_val + height])
            new_ranges.append([player.destination_cards[current_card], x, x + width * 3, y_val, y_val + height])
            current_card += 1
        return new_ranges

    box_width = int(DISPLAY_WIDTH / 10)
    box_height = int(DISPLAY_HEIGHT / 13)
    new_ranges = draw_table(int(DISPLAY_WIDTH / 2.8), int(DISPLAY_HEIGHT / 3), box_width, box_height,
                            [box_width * 3, box_height * len(player.destination_cards)])
    card_ranges = new_ranges
    pygame.display.update()

    wooden_button = pygame.image.load("images/woodenbutton.png")
    wooden_button = pygame.transform.scale(wooden_button, (int(DISPLAY_WIDTH / 9), int(DISPLAY_HEIGHT / 15)))
    wooden_button_hover = pygame.image.load("images/woodenbuttonhover.png")
    wooden_button_hover = pygame.transform.scale(wooden_button_hover,
                                                 (int(DISPLAY_WIDTH / 9), int(DISPLAY_HEIGHT / 15)))
    destination_card_button = RectButton(int(DISPLAY_WIDTH / 2.25),
                                         int(DISPLAY_HEIGHT / 1.175),
                                         int(DISPLAY_WIDTH / 9),
                                         int(DISPLAY_HEIGHT / 15),
                                         "RED",
                                         pygame.font.Font(BUTTON_FONT, 13), "Draw", screen, "BLACK", True,
                                         " Destination Card", wooden_button)

    destination_card_button.draw()

    card_drawn = False
    cards_removed = 0

    running = True

    while running:

        if destination_card_button.rect.collidepoint(pygame.mouse.get_pos()):
            destination_card_button.image = wooden_button_hover
        else:
            destination_card_button.image = wooden_button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE or event.key == pygame.K_m:
                    for j in range(-1, -4, -1):
                        if (len(player.destination_cards) < abs(j)):
                            break
                        player.destination_cards[j].is_clicked = False
                    return card_drawn

            elif event.type == pygame.MOUSEBUTTONDOWN:
                current_pos = pygame.mouse.get_pos()
                if (cards_removed < 2):
                    for card_range in range(len(card_ranges)):
                        r = card_ranges[card_range]
                        x = current_pos[0]
                        y = current_pos[1]
                        if x >= r[1] and x <= r[2] and y >= r[3] and y <= r[4]:
                            card_index = player.destination_cards.index(r[0])

                            # to do, inform the players that they can remove destination cards they just selected.
                            if player.destination_cards[card_index].is_clicked == True:
                                player.destination_cards.pop(card_index)
                                cards_removed += 1
                                screen.fill(Color.COLOR_DICT.get("WHITE"))
                                draw_title()
                                draw_text("Press 'ESC' to exit this tab", text_font, "RED", screen, (DISPLAY_WIDTH / 2),
                  (DISPLAY_HEIGHT / 3.75))
                            break
                elif (cards_removed == 2):
                    screen.fill(Color.COLOR_DICT.get("WHITE"))
                    draw_title()
                    draw_text("(!) You cannot remove more than 2 destination cards", text_font, "RED", screen, (DISPLAY_WIDTH / 2),
                    (DISPLAY_HEIGHT / 3.75))
                
                    
                if (not card_drawn):

                    if destination_card_button.rect.collidepoint(current_pos):
                        new_destination_cards = deck.discard_destination_cards(3)
                        for card in new_destination_cards:
                            card.is_clicked = True
                        player.destination_cards.extend(new_destination_cards)
                        card_drawn = True
                        screen.fill(Color.COLOR_DICT.get("WHITE"))
                        draw_title()
                        draw_text("Press 'ESC' to exit this tab", text_font, "RED", screen, (DISPLAY_WIDTH / 2), (DISPLAY_HEIGHT / 3.75))

        new_ranges = draw_table(int(DISPLAY_WIDTH / 2.8), int(DISPLAY_HEIGHT / 3), box_width, box_height,
                                [box_width * 3, box_height * len(player.destination_cards)])
        card_ranges = new_ranges
        pygame.time.Clock().tick(FPS)

        # temporary, replace with buttons in the future
        destination_card_button.draw()
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
            city_button = Button(int(circle_x),
                                 int(circle_y),
                                 20, 20)

            city_buttons.append(city_button)
    first_creation_pass = False


def player_prompt(player, screen, background, current_turn):
    # Draw three buttons for options
    font = pygame.font.Font(FONT, 60)

    draw_game_area(screen)

    draw_text("Player " + str(current_turn + 1) + " choose a move", font, "BLACK", screen, (DISPLAY_WIDTH / 2),
              (DISPLAY_HEIGHT / 2))

    pygame.display.update()

    # Create buttons later

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
                    # draw?
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


def display_scores(screen, current_turn):
    font = pygame.font.Font(FONT, 30)

    current_player = PLAYERS[current_turn]

    draw_text("Player " + str((current_turn + 1)) + ": " + str(current_player.score) + " pts", font,
              current_player.color, screen, DISPLAY_WIDTH / 1.75, DISPLAY_HEIGHT / 1.1)


def calculate_end_scores():
    """
    1. Add or subtract the score in a destination card depending on whether it was completed by the player
    2. The player who has the longest continuous path gets 10 extra points with a bonus card
    3. Player with most points wins, and for tie breakers player with most completed destinations wins
    """

    # 3
    winner = None
    tied_players = []
    for player in PLAYERS:
        if winner is None:
            winner = player
        elif player.score > winner.score:
            winner = player
            tied_players.clear()
        elif player.score == winner.score:
            tied_players.append(player)
            tied_players.append(winner)

    # Check if there is a tie
    if len(tied_players)==0:
        return winner
    else:
        return tied_players


def main():
    # initialize game
    pygame.init()
    screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    # start screen menu
    screen.blit(pygame.transform.scale(start_screen_image, (DISPLAY_WIDTH, DISPLAY_HEIGHT)), (0, 0))
    RectButton(int(DISPLAY_WIDTH / 2.675),
               int(DISPLAY_HEIGHT / 1.07),
               int(DISPLAY_WIDTH / 4),
               int(DISPLAY_HEIGHT / 14),
               "RED",
               pygame.font.Font(BUTTON_FONT, 36), "Press P to Play", screen, "BLACK", True).draw()
    pygame.display.update()
    temp = True
    rules = pygame.image.load("images/Rules.PNG")
    while temp:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    temp = False
                    break
                # if event.key == pygame.K_h:
                #     help_screen(screen, rules)
        
    pygame.display.update()
    game_loop(screen, False, pygame.transform.scale(board_image, (DISPLAY_WIDTH, DISPLAY_HEIGHT)),
              rules)


# TODO display player scores in the game, fix the fonts so that they are more readable, display train cards with
#  their images not their colors


if __name__ == '__main__':
    main()
