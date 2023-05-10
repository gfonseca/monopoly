from entity.table import SaleProperty


class TestSaleProperty:
    def test_rent_value(self):
        SALE_VALUE = 10000
        RENTAL = 3000

        p = SaleProperty(id=1, sale_value=SALE_VALUE)
        assert p.rental_value == RENTAL
