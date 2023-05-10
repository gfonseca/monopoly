from abc import ABC, abstractclassmethod


class PlayerStrategy(ABC):

    @abstractclassmethod
    def makeDecision(self):
        pass


class Player:

    def __init__(self, name: str, strategy: PlayerStrategy):
        self.name: str = name
        self.strategy: PlayerStrategy = strategy
        self.bank: int = 0

    def is_broke(self):
        return self.bank < 0

    def receiveMoney(self, amount: int):
        self.bank += amount

# def build_player(name: str) -> Player:
#     match strategy:
#         case "random":
#             return Player(
#                 name="JohnRandom",
#                 strategy=RandomStrategy()
#             )