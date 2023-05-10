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
