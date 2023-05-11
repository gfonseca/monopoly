from typing import List
import random

from entity.player import Player, build_player
from entity.table import Table


PLAYER_STRATEGIES = ["random", "cautious", "demanding", "impulsive"]


def bootstrap_players():
    players: List[Player] = [build_player(s) for s in PLAYER_STRATEGIES]
    for p in players:
        p.receive_money(300)

    random.shuffle(players)
    return players


def make_money_transaction(player_a: Player, player_b: Player, amount: int):
    player_a.pay_money(amount)

    if player_a.bank < 0:
        amount = amount + player_a.bank

    player_b.receive_money(amount)


def player_walk(player: Player, table: Table):
    dice = random.randint(1, 6)
    table_size = table.get_size()
    player.walk(dice, table_size)
