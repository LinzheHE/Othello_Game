from board import Board


def test_board_constructor():
    COLUMNS = 4
    ROWS = 4
    CELL_SIZE = 100
    board1 = Board(COLUMNS, ROWS, CELL_SIZE)
    # test the input values
    assert board1.COLUMNS == 4
    assert board1.ROWS == 4
    assert board1.CELL == 100
    # test the table
    assert board1.table == [[0, 0, 0, 0], [0, 'white', 'black', 0],
                            [0, 'black', 'white', 0], [0, 0, 0, 0]]
    # test the initial values
    tile_count = 0
    tiles = []
    assert board1.black_count == tile_count
    assert board1.white_count == tile_count
    assert board1.black_tiles == []
    assert board1.white_tiles == []

    COLUMNS = 2
    ROWS = 2
    CELL_SIZE = 100
    board2 = Board(COLUMNS, ROWS, CELL_SIZE)
    # test the input values
    assert board2.COLUMNS == 2
    assert board2.ROWS == 2
    assert board2.CELL == 100
    # test the table
    assert board2.table == [['white', 'black'], ['black', 'white']]
