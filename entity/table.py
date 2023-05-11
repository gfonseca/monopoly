from typing import List

from entity.player import Player

from .property import SaleProperty


class Table:
    TABLE_SIZE = 20

    PROPERTIES_VALUES: List[int] = [
        360, 560, 40, 520, 480,
        440, 160, 320, 720, 280,
        760, 800, 120, 200, 640,
        600, 680, 240, 400, 80
    ]

    def __init__(self):
        self.squares: List[SaleProperty] = [
            SaleProperty(id=i, sale_value=Table.PROPERTIES_VALUES[i])
            for i in range(Table.TABLE_SIZE)
        ]

    def get_size(self):
        return len(self.squares)

    def expropriate_player(self, player: Player):
        properties = filter(lambda x: x.owner is not None,  self.squares)
        for s in properties:
            owner = s.get_owner()
            if owner.name == player.name:
                s.owner = None

    def __getitem__(self, i: int) -> SaleProperty:
        return self.squares[i]
