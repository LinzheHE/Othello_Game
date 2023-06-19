from board import Board
from computer_control import ComputerControl


def test_board_check():
    # initialize 5 * 5 board to test
    board1 = Board(5, 5, 100)
    cc1 = ComputerControl(board1)
    # set some tiles on board1
    board1.table = [[0, 'black', 0, 0, 'white'],
                    [0, 'black', 0, 'black', 0],
                    [0, 'black', 'black', 0, 0],
                    [0, 0, 'black', 'white', 0],
                    [0, 0, 0, 0, 0]]
    # check the initial value
    assert cc1.best_position == (-1, -1)
    # check the function
    cc1.board_check()
    assert cc1.best_position == ((1, 3))


def test_cell_check():
    # still use board1 to test
    board1 = Board(5, 5, 100)
    cc1 = ComputerControl(board1)
    # set some tiles on board1
    board1.table = [[0, 'black', 0, 0, 'white'],
                    [0, 'black', 0, 'black', 0],
                    [0, 'black', 'black', 0, 0],
                    [0, 0, 'black', 'white', 0],
                    [0, 0, 0, 0, 0]]
    # check for valid cell (0, 0)
    col = 0
    row = 0
    flips_1 = 2
    total_flips_1 = cc1.cell_check(col, row)
    assert total_flips_1 == flips_1
    # check for valid cell (1, 3)
    col = 1
    row = 3
    flips_2 = 3
    total_flips_2 = cc1.cell_check(col, row)
    assert total_flips_2 == flips_2
    # check for invalid cell (2, 0)
    col = 2
    row = 0
    flips_3 = 0
    total_flips_3 = cc1.cell_check(col, row)
    assert total_flips_3 == flips_3


def test_line_check():
    # still use board1 to test
    board1 = Board(5, 5, 100)
    cc1 = ComputerControl(board1)
    # set some tiles on board1
    board1.table = [[0, 'black', 0, 0, 'white'],
                    [0, 'black', 0, 'black', 0],
                    [0, 'black', 'black', 0, 0],
                    [0, 0, 'black', 'white', 0],
                    [0, 0, 0, 0, 0]]
    # check for valid cell and valid line
    col = 1
    row = 3
    xadd = 1
    yadd = -1
    flips = 2
    total_flip = cc1.line_check(col, row, xadd, yadd)
    assert total_flip == flips
    # check for invalid case
    col = 1
    row = 3
    xadd = 0
    yadd = -1
    total_flip = cc1.line_check(col, row, xadd, yadd)
    assert total_flip is None
