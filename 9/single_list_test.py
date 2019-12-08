import unittest

from single_list import SingleList, Node


class TestSingleList(unittest.TestCase):
    def setUp(self):
        self.first_list = SingleList()
        self.second_list = SingleList()
        self.first_list.insert_head(Node(3))
        self.first_list.insert_head(Node(5))
        self.first_list.insert_tail(Node(7))
        self.second_list.insert_head(Node(1))
        self.second_list.insert_tail(Node(11))

    def test_remove_tail(self):
        tail = self.first_list.remove_tail()
        self.assertEqual(tail.data, 7)

    def test_merge(self):
        count = self.first_list.count() + self.second_list.count()
        self.first_list.merge(self.second_list)
        self.assertEqual(self.first_list.count(), count)

    def test_clear(self):
        self.first_list.clear()
        self.assertEqual(self.first_list.count(), 0)
