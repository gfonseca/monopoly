from typing import List

from .property import SaleProperty


class Table:
    TABLE_SIZE = 20
    PROPERTIES_VALUES: List[int] = [
        5500, 8500, 3500, 500, 9500,
        10000, 6500, 5000, 8000, 2000,
        9000, 6000, 2500, 4500, 4000,
        3000, 1000, 7000, 1500, 7500
    ]

    def __init__(self):
        self.squares: List[SaleProperty] = [
            SaleProperty(id=i, sale_value=Table.PROPERTIES_VALUES[i])
            for i in range(Table.TABLE_SIZE)
        ]

    def __getitem__(self, i: int) -> SaleProperty:
        return self.squares[i]
