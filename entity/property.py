from .player import Player


class SaleProperty:
    RENTAL_TAX = 0.10

    def __init__(self, id: str, sale_value: int):
        self.id: str = id
        self.owner: Player = None
        self.sale_value: int = sale_value
        self.rental_value: int = self._calc_rent_value(sale_value)

    def get_owner(self) -> Player | None:
        return self.owner

    def _calc_rent_value(self, value: int) -> int:
        return int(value * SaleProperty.RENTAL_TAX)
