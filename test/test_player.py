from unittest.mock import MagicMock
import pytest
from entity.player import DemandingStrategy, Player, RandomStrategy


@pytest.fixture(scope="function")
def mock_strategy(mocker):
    return mocker.patch('entity.player.PlayerStrategy')


@pytest.fixture(scope="function")
def player_john(mock_strategy):
    return Player(name="JohnRandom", strategy=mock_strategy)


@pytest.fixture(scope="function")
def player_ned(mocker):
    return mocker.patch('entity.player.Player')


class TestPlayer:

    def test_not_start_broken(self, player_john):
        assert not player_john.is_broke()

    def test_broken_player(self, player_john):
        player_john.bank = -1

        assert player_john.is_broke()

    def test_receive_money(self, player_john):
        player_john.receive_money(300)
        assert player_john.bank == 300

    def test_pay_money(self, player_john):
        player_john.bank = 400
        player_john.pay_money(400)

        assert player_john.bank == 0

    def test_strategy(self, mocker, mock_strategy):
        PROPERTY_VALUE = 1500
        mock_strategy.make_decision = MagicMock()
        mock_strategy.make_decision.return_value = True
        p = Player(name="JohnRandom", strategy=mock_strategy)
        res = p.make_decision(PROPERTY_VALUE)

        mock_strategy.make_decision.assert_called_once()
        assert res


class TestStrategy:

    def test_random_strategy(self):
        PROPERTY_VALUE = 0
        PLAYER_BALANCE = 0
        strategy = RandomStrategy()
        res = strategy.make_decision(PROPERTY_VALUE, PLAYER_BALANCE)

        assert isinstance(res, bool)

    def test_demanding_strategy_deny(self):
        RENT_VALUE = 10
        PLAYER_BALANCE = 0
        strategy = DemandingStrategy()
        res = strategy.make_decision(RENT_VALUE, PLAYER_BALANCE)

        assert res == False

    def test_demanding_strategy_agree(self):
        RENT_VALUE = 51
        PLAYER_BALANCE = 0
        strategy = DemandingStrategy()
        res = strategy.make_decision(RENT_VALUE, PLAYER_BALANCE)

        assert res

    def test_demanding_strategy_agree(self):
        RENT_VALUE = 51
        PLAYER_BALANCE = 100

        strategy = DemandingStrategy()
        res = strategy.make_decision(RENT_VALUE, PLAYER_BALANCE)

        assert res
