import unittest

from bst import bst_max, bst_min, Node


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
