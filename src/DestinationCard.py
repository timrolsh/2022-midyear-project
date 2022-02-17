from src.Card import Card
from src.City import City


class DestinationCard(Card):
    """
    Represents a destination card in ticket to ride. Includes a starting city, ending city, and the number of points
    gained by completing the destination.
    """

    def __init__(self, start: City, end: City, points: int):
        super().__init__()
        self.start = start
        self.end = end
        self.points = points

    def __str__(self):
        return f"Card for {self.start.name} to {self.end.name}"
