from typing import List
import random

from entity.player import Player, build_player
from entity.property import SaleProperty
from entity.table import Table


PLAYER_STRATEGIES = ["random", "cautious", "demanding", "impulsive"]


def bootstrap_players():
    players: List[Player] = [build_player(s) for s in PLAYER_STRATEGIES]
    for p in players:
        p.receive_money(300)

    random.shuffle(players)
    return players

# def expropriate_player(player: Player)

def player_walk(player: Player, table: Table):
    dice = random.randint(1, 6)
    table_size = table.get_size()
    player.walk(dice, table_size)


def player_action(player: Player, table: Table):
    sale_property: SaleProperty = table[player.square]
    owner = sale_property.get_owner()

    # Fell in private property
    if owner:
        player.pay_rent(owner, sale_property.rental_value)
        return

    # Just don`t have money to buy
    if player.bank < sale_property.sale_value:
        return

    # Make decision based on player strategy
    if player.make_decision(sale_property.rental_value):
        player.pay_money(sale_property.sale_value)
        sale_property.owner = player
