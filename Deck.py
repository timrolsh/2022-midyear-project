from TrainCard import TrainCard
from Field import Field
from DestinationCard import DestinationCard
import random

class Deck:
    def __init__(self):
        self.train_cards = []
        colors = ["Purple", "Blue", "Orange", "White", "Green", "Yellow", "Black", "Red", "Rainbow"]
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
        return len(self.train_cards)

    def destination_cards_length(self):
        return len(self.destination_cards)

    def discard_train_card(self, num_cards: int):
        popped_cards = []
        for i in range(num_cards):
            popped_cards.append(self.train_cards.pop())
        return popped_cards
    
    def discard_destination_cards(self, num_cards: int):
        popped_cards = []
        for i in range(num_cards):
            popped_cards.append(self.destination_cards.pop())
        return popped_cards