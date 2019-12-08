# coding=utf-8
"""Zadanie 8"""


class RandomQueue(object):
    def __init__(self):
        self.queue = []

    def __str__(self):
        return str(self.queue)

    def insert(self, item):
        self.queue.append(item)

    def remove(self):
        from random import randint

        random_num = randint(0, len(self.queue) - 1)
        random_item = self.queue[random_num]
        self.queue.remove(random_item)
        return random_item

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return False  # nie będzie nigdy zapełniona

    def clear(self):
        self.queue = []
