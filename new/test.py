import unittest

from linked_list import LinkedList
from stack import Stack


# doubly-linked list
class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.emptyList = LinkedList()
        self.List = LinkedList()

        # populate list with 1, 2, 3, 4
        for i in range(1, 5):
            self.List.append(i)

    def test_tup(self):
        '''Test returning the linked list as a tuple literal.'''
        self.assertEqual(self.emptyList.tup(), ())
        tup = (1, 3.14, 'foo', True)

        for i in tup:
            self.emptyList.append(i)

        self.assertEqual(self.emptyList.tup(), tup)

    def test_repr(self):
        '''Test returning the linked list as a string.'''
        self.assertEqual(repr(self.emptyList), '()')
        tup = (1, 3.14, 'foo', True)

        for i in tup:
            self.emptyList.append(i)

        self.assertEqual(repr(self.emptyList), "(1, 3.14, 'foo', True)")

    def test_insert(self):
        '''Test inserting values at the head of list the list.'''
        for i in range(1, 5):
            self.emptyList.insert(i)

        self.assertEqual(self.emptyList.tup(), (4, 3, 2, 1))

    def test_append(self):
        '''Test appending values at the end of the list.'''
        self.List.append(True)
        self.assertEqual(self.List.tup(), (1, 2, 3, 4, True))

    def test_pop(self):
        '''Test popping off and returning the head of the list.'''
        self.assertEqual(self.List.pop(), 1)
        self.assertEqual(self.List.tup(), (2, 3, 4))
        self.assertEqual(self.List.pop(), 2)
        self.assertEqual(self.List.pop(), 3)
        self.assertEqual(self.List.pop(), 4)
        self.assertEqual(self.List.tup(), ())

        with self.assertRaises(IndexError):
            self.emptyList.pop()

    def test_shift(self):
        '''Test removing and return the tail of the list.'''
        self.assertEqual(self.List.shift(), 4)
        self.assertEqual(self.List.tup(), (1, 2, 3))
        self.assertEqual(self.List.shift(), 3)
        self.assertEqual(self.List.shift(), 2)
        self.assertEqual(self.List.shift(), 1)
        self.assertEqual(self.List.tup(), ())

        with self.assertRaises(IndexError):
            self.emptyList.shift()

    def test_remove(self):
        '''Testing finding and removing values from the list.'''
        for i in range(1, 5):
            self.List.append(i)

        self.List.remove(2)
        self.assertEqual(self.List.tup(), (1, 3, 4, 1, 2, 3, 4))

        with self.assertRaises(ValueError):
            self.List.remove(6)

    def test_size(self):
        '''Test returning the length of the list.'''
        for i in range(100):
            self.emptyList.insert(i)

        self.assertEqual(self.emptyList.size(), 100)

    def test_contains(self):
        '''Test returning T/F for whether the list contains certain values.'''
        self.assertTrue(self.List.contains(2))
        self.assertFalse(self.List.contains(10))


# LIFO
class TestStack(unittest.TestCase):

    def setUp(self):
        self.emptyStack = Stack()
        self.Stack = Stack()

        for i in range(5):
            self.Stack.push(i)

    def test_tup(self):
        '''Test returning the stack as a tuple literal.'''
        self.assertEqual(self.emptyStack.tup(), ())
        tup = (1, 3.14, 'foo', True)

        for i in tup:
            self.emptyStack.push(i)

        self.assertEqual(self.emptyStack.tup(), (True, 'foo', 3.14, 1))

    def test_repr(self):
        '''Test returning the stack as a string.'''
        self.assertEqual(repr(self.emptyStack), '()')
        tup = (1, 3.14, 'foo', True)

        for i in tup:
            self.emptyStack.push(i)

        self.assertEqual(repr(self.emptyStack), "(True, 'foo', 3.14, 1)")

    def test_push(self):
        '''Test pushing items on top of the stack.'''
        self.Stack.push(True)
        self.assertEqual(self.Stack.tup(), (True, 4, 3, 2, 1, 0))

    def test_pop(self):
        '''Test popping off and returning the top of the stack.'''
        self.assertEqual(self.Stack.pop(), 4)
        self.assertEqual(self.Stack.tup(), (3, 2, 1, 0))
        self.assertEqual(self.Stack.pop(), 3)
        self.assertEqual(self.Stack.pop(), 2)
        self.assertEqual(self.Stack.pop(), 1)
        self.assertEqual(self.Stack.pop(), 0)
        self.assertEqual(self.Stack.tup(), ())

        with self.assertRaises(ValueError):
            self.Stack.pop()

    def test_peek(self):
        '''Test seeing the top of the stack w/o modifying it.'''
        self.assertEqual(self.Stack.peek(), 4)

        with self.assertRaises(ValueError):
            self.emptyStack.peek()


if __name__ == '__main__':
    unittest.main()
