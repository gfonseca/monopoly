from unittest.mock import MagicMock
import pytest

from usecases.player import \
    bootstrap_players, \
    player_walk, \
    player_action


@pytest.fixture(scope="function")
def receive_money_mock(mocker):
    return mocker.patch("entity.player.Player.receive_money")

@pytest.fixture
def player_mock(mocker):
    return mocker.patch("entity.player.Player")


class TestUsecasesPlayer:

    def test_boot_strap_players(self, receive_money_mock: MagicMock):
        bootstrap_players()
        assert receive_money_mock.call_count == 4

    def test_player_walk(self, mocker, player_mock):
        DICE_VALUE = 4
        TABLE_SIZE = 20
        walk_mock = mocker.patch("entity.player.Player.walk")

        table_mock = mocker.patch("entity.table.Table")
        table_mock.get_size = mocker.Mock()
        table_mock.get_size.return_value = TABLE_SIZE

        randint_mock = mocker.patch("random.randint")
        randint_mock.return_value = DICE_VALUE

        player_walk(player_mock, table_mock)

        walk_mock.assert_called_once_with(DICE_VALUE, TABLE_SIZE)

    # def test_expropriate_player(self):

    #     expropriate_player(player, table)

    def test_player_action_pay_rent(self, mocker):
        PLAYER_SQUARE = 13
        RENTAL_VALUE = 50
        SALE_VALUE = 500

        mock_player2: MagicMock = mocker.patch("entity.player.Player")
        mock_player: MagicMock = mocker.patch("entity.player.Player")
        mock_player.pay_rent: MagicMock = mocker.Mock()
        mock_player.bank: 200
        mock_player.square = PLAYER_SQUARE

        mock_table: MagicMock = mocker.patch("entity.table.Table")

        mock_prop: MagicMock = mocker.patch("entity.property.SaleProperty")
        mock_prop.get_owner: MagicMock = mocker.Mock()
        mock_prop.rental_value = RENTAL_VALUE
        mock_prop.sale_value = SALE_VALUE
        mock_prop.get_owner.return_value = mock_player2

        mock_table: MagicMock = mocker.patch("entity.table.Table")
        mock_table.__getitem__: MagicMock = mocker.Mock()
        mock_table.__getitem__.return_value = mock_prop

        player_action(mock_player, mock_table)

        mock_player.pay_rent.assert_called_once_with(mock_player2, RENTAL_VALUE)
        mock_table.__getitem__.assert_called_once_with(PLAYER_SQUARE)
        mock_prop.get_owner.assert_called_once()


    def test_player_action_pay_rent(self, mocker):
        PLAYER_SQUARE = 13
        RENTAL_VALUE = 50
        SALE_VALUE = 500

        mock_player: MagicMock = mocker.patch("entity.player.Player")
        mock_player.pay_rent: MagicMock = mocker.Mock()
        mock_player.bank = SALE_VALUE
        mock_player.make_decision: MagicMock = mocker.Mock()
        mock_player.square = PLAYER_SQUARE

        mock_table: MagicMock = mocker.patch("entity.table.Table")

        mock_prop: MagicMock = mocker.patch("entity.property.SaleProperty")
        mock_prop.get_owner: MagicMock = mocker.Mock()
        mock_prop.rental_value = RENTAL_VALUE
        mock_prop.sale_value = SALE_VALUE
        mock_prop.get_owner.return_value = None

        mock_table: MagicMock = mocker.patch("entity.table.Table")
        mock_table.__getitem__: MagicMock = mocker.Mock()
        mock_table.__getitem__.return_value = mock_prop

        player_action(mock_player, mock_table)

        mock_player.pay_rent.assert_not_called()
        mock_player.make_decision.assert_called_once_with(RENTAL_VALUE)
        mock_table.__getitem__.assert_called_once_with(PLAYER_SQUARE)
        mock_prop.get_owner.assert_called_once()

        assert mock_prop.owner == mock_player
