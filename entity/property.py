from .player import Player


class SaleProperty:
    RENTAL_TAX = 0.3

    def __init__(self, id: str, sale_value: int):
        self.id: str = id
        self.owner: Player = None
        self.sale_value: int = sale_value
        self.rental_value: int = int(sale_value * SaleProperty.RENTAL_TAX)

    def getOwner(self) -> Player | None:
        return self.owner
