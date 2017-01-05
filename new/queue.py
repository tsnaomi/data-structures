# coding='utf-8'


class Node:

    def __init__(self, val, post=None):
        self.val = val
        self.post = post

    def __repr__(self):
        return str(self.val)


# FIFO: First in, First out
class Queue:

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
