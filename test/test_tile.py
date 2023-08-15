from sys import path
import pytest

path.insert(0, '..')
from minesweeper.tile import Tile

@pytest.fixture
def tile():
    tile = Tile((3, 3))
    return tile

@pytest.mark.tile
def test_safe_tile(tile):
    assert tile.coordinates == (3, 3)
    assert tile.is_mine == False
    assert tile.num_adjacent_mines == None
    assert tile.is_flipped == False
    assert tile.is_flagged == False
    assert tile.is_question == False

