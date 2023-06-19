from board import Board
from human_control import HumanControl


def test_board_check():
    # initialize 5 * 5 board to test
    board1 = Board(5, 5, 100)
    hc1 = HumanControl(board1)
    # set some tiles on board1
    board1.table = [[0, 'white', 0, 0, 'black'],
                    [0, 'white', 0, 'white', 0],
                    [0, 'white', 'white', 0, 0],
                    [0, 0, 'white', 'black', 0],
                    [0, 0, 0, 0, 0]]
    hc1.board_check()
    # check the valid positions
    valid1 = (0, 0)
    valid2 = (1, 3)
    assert valid1 in hc1.vaild_positions
    assert valid2 in hc1.vaild_positions


def test_line_check():
    # still use board1 to check
    board1 = Board(5, 5, 100)
    hc1 = HumanControl(board1)
    # set some tiles on board1
    board1.table = [[0, 'white', 0, 0, 'black'],
                    [0, 'white', 0, 'white', 0],
                    [0, 'white', 'white', 0, 0],
                    [0, 0, 'white', 'black', 0],
                    [0, 0, 0, 0, 0]]
    # pick a valid cell to test
    col = 1
    row = 3
    # check the valid line: upper right
    xadd = 1
    yadd = -1
    hc1.line_check(col, row, xadd, yadd)
    assert hc1.vaild_positions == [(col, row)]
    # check an invaild line: up
    xadd = 0
    yadd = -1
    hc1.line_check(col, row, xadd, yadd)
    assert hc1.vaild_positions == [(col, row)]
    # pick an invalid cell to test
    col = 3
    row = 2
    for xadd in hc1.ADD:
        for yadd in hc1.ADD:
            hc1.line_check(col, row, xadd, yadd)
    assert hc1.vaild_positions == [(1, 3)]
