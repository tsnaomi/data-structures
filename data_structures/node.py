class Node:

    def __init__(self, val, prev=None, post=None):
        self.val = val
        self.prev = prev
        self.post = post

    def __repr__(self):
        '''Return the node as a string literal.'''
        return str(self.val)
