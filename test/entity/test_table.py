from random import shuffle
from unittest.mock import MagicMock
import pytest

from entity.table import Table, SaleProperty


class TestTable:
    def test_table_build(self):
        TOTAL_SQUARES = 20
        t = Table()
        assert len(t.squares) == TOTAL_SQUARES

    def test_squares_values(self):
        VALUES = Table.PROPERTIES_VALUES
        t = Table()
        for s in t.squares:
            if s.sale_value not in VALUES:
                pytest.fail(
                    f"sale_value {s.sale_value} not in value list"
                )

    def test_assert_getitem_type(self):
        t = Table()
        table_square = t[2]
        assert isinstance(table_square, SaleProperty)

    @pytest.mark.skip
    def test_expropriate_player(self, mocker):
        player: MagicMock = mocker.patch("entity.player.Player")
        get_owner: MagicMock = mocker.patch("entity.property.SaleProperty.get_owner")
        sale_property: MagicMock = mocker.patch("entity.property.SaleProperty")

        sale_property.owner = "John Random"

        t = Table()
        t.squares = [sale_property for _ in range(20)]
        t.expropriate_player(player)
        assert get_owner.call_count == 20
