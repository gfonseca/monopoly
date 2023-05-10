from unittest.mock import MagicMock
import pytest

from usecases.players import bootstrap_players


@pytest.fixture
def player_mock(mocker):
    return mocker.patch("entity.player.Player")


class TestPlayerUsecases:

    def test_boot_strap_players(self, player_mock: MagicMock):
        player_mock.receive_money = MagicMock()
        players = [player_mock for p in range(4)]
        bootstrap_players(players)
        assert player_mock.receive_money.call_count == 4
