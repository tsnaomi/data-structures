# coding=utf-8


class Node:

    def __init__(self, val, post=None):
        self.val = val
        self.post = post

    def __repr__(self):
        return str(self.val)


# LIFO: Last in, First out
class Stack:

    def __init__(self):
        self.Stack = None

    def __repr__(self):
        return str(self.tup())

    def tup(self):
        '''Return the stack as a tuple literal, from top to bottom.'''
        nodes = tuple()
        node = self.Stack

        while node:
            nodes += (node.val, )
            node = node.post

        return nodes

    def push(self, val):
        '''Add 'val' to the top of the stack.'''
        self.Stack = Node(val, post=self.Stack)

    def pop(self):
        '''Pop off and return the top item of the stack.'''
        try:
            val = self.Stack.val
            self.Stack = self.Stack.post

            return val

        except AttributeError:
            raise ValueError('Ain\'t no pancakes in this stack to pop.')

    def peek(self):
        '''Return the top (pancake) of the stack w/o modifying the stack.'''
        try:
            return self.Stack.val

        except AttributeError:
            raise ValueError('Ain\'t no pancakes in this stack.')
