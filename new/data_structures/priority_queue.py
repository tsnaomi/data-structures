# coding='utf-8'

# .insert(item): inserts an item into the queue.
# .pop(): removes the most important item from the queue.
# .peek(): returns the most important item without removing it from the queue.

import unittest


class Node:

    def __init__(self, val, priority=1, prev=None, post=None):
        self.val = val
        self.priority = priority  # 1 = hiest priority
        self.prev = prev
        self.post = post

    def __repr__(self):
        return '%s (%s)' % (str(self.val), str(self.priority))


# FIFO: First in, First out
class PriorityQueue:

    def __init__(self):
        self.Queue = None

    def __repr__(self):
        return str(self.tup())

    def tup(self):
        '''Return the queue as a tuple literal, from first to last.'''
        nodes = tuple()
        node = self.Queue

        while node:
            nodes += (node.val, )
            node = node.post

        return nodes

    def enqueue(self, val):
        '''Add 'val' to the front of the queue.'''
        node = self.Queue

        while node:
            if node.post:
                node = node.post

            else:
                node.post = Node(val)
                break

        else:
            self.Queue = Node(val)

    def dequeue(self):
        '''Remove and return the first item in the queue.'''
        try:
            val = self.Queue.val
            self.Queue = self.Queue.post

            return val

        except AttributeError:
            raise ValueError('This queue be empty!')

    def peek(self):
        '''Return the the first item in the queue w/o modifying the queue.'''
        try:
            return self.Queue.val

        except AttributeError:
            raise ValueError('This queue be empty!')

    def size(self):
        '''Return the size of the queue.'''
        n = 0
        node = self.Queue

        while node:
            n += 1
            node = node.post

        return n


class TestPriorityQueue(unittest.TestCase):

    def setUp(self):
        self.emptyQueue = PriorityQueue()
        self.Queue = PriorityQueue()

        items = [(10, 2), (9, 1), (8, 1), (4, 2), (3, 3), (4, 3), (10, 1)]

        for val, priority in items:
            self.Queue.insert(val, priority)

    def test_insert(self):
        '''Test inserting items into the priority queue.'''
        expected = [(9, 1), (10, 2), (8, 1), (4, 2), (3, 3), (4, 3), (10, 1)]
        self.assertEqual(self.Queue.queue, expected)

        self.Queue.insert(True, 1)
        expected = [(9, 1), (10, 2), (8, 1), (4, 2), (3, 3), (4, 3), (10, 1)]
        self.assertEqual(self.Queue.queue, expected)

        self.Queue.enqueue(True)
        self.assertEqual(self.Queue.tup(), (0, 1, 2, 3, 4, True))

    def test_pop(self):
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
