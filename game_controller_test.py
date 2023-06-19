from board import Board
from game_manager import GameManager
from game_controller import GameController


def test_status_check():
    bd = Board(3, 3, 100)
    gm = GameManager(bd)
    gc = GameController(bd, gm)
    # check initial value
    assert gc.game_over is False
    # initilize a board to check
    bd.table = [["black", "black", "black"],
                ["black", "black", "black"],
                ["black", "black", "black"]]
    gc.status_check()
    assert gc.game_over is True


def test_name_record():
    name = "yyy"
    bd = Board(3, 3, 100)
    gm = GameManager(bd)
    gc = GameController(bd, gm)
    gc.name_record(name)
    assert gc.user_name == name
