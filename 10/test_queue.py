import unittest

from queue import Queue


class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_put(self):
        self.queue.put(0)
        self.assertEqual(0, self.queue.items[0])

    def test_get(self):
        self.queue.items[0] = 0
        self.queue.tail = 1
        self.assertEqual(0, self.queue.get())

    def test_put_to_full(self):
        queue = self.queue
        for i in range(5):
            queue.put(i)
        self.assertRaises(ValueError, queue.put, 1)

    def test_get_to_empty(self):
        self.assertRaises(ValueError, self.queue.get)

    def test_put_and_get_valid(self):
        self.queue.put(0)
        item = self.queue.get()
        self.assertEqual(0, item)

    def test_queue_type(self):
        expected = [1, 2, 3, 4]
        item_list = []
        for i in range(1, 5):
            self.queue.put(i)
        while not self.queue.is_empty():
            item_list.append(self.queue.get())
        self.assertEqual(item_list, expected)

    def test_is_empty(self):
        self.assertTrue(self.queue.is_empty())
        self.queue.put(2)
        self.queue.get()
        self.assertTrue(self.queue.is_empty())

    def test_is_full(self):
        queue = self.queue
        for i in range(5):
            queue.put(i)
        self.assertTrue(queue.is_full())
