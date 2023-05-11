from typing import List


from usecases.player import player_walk, player_action
from entity.player import Player
from entity.table import Table


class GameEngine:

    def __init__(self, players: List[Player]):
        self.players: List[Player] = players
        self.table: Table = Table()
        self.winner = None

    def turn(self):
        for k, p in enumerate(self.players):
            player_walk(p, self.table)
            player_action(p, self.table)

            if p.is_broke():
                del self.players[k]

            if len(self.players) <= 1:
                self.winner = self.players[0]
                break

    def run(self) -> Player | None:
        turn: int = 0
        while self.winner is None:
            self.turn()
            if turn > 1000:
                break
            turn += 1

        if self.winner is None:
            return None

        return self.winner
