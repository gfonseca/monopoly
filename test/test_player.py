import pytest
import mock

from entity.player import Player, PlayerStrategy


class TestPlayer:
    def test_broken(self):
        PLAYER_NAME = "JohnRandom"
        stg = mock.Mock(PlayerStrategy)
        p = Player(name=PLAYER_NAME, strategy=stg)

        assert p.is_broke() == False
