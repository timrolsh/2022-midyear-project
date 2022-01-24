"""THis class is redundant. We do not need a specific class to store one variable. The dictionary of colors has been
moved to Game, and can be accessed from there """


class Color:
    """
    Dictionary with all the possible colors and their RGB values for translation onto the field/board.
    """

    COLOR_DICT = {"WHITE": (255, 255, 255), "YELLOW": (252, 239, 108), "BLUE": (67, 147, 242), "BLACK": (69, 70, 74),
                  "RED": (201, 88, 80), "ORANGE": (214, 139, 84), "PINK": (201, 134, 175), "GREEN": (169, 195, 86),
                  "GRAY": (128, 128, 128)}
