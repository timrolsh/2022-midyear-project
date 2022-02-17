import pygame


class Color:
    """
    Dictionary with all the possible colors and their RGB values for translation onto the field/board.
    """

    COLOR_DICT = {
        "WHITE": (255, 255, 255),
        "YELLOW": (252, 239, 108),
        "BLUE": (67, 147, 242),
        "BLACK": (69, 70, 74),
        "RED": (201, 88, 80),
        "ORANGE": (214, 139, 84),
        "PINK": (201, 134, 175),
        "GREEN": (65, 163, 23),
        "GRAY": (128, 128, 128),
        "PURPLE": (150, 0, 150)
    }
    
    # "GREEN": (169, 195, 86),

    """Dictionary with all the possible colors and their RGB values for translation onto the field/board. Will be 
    used to draw cards in the game """
    COLORS_IMAGES = {
        "BLACK": pygame.image.load('images/black_traincard.png'),
        "BLUE": pygame.image.load('images/blue_traincard.png'),
        "GREEN": pygame.image.load('images/green_traincard.png'),
        "ORANGE": pygame.image.load('images/orange_traincard.png'),
        "PINK": pygame.image.load('images/pink_traincard.png'),
        "RAINBOW": pygame.image.load('images/rainbow_traincard.png'),
        "RED": pygame.image.load('images/red_traincard.png'),
        "WHITE": pygame.image.load('images/white_traincard.png'),
        "YELLOW": pygame.image.load('images/yellow_traincard.png'),
        "FACEDOWN": pygame.image.load('images/facedown_traincard.png')
    }
