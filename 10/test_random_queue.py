import unittest

from random_queue import RandomQueue


class TestRandomQueue(unittest.TestCase):
    def setUp(self):
        self.random_queue = RandomQueue()
        self.random_queue.insert(3)
        self.random_queue.insert(1)
        self.random_queue.insert(3)
        self.random_queue.insert(5)
        self.random_queue.insert(9)

    def test_insert(self):
        random_queue = RandomQueue()
        random_queue.insert(0)
        item = random_queue.remove()
        self.assertEqual(0, item)

    def test_is_empty(self):
        random_queue = RandomQueue()
        self.assertTrue(random_queue.is_empty())

    def test_is_full(self):
        self.assertFalse(self.random_queue.is_full())

    def test_clear(self):
        self.random_queue.clear()
        self.assertTrue(self.random_queue.is_empty())

    def test_remove(self):
        removed_items = []
        item_set = {3, 1, 5, 9}
        while not self.random_queue.is_empty():
            removed_items.append(self.random_queue.remove())
        self.assertTrue(self.random_queue.is_empty())
        self.assertEqual(set(removed_items), item_set)
