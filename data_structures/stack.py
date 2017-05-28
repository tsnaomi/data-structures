class Node:

    def __init__(self, val, post=None):
        self.val = val
        self.post = post

    def __repr__(self):
        '''Return the node as a string literal.'''
        return str(self.val)


# LIFO: Last in, First out
class Stack:

    def __init__(self):
        self.Stack = None
        self.length = 0

    def __repr__(self):
        '''Return the stack as a string literal.'''
        return str(tuple(self))

    def __len__(self):
        '''Return the size of the stack.'''
        return self.length

    def __iter__(self):
        '''Return an iterator of the stack's nodes.'''
        node = self.Stack

        while node:
            yield node.val
            node = node.post

    def push(self, val):
        '''Add 'val' to the top of the stack.'''
        self.Stack = Node(val, post=self.Stack)
        self.length += 1

    def pop(self):
        '''Pop off and return the top item of the stack.'''
        try:
            val = self.Stack.val
            self.Stack = self.Stack.post
            self.length -= 1

            return val

        except AttributeError:
            raise ValueError('Ain\'t no pancakes in this stack to pop.')

    def peek(self):
        '''Return the top (pancake) of the stack w/o modifying the stack.'''
        try:
            return self.Stack.val

        except AttributeError:
            raise ValueError('Ain\'t no pancakes in this stack.')

    def size(self):
        '''Return the size of the stack.'''
        return len(self)
