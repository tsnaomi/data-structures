import unittest

from linked_list import LinkedList


# doubly-linked list
class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.List = LinkedList()
        self.emptyList = LinkedList()

    def test_insert(self):
        #
        for i in range(1, 5):
            self.List.insert(i)

        self.assertEqual(repr(self.List), '[4, 3, 2, 1]')
        self.assertEqual(repr(self.emptyList), '[]')

    def test_append(self):
        #
        for i in range(1, 5):
            self.List.append(i)
        self.emptyList.append(8)

        self.assertEqual(repr(self.List), '[1, 2, 3, 4]')
        self.assertEqual(repr(self.emptyList), '[8]')

    def test_pop(self):
        #
        for i in range(1, 5):
            self.List.insert(i)
        self.assertEqual(self.List.pop(), 4)
        self.assertEqual(repr(self.List), '[3, 2, 1]')
        self.List.pop()
        self.List.pop()
        self.assertEqual(self.List.pop(), 1)
        self.assertEqual(repr(self.List), '[]')
        with self.assertRaises(IndexError):
            self.emptyList.pop()

    def test_shift(self):
        #
        for i in range(1, 3):
            self.List.insert(i)
        self.assertEqual(self.List.shift(), 1)
        self.assertEqual(repr(self.List), '[2]')
        self.assertEqual(self.List.shift(), 2)
        self.assertEqual(repr(self.List), '[]')
        with self.assertRaises(IndexError):
            self.emptyList.shift()

    def test_remove(self):
        #
        for i in range(2):
            for j in range(1, 5):
                self.List.append(j)
        self.List.remove(2)
        self.assertEqual(repr(self.List), '[1, 3, 4, 1, 2, 3, 4]')
        with self.assertRaises(ValueError):
            self.List.remove(6)

    def test_size(self):
        for i in range(10):
            self.List.insert(i)
        self.assertEqual(self.List.size(), 10)

    def test_contains(self):
        for i in range(4):
            self.List.insert(i)
        self.assertTrue(self.List.contains(2))
        self.assertFalse(self.List.contains(4))

    def test_repr(self):
        tup = (1, 3.14, 'foo', True)
        for i in tup:
            self.List.append(i)
        self.assertEqual(self.List._print(), tup)

if __name__ == '__main__':
    unittest.main()
