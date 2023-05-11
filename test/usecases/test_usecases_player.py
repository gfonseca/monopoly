from unittest.mock import MagicMock
import pytest

from usecases.player import \
    bootstrap_players, \
    make_money_transaction, \
    player_walk 


@pytest.fixture(scope="function")
def receive_money_mock(mocker):
    return mocker.patch("entity.player.Player.receive_money")


@pytest.fixture
def pay_money_mock(mocker):
    return mocker.patch("entity.player.Player.pay_money")


@pytest.fixture
def player_mock(mocker):
    return mocker.patch("entity.player.Player")


class TestUsecasesPlayer:

    def test_boot_strap_players(self, receive_money_mock: MagicMock):
        bootstrap_players()
        assert receive_money_mock.call_count == 4

    def test_make_money_transaction(
        self,
        player_mock,
        pay_money_mock: MagicMock,
        receive_money_mock: MagicMock
    ):
        TRANSACTION_AMOUNT = 500
        player_mock.bank = 500

        make_money_transaction(
            player_a=player_mock,
            player_b=player_mock,
            amount=TRANSACTION_AMOUNT
        )

        pay_money_mock.assert_called_once_with(TRANSACTION_AMOUNT)
        receive_money_mock.assert_called_once_with(TRANSACTION_AMOUNT)

    def test_money_transaction_low_budget(
        self,
        player_mock,
        pay_money_mock: MagicMock,
        receive_money_mock: MagicMock
    ):
        TRANSACTION_AMOUNT = 500
        PLAYER_A_BUDGET = 250

        player_mock.bank = -250

        make_money_transaction(
            player_a=player_mock,
            player_b=player_mock,
            amount=TRANSACTION_AMOUNT
        )

        pay_money_mock.assert_called_once_with(TRANSACTION_AMOUNT)
        receive_money_mock.assert_called_once_with(PLAYER_A_BUDGET)

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