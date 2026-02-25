import unittest
import sem2_lab2

class TestSquareFit(unittest.TestCase):
    def test_can_fit(self):
        self.assertTrue(sem2_lab2.can_fit(9, 10, 2, 3))
        self.assertFalse(sem2_lab2.can_fit(8, 10, 2, 3))

    def test_get_min_square_size(self):
        self.assertEqual(sem2_lab2.get_min_square_size(10, 2, 3), 9)
        self.assertEqual(sem2_lab2.get_min_square_size(1, 5, 7), 7)
        self.assertEqual(sem2_lab2.get_min_square_size(4, 1, 1), 2)

if __name__ == "__main__":
    unittest.main()