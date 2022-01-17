from Card import Card
from City import City

class DestinationCard(Card):
    def __init__(self, start: City, end: City, points: int):
        self.start = start
        self.end = end
        self.points = points
