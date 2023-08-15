from sys import path
import pytest

path.insert(0, '..')
from minesweeper.tile import Tile

@pytest.fixture
def tile():
    tile = Tile((3, 3))
    return tile

@pytest.mark.tile
def test_tile_constructor(tile):
    assert tile.get_coordinates() == (3, 3)
    assert tile.is_mine == False
    assert tile.num_adjacent_mines == None
    assert tile.is_flipped == False
    assert tile.is_flagged == False
    assert tile.is_question == False

@pytest.mark.tile
def test_simple_toggles(tile):
    assert tile.is_flagged == False
    assert tile.is_question == False
    tile.toggle_flag()
    assert tile.is_flagged == True
    assert tile.is_question == False
    tile.toggle_flag()
    assert tile.is_flagged == False
    assert tile.is_question == False
    tile.toggle_question()
    assert tile.is_flagged == False
    assert tile.is_question == True
    tile.toggle_question()
    assert tile.is_flagged == False
    assert tile.is_question == False

@pytest.mark.tile
def test_interacting_toggles(tile):
    assert tile.is_flagged == False
    assert tile.is_question == False
    tile.toggle_flag()
    tile.toggle_question()
    assert tile.is_flagged == False
    assert tile.is_question == True
    tile.toggle_flag()
    assert tile.is_flagged == True
    assert tile.is_question == False



