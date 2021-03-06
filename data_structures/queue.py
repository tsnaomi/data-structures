from node import Node


# FIFO: First in, First out
class Queue:

    def __init__(self):
        self.Queue = None
        self.end = None
        self.length = 0

    def __repr__(self):
        '''Return the queue as a string literal.'''
        return str(tuple(self))

    def __len__(self):
        '''Return the size of the queue.'''
        return self.length

    def __iter__(self):
        '''Return an iterator of the queue's nodes.'''
        node = self.Queue

        while node:
            yield node.val
            node = node.post

    def enqueue(self, val):
        '''Add 'val' to the queue.'''
        node = Node(val)

        if self.Queue:
            node.prev = self.end
            self.end = node
            self.end.prev.post = node

        else:
            self.Queue = node
            self.end = node

        self.length += 1

    def dequeue(self):
        '''Remove and return the first item in the queue.'''
        try:
            val = self.Queue.val
            self.Queue = self.Queue.post
            self.length -= 1

            try:
                self.Queue.prev = None

            except AttributeError:
                self.end = None

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
        return len(self)
