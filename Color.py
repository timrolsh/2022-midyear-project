""" this class contains static variables
that appear in Ticket To Ride. The colors
are not all "exact" as they are on the
color wheel. For example, the color green
would be (0,255,0), but Ticket To Ride
uses a different shade of green.
"""


class Color:
    """
    Dictionary with all the possible colors and their RGB values for translation onto the field/board. 
    """

    COLOR_DICT = {"WHITE": (255, 255, 255), "YELLOW": (252, 239, 108), "BLUE": (67, 147, 242), "BLACK": (69, 70, 74),
                  "RED": (201, 88, 80), "ORANGE": (214, 139, 84), "PINK": (201, 134, 175), "GREEN": (169, 195, 86),
                  "GRAY": (128, 128, 128)}
