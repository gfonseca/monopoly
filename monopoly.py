#! /usr/bin/env python3

from typing import List

from usecases.player import bootstrap_players, player_walk, player_action
from entity.player import Player
from entity.table import Table
from usecases.table import expropriate_player
from utils import add_stats, print_stats


GAMES_TOTAL = 300
STATS = {}


class GameEngine:

    def __init__(self, players: List[Player]):
        self.players: List[Player] = players
        self.table: Table = Table()
        self.winner: str = None
        self.turns: int = 0

    def turn(self):
        for k, player in enumerate(self.players):
            player_walk(player, self.table)
            player_action(player, self.table)

            if player.is_broke():
                expropriate_player(player, self.table)
                del self.players[k]

            if len(self.players) <= 1:
                self.winner = self.players[0]
                break

    def run(self) -> Player | None:
        while self.winner is None:
            self.turn()
            if self.turns >= 1000:
                break
            self.turns += 1

        if self.winner is None:
            return None

        return self.winner


if __name__ == "__main__":
    turns_sum: int = 0
    for i in range(GAMES_TOTAL):
        players = bootstrap_players()
        ge = GameEngine(players)
        winner = ge.run()
        turns_sum += ge.turns
        name = winner.name if winner is not None else "Timeout"
        add_stats(name, STATS)

    print_stats(STATS, GAMES_TOTAL, turns_sum)
