from tile import Tile


def test_constructor():
    column = 1
    row = 2
    color = 'blue'
    CELL_SIZE = 90
    tile = Tile(column, row, color, CELL_SIZE)
    assert tile.column == 1
    assert tile.row == 2
    assert tile.color == 'blue'
    assert tile.CELL_SIZE == 90
