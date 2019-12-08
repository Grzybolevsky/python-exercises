# coding=utf-8
import unittest


class Node:
    """Klasa reprezentująca węzeł drzewa binarnego."""

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

    def insert(self, node):
        if self.data < node.data:  # na prawo
            if self.right:
                self.right.insert(node)
            else:
                self.right = node
        elif self.data > node.data:  # na lewo
            if self.left:
                self.left.insert(node)
            else:
                self.left = node
        else:
            pass  # ignoruję duplikaty

    def count(self):
        counter = 1
        if self.left:
            counter += self.left.count()
        if self.right:
            counter += self.right.count()
        return counter

    def search(self, data):
        if self.data == data:
            return self
        if data < self.data:
            if self.left:
                return self.left.search(data)
        else:
            if self.right:
                return self.right.search(data)
        return None


def bst_max(top):
    if top is None:
        raise ValueError("Lacze do korzenia jest puste")
    elif not isinstance(top, Node):
        raise ValueError("Argument top nie jest typu Node")
    current_node = top
    while current_node.right is not None:
        current_node = current_node.right
    return current_node


def bst_min(top):
    if top is None:
        raise ValueError("Lacze do korzenia jest puste")
    elif not isinstance(top, Node):
        raise ValueError("Argument top nie jest typu Node")
    current_node = top
    while current_node.left is not None:
        current_node = current_node.left
    return current_node


class TestBST(unittest.TestCase):
    def setUp(self):
        self.root = Node(5)
        self.root.insert(Node(1))
        self.root.insert(Node(4))
        self.root.insert(Node(8))
        self.root.insert(Node(11))
        self.root.insert(Node(0))
        self.root.insert(Node(12))
        self.root.insert(Node(-1))

    def test_max(self):
        self.assertEqual(bst_max(self.root).data, 12)

    def test_min(self):
        self.assertEqual(bst_min(self.root).data, -1)
