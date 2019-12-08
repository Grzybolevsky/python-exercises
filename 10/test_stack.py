import unittest

from stack import Stack


class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_push(self):
        self.stack.push(0)
        self.assertEqual(self.stack.items[0], 0)

    def test_pop(self):
        self.stack.items[0] = 0
        self.stack.n = 1
        self.assertEqual(self.stack.pop(), 0)

    def test_push_pop_valid(self):
        self.stack.push(1)
        self.assertEqual(self.stack.pop(), 1)

    def test_pop_empty(self):
        self.assertRaises(ValueError, self.stack.pop)

    def test_pop_full(self):
        stack = Stack(1)
        stack.push(0)
        self.assertRaises(ValueError, stack.push, 1)

    def test_is_empty(self):
        self.assertTrue(self.stack.is_empty())

        stack = Stack(4)
        for i in range(4):
            stack.push(i)
        for i in range(4):
            stack.pop()
        self.assertTrue(stack.is_empty())

    def test_is_full(self):
        stack = Stack(5)
        for i in range(5):
            stack.push(i)
        self.assertTrue(stack.is_full())
