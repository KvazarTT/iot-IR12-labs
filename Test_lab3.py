import unittest
from Labs.Lab3.sem2_lab3 import BinaryTree, is_tree_balanced

class TestBinaryTreeBalance(unittest.TestCase):
    def test_empty_tree(self):
        self.assertTrue(is_tree_balanced(None))

    def test_single_node(self):
        root = BinaryTree(1)
        self.assertTrue(is_tree_balanced(root))

    def test_balanced_tree_from_example(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.right = BinaryTree(3)
        root.left.left = BinaryTree(4)
        root.left.right = BinaryTree(5)

        self.assertTrue(is_tree_balanced(root))

    def test_balanced_tree_second_example(self):
        root = BinaryTree(3)
        root.left = BinaryTree(9)
        root.right = BinaryTree(20)
        root.right.left = BinaryTree(15)
        root.right.right = BinaryTree(7)

        self.assertTrue(is_tree_balanced(root))

    def test_unbalanced_tree(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.left.left = BinaryTree(3)

        self.assertFalse(is_tree_balanced(root))

    def test_unbalanced_tree_complex(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.right = BinaryTree(2)
        root.left.left = BinaryTree(3)
        root.left.right = BinaryTree(3)
        root.left.left.left = BinaryTree(4)
        root.left.left.right = BinaryTree(4)

        self.assertFalse(is_tree_balanced(root))

if __name__ == '__main__':
    unittest.main()