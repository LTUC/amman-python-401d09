from demo.ten_thousand.ten_thousand import Game
from demo.tests.flo import diff
import pytest

def test_no_for_play_game():
    game = Game()
    diffs = diff(game.play, 'version_2/quitter.sim.txt')
    assert not diffs, diffs