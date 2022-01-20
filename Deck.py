from TrainCard import TrainCard
from Field import Field
from DestinationCard import DestinationCard
import random


class Deck:
    """
    Represents the main deck of cards in the Ticket to Ride board game
    """

    def __init__(self):
        """
        Initialize all the train cards and destination cards in a deck of cards. 12 cards of each color for train
        cards, and use the destination_list.txt file to import all the destination cards.
        """
        self.train_cards = []
        colors = ["PURPLE", "BLUE", "ORANGE", "WHITE", "GREEN", "YELLOW", "BLACK", "RED", "RAINBOW"]
        for color in colors:
            for i in range(12):
                self.train_cards.append(TrainCard(color))
        random.shuffle(self.train_cards)

        self.destination_cards = []

        destination_list_file = open('data/destination_list.txt', 'r')
        destination_list = destination_list_file.read()

        for line in destination_list.split('\n'):
            start, end, points = line.split(', ')
            points = int(points)
            destination_card = DestinationCard(Field.cities[start], Field.cities[end], points)
            self.destination_cards.append(destination_card)

        destination_list_file.close()

    def train_cards_length(self):
        """
        Method to find how many train cards left in the deck
        """
        return len(self.train_cards)

    def destination_cards_length(self):
        """
        Method to find how many remaining destination cards in the deck
        """
        return len(self.destination_cards)

    def discard_train_card(self, num_cards: int):
        """
        Return n train cards from the top of the deck
        """
        popped_cards = []
        for i in range(num_cards):
            popped_cards.append(self.train_cards.pop())
        return popped_cards

    def discard_destination_cards(self, num_cards: int):
        """
        Return n destination cards from the top of the deck
        """
        popped_cards = []
        for i in range(num_cards):
            popped_cards.append(self.destination_cards.pop())
        return popped_cards
