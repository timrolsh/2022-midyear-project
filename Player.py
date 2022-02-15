from Track import Track
from UnionFind import UnionFind


class Player:
    """
    Player class, with all the functions available to a player of the online game
    """
    # static map score table to be used by players when incrementing their points
    SCORE_TABLE = {1: 1, 2: 2, 3: 4, 4: 7, 5: 10, 6: 15}

    def __init__(self, color: (int, int, int)):
        self.color = color
        self.train_cards = []
        self.clicked_cards = set()
        self.destination_cards = []
        self.score = 0
        self.owned_tracks = []
        self.union_find = UnionFind()
        self.current_card_color = None

    def claim_tracks(self, track: Track):
        """
        Claim a track using the train cards a player currently has. This only works if the cards are the same color
        as the track, and the player has enough cards.
        """
        if track.occupied_by != None:
            raise Exception("Track is already occupied")

        num_matching_cards = 0
        cards_left = []
        is_enough_cards = False
        for train_card in self.train_cards:

            if is_enough_cards:
                cards_left.append(train_card)
                continue

            if train_card.is_match(track.color) and train_card.is_clicked:
                num_matching_cards += 1
                if num_matching_cards >= track.length:
                    is_enough_cards = True
            else:
                cards_left.append(train_card)

        if is_enough_cards:
            self.owned_tracks.append(track)
            self.score += Player.SCORE_TABLE[track.length]
            self.union_find.connect_cities(track.city1, track.city2)
            track.occupied_by = self
            self.train_cards = cards_left
        else:
            raise Exception(
                "Player doesn't have enough train cards to claim this track")

    def claim_destination(self):
        """
        Claim a destination card and add points to the user's score. Uses the UnionFind algorithm to check if two
        cities are connected.
        """
        for d in range(len(self.destination_cards)):
            destination_card = self.destination_cards[d]
            if self.union_find.is_connected(destination_card.start, destination_card.end):
                self.destination_cards.pop(d)
                self.score += destination_card.points
