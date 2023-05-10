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
        pass


class Player:

    def __init__(self, name: str, strategy: PlayerStrategy):
        self.strategy: PlayerStrategy = strategy
        self.name: str = name
        self.bank: int = 0

    def is_broke(self) -> bool:
        return self.bank < 0

    def receive_money(self, amount: int):
        self.bank += amount

    def pay_money(self, amount: int):
        self.bank -= amount

    def make_decision(self, rent_value: int) -> bool:
        return self.strategy.make_decision(rent_value, self.bank)


# def build_player(name: str) -> Player:
#     match strategy:
#         case "random":
#             return Player(
#                 name="JohnRandom",
#                 strategy=RandomStrategy()
#             )
