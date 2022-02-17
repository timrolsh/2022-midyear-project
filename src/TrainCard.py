from src.Card import Card


class TrainCard(Card):
    """
    Represents a single train card in the game. Cards can be one of eight colors, or Rainbow (wild card). Players can
    use cards to claim cars on the board.
    """

    def __init__(self, color: str):
        super().__init__()
        self.color = color

    def is_match(self, color: str):
        return self.color == "RAINBOW" or color == "GRAY" or self.color == color

    def __str__(self):
        return f"Card of color {self.color}"
