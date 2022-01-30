import string
from City import City
from pygame import Rect
import Color
class Button:
    def __init__(self, x: int, y: int, width: int, height: int):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        

    def __str__(self) -> str:
        return f"Button at  position x: {self.x} and y: {self.y} with width of {self.width} and height {self.height}"
