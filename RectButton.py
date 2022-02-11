from cmath import rect
from re import L
import Button
from Color import Color
import pygame


class RectButton():
    def __init__(self, x: int, y: int, width: int, height: int, color, font=None, text=None, screen=None,
                 text_color=None, double_line=None, text2=None, image=None):
        if type(color) == str:
            self.color = Color.COLOR_DICT[color]
        else:
            self.color = color
        self.rect = pygame.Rect((x, y), (width, height))
        # self.rect = image.get_rect()
        if font != None:
            self.text_surface = font.render(text, True, text_color)
            self.text_rect = self.text_surface.get_rect(
                center=self.rect.center)

        self.screen = screen
        self.is_clicked = False
        self.double_line = double_line
        self.text2 = text2
        self.font = font
        self.text_color = text_color
        self.image = image
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self):
        if self.image != None:
            self.screen.blit(self.image, self.rect)
        else:
            pygame.draw.rect(self.screen, self.color, self.rect)

        if self.font != None:
            self.screen.blit(self.text_surface, self.text_rect)

        if (self.double_line):
            ts_2 = self.font.render(self.text2, True, self.text_color)
            tr_2 = ts_2.get_rect(
                center=(self.rect.centerx, self.rect.centery + 10))
            self.screen.blit(ts_2, tr_2)

    def point_in_rect(self, point):
        return self.rect.collidepoint(point)

    def click(self):
        self.is_clicked = True
