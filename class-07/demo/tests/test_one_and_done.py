from demo.ten_thousand.ten_thousand import Game
from demo.tests.flo import diff
import pytest


def test_one_and_done():
    game = Game()
    diffs = diff(game.play, 'version_2/one_and_done.sim.txt')
    assert not diffs, diffs