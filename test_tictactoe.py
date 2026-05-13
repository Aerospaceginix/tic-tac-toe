import unittest
from tictactoe import check_winner, is_full

class TestTicTacToe(unittest.TestCase):
    def test_check_winner_row(self):
        board = [["X", "X", "X"], [" ", " ", " "], [" ", " ", " "]]
        self.assertEqual(check_winner(board), "X")

    def test_check_winner_col(self):
        board = [["O", " ", " "], ["O", " ", " "], ["O", " ", " "]]
        self.assertEqual(check_winner(board), "O")

    def test_check_winner_diag(self):
        board = [["X", " ", " "], [" ", "X", " "], [" ", " ", "X"]]
        self.assertEqual(check_winner(board), "X")

    def test_is_full(self):
        board = [["X", "O", "X"], ["X", "O", "X"], ["O", "X", "O"]]
        self.assertTrue(is_full(board))

    def test_not_full(self):
        board = [["X", "O", "X"], ["X", " ", "X"], ["O", "X", "O"]]
        self.assertFalse(is_full(board))

if __name__ == "__main__":
    unittest.main()
