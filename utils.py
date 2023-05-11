
from functools import reduce
from termcolor import colored

def add_stats(name: str, stats: dict):
    if name not in stats:
        stats[name] = 1
        return

    stats[name] += 1


def print_stats(stats: dict, games_total: int, total_turns):
    colors = ["yellow", "white", "red", "blue"]
    place: int = 0

    # Total of matches that end in turn 1000
    timeouts = stats.pop("Timeout")

    # Average of turns per match
    turns_avg = int(total_turns / games_total)

    # Sum of players victories
    total_wins = reduce(lambda x, y: x+y, stats.values())

    # PLayer ranking by victories
    players = list(stats.items())
    players.sort(reverse=True, key=lambda t: t[1])

    print(colored(" "*8 + "MONOPOLY\n", "blue"))
    print(colored(" - PLAYER NAME -\t- WINS -\t- RATE -", "blue"))
    for name, victories in players:
        vic_tax = "%.2f" % (victories/total_wins*100)
        print(colored(f"{place+1}◉  {name}:\t  {victories}\t\t {vic_tax}%", colors[place]))
        place += 1
    print("\n")

    print(f"Players Wins:\t{total_wins}")
    print(f"Matches totals:\t{games_total}")
    print(f"Turns Average:\t{turns_avg}")
    print(f"Timeouts:\t{timeouts}")
