import random

from src.DestinationCard import DestinationCard
from src.Field import Field
from src.TrainCard import TrainCard

"""
Represents the main deck of cards in the Ticket to Ride board game
"""


class Deck:
    """
    Initialize all the train cards and destination cards in a deck of cards. 12 cards of each color for train cards,
    and use the destination_list.txt file to import all the destination cards.
    """

    def __init__(self):

        self.train_cards = []
        colors = ["PINK", "BLUE", "ORANGE", "WHITE",
                  "GREEN", "YELLOW", "BLACK", "RED", "RAINBOW"]
        for color in colors:
            for i in range(12):
                self.train_cards.append(TrainCard(color))
        random.shuffle(self.train_cards)

        self.destination_cards = []
        destination_list_txt = open('data/destination_list.txt', 'r')

        for line in destination_list_txt:
            start, end, points = line.split(', ')
            destination_card = DestinationCard(
                Field.cities[start], Field.cities[end], int(points))
            self.destination_cards.append(destination_card)
        random.shuffle(self.destination_cards)

        destination_list_txt.close()

    """
    Method to find how many train cards left in the deck
    """

    def remaining_train_cards(self):
        return len(self.train_cards)

    """
    Method to find how many remaining destination cards in the deck
    """

    def remaining_destination_cards(self):
        return len(self.destination_cards)

    """
    Return n train cards from the top of the deck
    """

    def discard_train_cards(self, num_cards: int):
        popped_cards = []
        for i in range(num_cards):
            if len(self.train_cards) != 0:
                popped_cards.append(self.train_cards.pop())
        return popped_cards

    """
    Return n destination cards from the top of the deck
    """

    def discard_destination_cards(self, num_cards: int):
        popped_cards = []
        for i in range(num_cards):
            if len(self.destination_cards) != 0:
                popped_cards.append(self.destination_cards.pop())
        return popped_cards

    """
    Takes a list of cards and throws them back into the deck of train cards. Then, shuffles the deck again so that 
    cards don't pile up 
    """

    def add_train_cards_back(self, cards_coming_back: [], top_five=False):
        for i in range(len(cards_coming_back) - 1, -1, -1):
            self.train_cards.append(cards_coming_back[i])
        if not top_five:
            random.shuffle(self.train_cards)
