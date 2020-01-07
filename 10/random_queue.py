# coding=utf-8
"""Zadanie 8"""
from random import randint


class RandomQueue(object):
    def __init__(self):
        self.queue = []

    def __str__(self):
        return str(self.queue)

    def insert(self, item):
        self.queue.append(item)

    def remove(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        index = randint(0, len(self.queue) - 1)
        element = self.queue[index]
        self.queue[index] = self.queue[-1]
        del self.queue[-1]
        return element

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return False  # nie będzie nigdy zapełniona

    def clear(self):
        self.queue = []
