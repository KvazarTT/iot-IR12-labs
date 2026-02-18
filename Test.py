import unittest
from Labs.Lab1.sem2_lab1 import two_sum, is_monotonic, find_unsorted_subarray

class TestLabWork(unittest.TestCase):

    def test_level_1_two_sum(self):
        self.assertEqual(two_sum([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(two_sum([3, 2, 4], 6), [1, 2])
        self.assertEqual(two_sum([3, 3], 6), [0, 1])
        self.assertEqual(two_sum([3, 5], 6), -1)

    def test_level_2_monotonic(self):
        self.assertTrue(is_monotonic([1, 2, 3, 4, 5]))
        self.assertTrue(is_monotonic([5, 4, 3, 2, 1]))
        self.assertFalse(is_monotonic([1, 2, 2, 3, 2, 4]))
        self.assertTrue(is_monotonic([1, 1, 1]))
        self.assertTrue(is_monotonic([10]))

    def test_level_3_unsorted_subarray(self):
        case1 = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
        self.assertEqual(find_unsorted_subarray(case1), (3, 9))
        self.assertEqual(find_unsorted_subarray([1, 2, 3, 4]), (-1, -1))
        self.assertEqual(find_unsorted_subarray([5, 4, 3, 2, 1]), (0, 4))
        self.assertEqual(find_unsorted_subarray([1]), (-1, -1))
        self.assertEqual(find_unsorted_subarray([1, 3, 2, 2, 2]), (1, 4))


if __name__ == '__main__':
    unittest.main()