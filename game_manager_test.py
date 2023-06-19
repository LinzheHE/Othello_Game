from board import Board
from game_manager import GameManager


def test_human_make_move():
    # initialize 5 * 5 board to test
    board1 = Board(5, 5, 100)
    gm1 = GameManager(board1)
    # set some tiles on board1
    board1.table = [[0, 'white', 0, 0, 'black'],
                    [0, 'white', 0, 'white', 0],
                    [0, 'white', 'white', 0, 0],
                    [0, 0, 'white', 'black', 0],
                    [0, 0, 0, 0, 0]]
    # check the initial value
    assert gm1.human_turn is True

    # when choose a valid position (1, 3)
    mouseX = 150
    mouseY = 350
    gm1.human_make_move(mouseX, mouseY)
    # test the updated board
    assert gm1.board.table == [[0, 'white', 0, 0, 'black'],
                               [0, 'white', 0, 'black', 0],
                               [0, 'white', 'black', 0, 0],
                               [0, 'black', 'black', 'black', 0],
                               [0, 0, 0, 0, 0]]
    # test the turn
    assert gm1.human_turn is False
    # when choose an invalid
    mouseX = 50
    mouseY = 50
    gm1.human_make_move(mouseX, mouseY)
    # test the updated board
    assert gm1.board.table == [[0, 'white', 0, 0, 'black'],
                               [0, 'white', 0, 'black', 0],
                               [0, 'white', 'black', 0, 0],
                               [0, 'black', 'black', 'black', 0],
                               [0, 0, 0, 0, 0]]


def test_computer_make_move():
    # initialize 5 * 5 board to test
    board1 = Board(5, 5, 100)
    gm1 = GameManager(board1)
    # set some tiles on board1
    board1.table = [[0, 'black', 0, 0, 'white'],
                    [0, 'black', 0, 'black', 0],
                    [0, 'black', 'black', 0, 0],
                    [0, 0, 'black', 'white', 0],
                    [0, 0, 0, 0, 0]]
    # change it to computer's turn
    gm1.human_turn = False
    # test
    gm1.computer_make_move()
    assert gm1.board.table == [[0, 'black', 0, 0, 'white'],
                               [0, 'black', 0, 'white', 0],
                               [0, 'black', 'white', 0, 0],
                               [0, 'white', 'white', 'white', 0],
                               [0, 0, 0, 0, 0]]
