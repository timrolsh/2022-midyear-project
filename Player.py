from ScoreTable import ScoreTable
from Track import Track
from UnionFind import UnionFind


class Player:
    """
    Player class, with all the functions available to a player of the online game
    """

    def __init__(self, color: (int, int, int)):
        self.color = color
        self.train_cards = []
        self.destination_cards = []
        self.score = 0
        self.owned_tracks = []
        self.union_find = UnionFind()

    def claim_tracks(self, track: Track):
        """
        Claim a track using the train cards a player currently has. This only works if the cards are the same color
        as the track, and the player has enough cards.
        """
        if track.occupied_by!=None:
            raise Exception("Track is already occupied")

        num_matching_cards = 0
        cards_left = []
        for train_card in self.train_cards:
            if train_card.is_match(track.color):
                num_matching_cards += 1
            else:
                cards_left.append(train_card)
        if num_matching_cards >= track.length:
            self.owned_tracks.append(track)
            self.score += ScoreTable.SCORE_TABLE[track.length]
            self.union_find.connect_cities(track.city1, track.city2)
            track.occupied_by = self
        else:
            raise Exception("Player doesn't have enough train cards to claim this track")

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


    
