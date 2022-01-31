from RectButton import RectButton
import pygame

class CardButton(RectButton):
    def __init__(self, x, y, width, height, color, screen, train_card=None):
        super().__init__(x=x, y=y, width=width, height=height, color=color, screen=screen)
        self.train_card = train_card

    def draw_with_border(self):
        new_gray_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(self.screen, (125, 125, 125), new_gray_rect)
        new_rect = pygame.Rect(self.x+5, self.y+5, self.width-10, self.height-10)
        pygame.draw.rect(self.screen, self.color, new_rect)