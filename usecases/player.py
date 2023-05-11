from typing import List

from entity.player import Player, build_player


PLAYER_STRATEGIES = ["random", "cautious", "demanding", "impulsive"]


def bootstrap_players():
    players: List[Player] = [build_player(s) for s in PLAYER_STRATEGIES]
    for p in players:
        p.receive_money(300)

    return players


def make_money_transaction(player_a: Player, player_b: Player, amount: int):
    player_a.pay_money(amount)

    if player_a.bank < 0:
        amount = amount + player_a.bank

    player_b.receive_money(amount)
