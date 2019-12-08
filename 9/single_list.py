# coding=utf-8
"""Zadanie 1"""


class Node(object):
    """Klasa reprezentująca węzeł listy jednokierunkowej."""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)  # bardzo ogólnie

    def get_data(self):
        return self.data


class SingleList(object):
    """Klasa reprezentująca całą listę jednokierunkową."""

    def __init__(self):
        self.length = 0  # nie trzeba obliczać za każdym razem
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.length == 0

    def count(self):  # tworzymy interfejs do odczytu
        return self.length

    def insert_head(self, node):
        if self.length == 0:
            self.head = self.tail = node
        else:  # dajemy na koniec listy
            node.next = self.head
            self.head = node
        self.length += 1

    def insert_tail(self, node):  # klasy O(N)
        if self.length == 0:
            self.head = self.tail = node
        else:  # dajemy na koniec listy
            self.tail.next = node
            self.tail = node
        self.length += 1

    def remove_head(self):  # klasy O(1)
        if self.length == 0:
            raise ValueError("pusta lista")
        node = self.head
        if self.head == self.tail:  # self.length == 1
            self.head = self.tail = None
        else:
            self.head = self.head.next
        node.next = None  # czyszczenie łącza
        self.length -= 1
        return node  # zwracamy usuwany node

    def remove_tail(self):
        """ Zwraca cały węzeł, skraca listę.
        Dla pustej listy rzuca wyjątek ValueError.
        klasy O(N)"""
        if self.length == 0:
            raise ValueError("pusta lista")
        tail = self.tail
        if self.head == self.tail:  # length == 1
            self.head = self.tail = None
        else:
            current_node = self.head
            while current_node.next != tail:
                current_node = current_node.next
            self.tail = current_node
            self.tail.next = None
        self.length -= 1
        return tail

    def merge(self, other):
        """ Węzły z listy other są przepinane do listy self na jej koniec, klasy O(1) """
        if self.length == 0:
            self.head, self.tail, self.length = other.head, other.tail, other.length
        else:
            self.tail.next = other.head
            self.length += other.length

    def clear(self):
        """czyszczenie listy, klasy O(N)"""
        while self.length != 0:
            self.remove_head()
