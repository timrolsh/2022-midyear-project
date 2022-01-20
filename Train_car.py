from Color import Color

class Train_car(): #to be continued bc i dont have time

    def __init__(self, color:str, size):
        if color in ["PURPLE", "BLUE", "ORANGE", "WHITE", "GREEN", "YELLOW", "BLACK", "RED", "RAINBOW"]:
            self.color = color
        else:
            raise Exception("The color you selected for initialization is not valid")

        size = 0

    def is_match(self, color: str):
        if self.color == "RAINBOW" or color == "GRAY" or self.color == color:
            return True
        else:
            return False
