#! /usr/bin/env python3

from functools import reduce
from termcolor import colored
from typing import List

from usecases.player import bootstrap_players, player_walk, player_action
from entity.player import Player
from entity.table import Table
from utils import add_stats, print_stats


GAMES_TOTAL = 300
STATS = {}


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


if __name__ == "__main__":
    for i in range(GAMES_TOTAL):
        players = bootstrap_players()
        ge = GameEngine(players)
        winner = ge.run()
        name = winner.name if winner is not None else "Timeout"
        add_stats(name)
    print_stats(STATS)
