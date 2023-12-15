import config

from detector import predict_uno_cards
from player import Player
from uno_classes import UnoCard

"""
This is the class to control the game. It is responsible for a game flow.
How to use Game:
1. Create an initial unocard
2. Create an instance
3. Call run_game
"""
class Game:

    def __init__(self, *args: [Player]):
        if len(args) < 2: raise Exception("You need at least two players!")
        self.players = args
        self.activePlayer = -1
        self.activeCard = None

    def get_next_player(self) -> Player:
        if self.activePlayer == len(self.players) - 1:
            self.activePlayer = 0
        else:
            self.activePlayer += 1
        return self.players[self.activePlayer]
    
    def is_active_player_winning(self) -> bool:
        if self.activePlayer == -1: return False

        player = self.players[self.activePlayer]

        return player.get_card_count() == 0

    """
    This method analyze the main deck by card detection.
    Detect the active card.
    """
    def update_game_stats(self):
        card, _ = predict_uno_cards(config.stack_camera)[0]
        self.activeCard = card
        print(f'Aktuelle Karte: {str(self.activeCard)}')

    """
    This is the main method to call.
    """
    def run_game(self):
        self.update_game_stats()
        while not self.is_active_player_winning():
            player = self.get_next_player()
            print(f'Nächster Spieler ist {player}')
            player.handle_turn(self.activeCard)
            self.update_game_stats()
        print(f"Congrats. {player} won the game.")

        # Cleanup
        for player in self.players:
            player.cleanup()