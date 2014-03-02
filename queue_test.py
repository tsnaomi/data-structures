#!/usr/bin/env Python

from queue import Queue
import unittest


class TestQueue(unittest.TestCase):
    """  """
    def setUp(self):
        self.queue = Queue()
        self.list1 = [4, 3, 2, 1]
        self.list2 = [3, 2, 1]

    def amass(self, node):
        nodes = []
        while node:
            nodes.insert(0, node.value)
            node = node.next
        return nodes

    def test_enqueue(self):
        for i in range(1, 5):
            self.queue.enqueue(i)
        nodes = self.amass(self.queue.head)
        self.assertEqual(nodes, self.list1)

    def test_dequeue(self):
        for i in range(4):
            self.queue.enqueue(i)
        returned = self.queue.dequeue()
        nodes = self.amass(self.queue.head)
        self.assertEqual(returned, 0)
        self.assertEqual(nodes, self.list2)

    def test_size(self):
        for i in range(10):
            self.queue.enqueue(i)
        self.assertEqual(self.queue.size(), 10)

if __name__ == '__main__':
    unittest.main()
