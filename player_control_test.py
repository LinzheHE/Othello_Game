from board import Board
from player_control import PlayerControl


def test_flip():
    # initialize 5 * 5 board to test
    board1 = Board(5, 5, 100)
    pc1 = PlayerControl(board1)
    # set some tiles on board1
    board1.table = [[0, 'white', 0, 0, 'black'],
                    [0, 'white', 0, 'white', 0],
                    [0, 'white', 'white', 0, 0],
                    [0, 0, 'white', 'black', 0],
                    [0, 0, 0, 0, 0]]
    # conduct the flip() method to cell (col=1, row=3)
    col = 1
    row = 3
    color = 'black'
    pc1.flip(col, row, color)
    # check the flip
    assert board1.table == [[0, 'white', 0, 0, 'black'],
                            [0, 'white', 0, 'black', 0],
                            [0, 'white', 'black', 0, 0],
                            [0, 0, 'black', 'black', 0],
                            [0, 0, 0, 0, 0]]


def test_one_way():
    # initialize 5 * 5 board to test
    board2 = Board(5, 5, 100)
    pc2 = PlayerControl(board2)
    # set some tiles on board2
    board2.table = [[0, 0, 0, 'black', 0],
                    ['black', 0, 'white', 0, 0],
                    [0, 0, 'white', 'white', 'black'],
                    ['white', 'white', 'white', 0, 0],
                    [0, 'black', 0, 'black', 0]]
    col = 1
    row = 2
    color = 'black'
    # check the upper left direction
    xadd = -1
    yadd = -1
    pc2.one_way(col, row, color, xadd, yadd)
    assert board2.table == [[0, 0, 0, 'black', 0],
                            ['black', 0, 'white', 0, 0],
                            [0, 0, 'white', 'white', 'black'],
                            ['white', 'white', 'white', 0, 0],
                            [0, 'black', 0, 'black', 0]]
    # check the upper direction
    xadd = 0
    yadd = -1
    pc2.one_way(col, row, color, xadd, yadd)
    assert board2.table == [[0, 0, 0, 'black', 0],
                            ['black', 0, 'white', 0, 0],
                            [0, 0, 'white', 'white', 'black'],
                            ['white', 'white', 'white', 0, 0],
                            [0, 'black', 0, 'black', 0]]
    # check the upper right direction
    xadd = 1
    yadd = -1
    pc2.one_way(col, row, color, xadd, yadd)
    assert board2.table == [[0, 0, 0, 'black', 0],
                            ['black', 0, 'black', 0, 0],
                            [0, 0, 'white', 'white', 'black'],
                            ['white', 'white', 'white', 0, 0],
                            [0, 'black', 0, 'black', 0]]
    # check the right direction
    xadd = 1
    yadd = 0
    pc2.one_way(col, row, color, xadd, yadd)
    assert board2.table == [[0, 0, 0, 'black', 0],
                            ['black', 0, 'black', 0, 0],
                            [0, 0, 'black', 'black', 'black'],
                            ['white', 'white', 'white', 0, 0],
                            [0, 'black', 0, 'black', 0]]
    # check the bottom right direction
    xadd = 1
    yadd = 1
    pc2.one_way(col, row, color, xadd, yadd)
    assert board2.table == [[0, 0, 0, 'black', 0],
                            ['black', 0, 'black', 0, 0],
                            [0, 0, 'black', 'black', 'black'],
                            ['white', 'white', 'black', 0, 0],
                            [0, 'black', 0, 'black', 0]]
    # check the down direction
    xadd = 0
    yadd = 1
    pc2.one_way(col, row, color, xadd, yadd)
    assert board2.table == [[0, 0, 0, 'black', 0],
                            ['black', 0, 'black', 0, 0],
                            [0, 0, 'black', 'black', 'black'],
                            ['white', 'black', 'black', 0, 0],
                            [0, 'black', 0, 'black', 0]]
    # check the bottom left direction
    xadd = -1
    yadd = 1
    pc2.one_way(col, row, color, xadd, yadd)
    assert board2.table == [[0, 0, 0, 'black', 0],
                            ['black', 0, 'black', 0, 0],
                            [0, 0, 'black', 'black', 'black'],
                            ['white', 'black', 'black', 0, 0],
                            [0, 'black', 0, 'black', 0]]
