import unittest

from linked_list import LinkedList
from stack import Stack
from queue import Queue
from binary_heap import BinaryHeap


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
        '''Test peeking at the top of the stack w/o modifying the stack.'''
        self.assertEqual(self.Stack.peek(), 4)

        with self.assertRaises(ValueError):
            self.emptyStack.peek()

    def test_size(self):
        '''Test returning the size of the stack.'''
        for i in range(100):
            self.emptyStack.push(i)

        self.assertEqual(self.emptyStack.size(), 100)


# FIFO
class TestQueue(unittest.TestCase):

    def setUp(self):
        self.emptyQueue = Queue()
        self.Queue = Queue()

        for i in range(5):
            self.Queue.enqueue(i)

    def test_tup(self):
        '''Test returning the queue as a tuple literal.'''
        self.assertEqual(self.emptyQueue.tup(), ())
        tup = (1, 3.14, 'foo', True)

        for i in tup:
            self.emptyQueue.enqueue(i)

        self.assertEqual(self.emptyQueue.tup(), tup)

    def test_repr(self):
        '''Test returning the queue as a string.'''
        self.assertEqual(repr(self.emptyQueue), '()')
        tup = (1, 3.14, 'foo', True)

        for i in tup:
            self.emptyQueue.enqueue(i)

        self.assertEqual(repr(self.emptyQueue), "(1, 3.14, 'foo', True)")

    def test_enqueue(self):
        '''Test adding items to the front of the queue.'''
        self.Queue.enqueue(True)
        self.assertEqual(self.Queue.tup(), (0, 1, 2, 3, 4, True))

    def test_dequeue(self):
        '''Test removing items from the front of the queue.'''
        self.assertEqual(self.Queue.dequeue(), 0)
        self.assertEqual(self.Queue.tup(), (1, 2, 3, 4))
        self.assertEqual(self.Queue.dequeue(), 1)
        self.assertEqual(self.Queue.dequeue(), 2)
        self.assertEqual(self.Queue.dequeue(), 3)
        self.assertEqual(self.Queue.dequeue(), 4)
        self.assertEqual(self.Queue.tup(), ())

        with self.assertRaises(ValueError):
            self.Queue.dequeue()

    def test_peek(self):
        '''Test peeking at the first enqueued item w/o modifying the queue.'''
        self.assertEqual(self.Queue.peek(), 0)

        with self.assertRaises(ValueError):
            self.emptyQueue.peek()

    def test_size(self):
        '''Test returning the size of the queue.'''
        for i in range(100):
            self.emptyQueue.enqueue(i)

        self.assertEqual(self.emptyQueue.size(), 100)


class TestBinaryHeap(unittest.TestCase):

    def setUp(self):
        # min heap
        self.minHeap = BinaryHeap(Min=True, iterable=[0, 2, 4, 6, 8])

        # max heap
        self.maxHeap = BinaryHeap(Min=False, iterable=[0, 2, 4, 6, 8])

    def test_push(self):
        '''Test pushing items into a binary heap.'''
        # min heap
        self.assertEqual(self.minHeap.Heap, [0, 2, 4, 6, 8])
        self.minHeap.push(3)
        self.assertEqual(self.minHeap.Heap, [0, 2, 3, 6, 8, 4])
        self.minHeap.push(-1)
        self.assertEqual(self.minHeap.Heap, [-1, 2, 0, 6, 8, 4, 3])
        self.minHeap.push(-1)
        self.assertEqual(self.minHeap.Heap, [-1, -1, 0, 2, 8, 4, 3, 6])

        # max heap (assuming, when instantiating a heap with an iterable, the
        # iterable's items are pushed one-by-one)
        self.assertEqual(self.maxHeap.Heap, [8, 6, 2, 0, 4])
        self.maxHeap.push(5)
        self.assertEqual(self.maxHeap.Heap, [8, 6, 5, 0, 4, 2])
        self.maxHeap.push(9)
        self.assertEqual(self.maxHeap.Heap, [9, 6, 8, 0, 4, 2, 5])
        self.maxHeap.push(8)
        self.assertEqual(self.maxHeap.Heap, [9, 8, 8, 6, 4, 2, 5, 0])

    def test_pop(self):
        '''Test popping off and returning the top items in a binary heap.'''
        # min heap
        self.assertEqual(self.minHeap.pop(), 0)
        self.assertEqual(self.minHeap.Heap, [2, 6, 4, 8])
        self.assertEqual(self.minHeap.pop(), 2)
        self.assertEqual(self.minHeap.Heap, [4, 6, 8])
        self.assertEqual(self.minHeap.pop(), 4)
        self.assertEqual(self.minHeap.Heap, [6, 8])
        self.assertEqual(self.minHeap.pop(), 6)
        self.assertEqual(self.minHeap.Heap, [8])
        self.assertEqual(self.minHeap.pop(), 8)
        self.assertEqual(self.minHeap.Heap, [])

        with self.assertRaises(ValueError):
            self.minHeap.pop()

        # max heap
        self.assertEqual(self.maxHeap.pop(), 8)
        self.assertEqual(self.maxHeap.Heap, [6, 4, 2, 0])
        self.assertEqual(self.maxHeap.pop(), 6)
        self.assertEqual(self.maxHeap.Heap, [4, 0, 2])
        self.assertEqual(self.maxHeap.pop(), 4)
        self.assertEqual(self.maxHeap.Heap, [2, 0])
        self.assertEqual(self.maxHeap.pop(), 2)
        self.assertEqual(self.maxHeap.Heap, [0])
        self.assertEqual(self.maxHeap.pop(), 0)
        self.assertEqual(self.maxHeap.Heap, [])

        with self.assertRaises(ValueError):
            self.minHeap.pop()


if __name__ == '__main__':
    unittest.main()
