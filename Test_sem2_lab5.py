import unittest
from sem2_lab5 import find_shortest_path

class TestKnightPath(unittest.TestCase):
    def test_example_case(self):
        self.assertEqual(find_shortest_path(8, (7, 0), (0, 7)), 6)

    def test_same_square(self):
        self.assertEqual(find_shortest_path(8, (3, 3), (3, 3)), 0)

    def test_one_move(self):
        self.assertEqual(find_shortest_path(8, (0, 0), (2, 1)), 1)
        self.assertEqual(find_shortest_path(8, (4, 4), (6, 5)), 1)

    def test_two_moves(self):
        self.assertEqual(find_shortest_path(8, (0, 0), (4, 2)), 2)

    def test_unreachable_target(self):
        self.assertEqual(find_shortest_path(3, (0, 0), (1, 1)), -1)

    def test_large_board(self):
        self.assertEqual(find_shortest_path(20, (0, 0), (19, 19)), 14)

if __name__ == '__main__':
    unittest.main()