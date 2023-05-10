from typing import List

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

    def __getitem__(self, i: int) -> SaleProperty:
        return self.squares[i]
