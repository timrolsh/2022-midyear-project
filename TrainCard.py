from Card import Card


class TrainCard(Card):
    """
    Represents a single train card in the game. Cards can be one of eight colors, or Rainbow (wild card). Players can use
    cards to claim cars on the board.
    """

    def __init__(self, color: str):
        if color in ["PURPLE", "BLUE", "ORANGE", "WHITE", "GREEN", "YELLOW", "BLACK", "RED", "RAINBOW"]:
            self.color = color
        else:
            raise Exception("The color you selected for initialization is not valid")

    def is_match(self, color: str):
        if self.color == "RAINBOW" or color == "GRAY" or self.color == color:
            return True
        else:
            return False

    def __str__(self):
        return f"Card of color {self.color}"
