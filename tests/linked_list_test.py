#!/usr/bin/env Python

from data_structures.linked_list import LinkedList
import unittest


class TestSinglyLinkedList(unittest.TestCase):
    """  """
    def setUp(self):
        self.foo = LinkedList()
        self.list1 = '(4, 3, 2, 1)'
        self.list2 = '(3, 2, 1)'
        self.list3 = '(4, 2, 1, 0)'
        self.list4 = "('bacon', 3.14, True, 4, 3, 2, 1)"

    def test_insert(self):
        for i in range(1, 5):
            self.foo.insert(i)
        self.assertEqual(self.foo.__str__(), self.list1)

    def test_pop(self):
        for i in range(1, 5):
            self.foo.insert(i)
        self.assertEqual(self.foo.pop(), 4)
        self.assertEqual(self.foo.__str__(), self.list2)

    def test_size(self):
        for i in range(10):
            self.foo.insert(i)
        self.assertEqual(self.foo.size(), 10)

    def test_search(self):
        for i in range(4):
            self.foo.insert(i)
        self.assertEqual(self.foo.search(2).value, 2)

    def test_remove(self):
        for i in range(5):
            self.foo.insert(i)
        self.foo.remove(3)
        self.assertEqual(self.foo.__str__(), self.list3)

    def test_PRINT(self):
        for i in range(1, 5):
            self.foo.insert(i)
        self.foo.insert(True)
        self.foo.insert(3.14)
        self.foo.insert("bacon")
        self.assertEqual(self.foo.PRINT(), self.list4)

if __name__ == '__main__':
    unittest.main()
