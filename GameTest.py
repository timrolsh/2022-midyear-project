from Deck import Deck
from DestinationCard import DestinationCard
from Player import Player
from Field import Field

deck = Deck()
d_train = deck.discard_train_cards(100)
d_dest = deck.discard_destination_cards(3)

player = Player(d_train, d_dest)
player.destination_cards.append(DestinationCard(
    Field.cities["New York"], Field.cities["Boston"], 10))

player.claim_tracks(Field.cities["New York"].tracks[1])
print(player.union_find.city_indices["New York"])
print(player.union_find.city_indices["Boston"])
print(player.union_find.city_components)
print(player.union_find.is_connected(
    Field.cities["New York"], Field.cities["Boston"]))
player.claim_destination()
print(player.score)
