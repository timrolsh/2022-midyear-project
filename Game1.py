from time import time
import pygame

from Deck import Deck

pygame.init()
# load original image for pygame
original_image = pygame.image.load("images/board.jpg")
start_background = pygame.image.load("images/startscreen.png")

FONT = "fonts/titlefont.ttf"
BUTTON_FONT = "fonts/buttonfont.ttf"
deck = Deck()
players = []
COLORS = {"WHITE": (255, 255, 255), "YELLOW": (252, 239, 108), "BLUE": (67, 147, 242), "BLACK": (69, 70, 74),
          "RED": (201, 88, 80), "ORANGE": (214, 139, 84), "PINK": (201, 134, 175), "GREEN": (169, 195, 86),
          "GRAY": (128, 128, 128)}
SCORE_TABLE = {1: 1, 2: 2, 3: 4, 4: 7, 5: 10, 6: 15}

"""THESE OPTIONS ARE CUSTOMIZABLE BY THE USER, GAME WILL PROPERLY SCALE TO THE DIMENSIONS SPECIFIED"""
FPS = 30
DISPLAY_WIDTH = 1280
DISPLAY_HEIGHT = 720

game_display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
deck = Deck()
