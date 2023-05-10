from typing import List

from entity.player import Player


def bootstrap_players(players: List[Player]):
    for p in players:
        p.receive_money(300)
