class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.left = None
        self.right = None
        self.height = 1

class AVLPriorityQueue:
    def __init__(self):
        self.root = None

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def right_rotate(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        return x

    def left_rotate(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def insert(self, value, priority):
        self.root = self._insert_node(self.root, value, priority)

    def _insert_node(self, node, value, priority):
        if not node:
            return Node(value, priority)

        if priority >= node.priority:
            node.left = self._insert_node(node.left, value, priority)
        else:
            node.right = self._insert_node(node.right, value, priority)

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

        balance = self.get_balance(node)
        if balance > 1 and priority >= node.left.priority:
            return self.right_rotate(node)

        if balance < -1 and priority < node.right.priority:
            return self.left_rotate(node)

        if balance > 1 and priority < node.left.priority:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        if balance < -1 and priority >= node.right.priority:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)
        return node

    def pop(self):
        if not self.root:
            return None
        self.root, popped_node = self._pop_leftmost(self.root)
        return popped_node.value, popped_node.priority

    def _pop_leftmost(self, node):
        if node.left is None:
            return node.right, node

        node.left, popped_node = self._pop_leftmost(node.left)
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance = self.get_balance(node)

        if balance < -1:
            balance_right = self.get_balance(node.right)
            if balance_right <= 0:
                return self.left_rotate(node), popped_node
            else:
                node.right = self.right_rotate(node.right)
                return self.left_rotate(node), popped_node

        return node, popped_node

    def peek(self):
        if not self.root:
            return None
        current = self.root
        while current.left is not None:
            current = current.left
        return current.value, current.priority

    def view_queue(self):
        elements = []
        self._in_order(self.root, elements)
        return elements

    def _in_order(self, node, elements):
        if node:
            self._in_order(node.left, elements)
            elements.append((node.value, node.priority))
            self._in_order(node.right, elements)