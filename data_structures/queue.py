class Node:

    def __init__(self, val, post=None):
        self.val = val
        self.post = post

    def __repr__(self):
        '''Return the node as a string literal.'''
        return str(self.val)


# FIFO: First in, First out
class Queue:

    def __init__(self):
        self.Queue = None
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

        self.length += 1

    def dequeue(self):
        '''Remove and return the first item in the queue.'''
        try:
            val = self.Queue.val
            self.Queue = self.Queue.post
            self.length -= 1

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
