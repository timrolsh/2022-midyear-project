import Button
from Color import Color
import pygame
class RectButton():
    def __init__(self, x: int, y: int, width: int, height: int, color: str, font, text, screen, text_color, double_line, text2):
    
        self.color = Color.COLOR_DICT.get(color)
        self.rect = pygame.Rect((x, y), (width, height))
        self.text_surface = font.render(text, True, text_color)
        self.text_rect = self.text_surface.get_rect(center = self.rect.center)
        self.screen = screen
        self.is_clicked = False
        self.double_line = double_line
        self.text2 = text2
        self.font = font
        self.text_color = text_color
    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        self.screen.blit(self.text_surface, self.text_rect)

        if (self.double_line):
            ts_2 = self.font.render(self.text2, True, self.text_color)
            tr_2 = ts_2.get_rect(center = (self.rect.centerx, self.rect.centery+10))
            self.screen.blit(ts_2, tr_2)
    def click(self):
        self.is_clicked = True
        
                
            
            