#! /usr/bin/env python3
from functools import reduce
from gameengine import GameEngine
from termcolor import colored

from usecases.player import bootstrap_players

GAMES_TOTAL = 1000
STATS = {}


def add_stats(name):
    if name not in STATS:
        STATS[name] = 1
        return

    STATS[name] += 1


def print_stats(stats: dict):
    colors = ["yellow", "white", "red", "blue"]
    timeouts = stats.pop("Timeout")
    place: int = 0
    total_wins = reduce(lambda x, y : x+y, stats.values())
    d = list(stats.items())
    d.sort(reverse=True, key=lambda t: t[1])
    print(colored(" "*8 + "MONOPOLY\n", "blue"))
    print(colored(" - PLAYER NAME -\t- WINS -\t- RATE -", "blue"))
    for name, victories in d:
        vic_tax = "%.2f" % (victories/total_wins*100)
        print(colored(f"{place+1}◉  {name}:\t  {victories}\t\t {vic_tax}%", colors[place]))
        place += 1
    print("\n")

    print(f"Players Wins:\t{total_wins}")
    print(f"Matches totals:\t{GAMES_TOTAL}")
    print(f"Timeouts:\t{timeouts}")


if __name__ == "__main__":
    for i in range(GAMES_TOTAL):
        players = bootstrap_players()
        ge = GameEngine(players)
        winner = ge.run()
        name = winner.name if winner is not None else "Timeout"
        add_stats(name)
    print_stats(STATS)
