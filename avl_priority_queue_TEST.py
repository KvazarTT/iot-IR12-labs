import unittest
from avl_priority_queue import AVLPriorityQueue

class TestAVLPriorityQueue(unittest.TestCase):
    def setUp(self):
        self.pq = AVLPriorityQueue()
    def test_empty_queue(self):
        self.assertIsNone(self.pq.peek(), "Peek з порожньої черги має повертати None")
        self.assertIsNone(self.pq.pop(), "Pop з порожньої черги має повертати None")
        self.assertEqual(self.pq.view_queue(), [], "View для порожньої черги має бути порожнім списком")

    def test_single_insert(self):
        self.pq.insert("Тест 1", 10)
        self.assertEqual(self.pq.peek(), ("Тест 1", 10))
        self.assertEqual(self.pq.view_queue(), [("Тест 1", 10)])

    def test_priority_order_pop(self):
        self.pq.insert("Низький", 1)
        self.pq.insert("Високий", 100)
        self.pq.insert("Середній", 50)

        self.assertEqual(self.pq.pop(), ("Високий", 100))
        self.assertEqual(self.pq.pop(), ("Середній", 50))
        self.assertEqual(self.pq.pop(), ("Низький", 1))

        self.assertIsNone(self.pq.pop())

    def test_equal_priorities(self):
        self.pq.insert("Завдання A", 10)
        self.pq.insert("Завдання B", 10)

    def test_view_queue_order(self):
        self.pq.insert("A", 5)
        self.pq.insert("B", 15)
        self.pq.insert("C", 10)
        self.pq.insert("D", 20)

        expected_order = [("D", 20), ("B", 15), ("C", 10), ("A", 5)]
        self.assertEqual(self.pq.view_queue(), expected_order)

    def test_avl_balancing_stress(self):
        for i in range(1, 101):
            self.pq.insert(f"Task {i}", i)
        self.assertEqual(self.pq.peek(), ("Task 100", 100))
        for i in range(100, 0, -1):
            val, prio = self.pq.pop()
            self.assertEqual(prio, i)

if __name__ == '__main__':
    unittest.main()