from abc import ABC, abstractclassmethod
import random


class PlayerStrategy(ABC):

    @abstractclassmethod
    def make_decision(self, rent_value: int, player_balance: int) -> bool:
        pass


class RandomStrategy(PlayerStrategy):

    def make_decision(self, rent_value: int, player_balance: int) -> bool:
        if random.randint(1, 10) > 5:
            return True

        return False


class ImpulsiveStrategy(PlayerStrategy):

    def make_decision(self, rent_value: int, player_balance: int) -> bool:
        return True


class DemandingStrategy(PlayerStrategy):

    def make_decision(self, rent_value: int, player_balance: int) -> bool:
        if rent_value > 50:
            return True

        return False


class CautiousStrategy(PlayerStrategy):

    def make_decision(self, rent_value: int, player_balance: int) -> bool:
        if player_balance > 80:
            return True

        return False


class Player:

    WAGE = 100

    def __init__(self, name: str, strategy: PlayerStrategy):
        self.strategy: PlayerStrategy = strategy
        self.name: str = name
        self.bank: int = 0
        self.square: int = 0

    def is_broke(self) -> bool:
        return self.bank < 0

    def receive_money(self, amount: int):
        self.bank += amount

    def pay_money(self, amount: int):
        self.bank -= amount

    def walk(self, walk_squares: int, table_size: int) -> bool:

        if (self.square + walk_squares) > table_size - 1:
            self.bank += Player.WAGE
            self.square = (self.square - table_size) + walk_squares
            return

        self.square += walk_squares

    def pay_rent(self, player_b: "Player", amount: int):
        self.pay_money(amount)

        if self.bank < 0:
            amount = amount + self.bank

        player_b.receive_money(amount)

    def make_decision(self, rent_value: int) -> bool:
        return self.strategy.make_decision(rent_value, self.bank)


def build_player(strategy_name: str) -> Player:
    match strategy_name:
        case "random":
            return Player(
                name="John Random",
                strategy=RandomStrategy()
            )
        case "cautious":
            return Player(
                name="Ned Cautious",
                strategy=CautiousStrategy()
            )
        case "impulsive":
            return Player(
                name="Robb Impulsive",
                strategy=ImpulsiveStrategy()
            )
        case "demanding":
            return Player(
                name="Caty Demanding",
                strategy=DemandingStrategy()
            )
