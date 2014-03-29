#!usr/bin/env Python

from random import randint

# inspiration: github.com/markcharyk


class Tree(object):
    ''' A binary search tree data structure '''
    def __init__(self, value=None):
        if isinstance(value, (int, float)) or value is None:
            self.value = value
            self.left = None if self.value is None else Tree()
            self.right = None if self.value is None else Tree()
        else:
            raise TypeError('Accio interger! Accio float!')

    def insert(self, x):
        ''' Inserts a value (x) into the tree. '''
        if isinstance(x, (int, float)):
            if self.value is None:
                self.value, self.left, self.right = x, Tree(), Tree()
            elif self.value > x:
                self.left.insert(x)
            elif self.value < x:
                self.right.insert(x)
        else:
            raise TypeError('Accio integer! Accio float!')

    def contains(self, x):
        ''' Returns True if the specified value (x) is in the tree. '''
        if isinstance(x, (int, float)):
            node = self
            while node.value != x and node.value is not None:
                node = node.left if node.value > x else node.right
            return node.value == x
        raise TypeError('Accio interger! Accio float!')

    def size(self):
        ''' Returns the number of nodes the tree contains. '''
        if self.value is None:
            return 0
        return 1 + self.left.size() + self.right.size()
        # return 0 if self.value is None \
        #     else 1 + self.left.size() + self.right.size()

    def depth(self):
        ''' Returns the number of levels the tree contains. '''
        if self.value is None:
            return 0
        return 1 + max(self.left.depth(), self.right.depth())
        # return 0 if self.value is None \
        #     else 1 + max(self.left.depth(), self.right.depth())

    def balance(self):
        ''' Returns an integer representing the balance of the tree.
            A negative number indicates a left-heavy tree.
            A positive number indicates a righ-heavy tree.
            0 indicates a lovely, perfectly balanced tree. '''
        if self.value is None:
            return 0
        return self.right.depth() - self.left.depth()
        # return 0 if self.value is None \
        #     else self.right.depth() - self.left.depth()

    def in_order(self):
        ''' Traverses the values in the tree one at a time in order '''
        if self.left is not None:
            for value in self.left.in_order():
                yield value
        if self.value is not None:
            yield self.value
        if self.right is not None:
            for value in self.right.in_order():
                yield value

    def pre_order(self):
        ''' Traverses the values in the tree one at a time, yielding parents
            first '''
        if self.value is not None:
            yield self.value
        if self.left is not None:
            for value in self.left.pre_order():
                yield value
        if self.right is not None:
            for value in self.right.pre_order():
                yield value

    def post_order(self):
        ''' Traverses the values in the tree one at a time, yielding children
            first '''
        if self.left is not None:
            for value in self.left.post_order():
                yield value
        if self.right is not None:
            for value in self.right.post_order():
                yield value
        if self.value is not None:
            yield self.value

    def breadth_first(self):  # collaborator: github.com/risingmoon
        ''' Traverses the values in the tree beginning with the root and going
            down level by level, yielding values left to right '''
        pqueue = [] if self.value is None else [self]  # pqueue is pseudo-queue
        while pqueue:
            node = pqueue.pop(0)
            if node.left and node.left.value is not None:
                pqueue.append(node.left)
            if node.right and node.right.value is not None:
                pqueue.append(node.right)
            yield node.value

    def get_dot(self):
        ''' Returns the tree with the root 'self' as a dot graph for
            visualization. '''
        return 'digraph G{\n%s}' % ('' if self.value is None else (
            '\t%s;\n%s\n' % (
                self.value,
                '\n'.join(self._get_dot())
            )
        ))

    def _get_dot(self):
        ''' Recursively prepares a dot graph entry for a node. '''
        if self.left is not None:
            yield '\t%s -> %s;' % (self.value, self.left.value)
            for i in self.left._get_dot():
                yield i
        elif self.right is not None:
            r = randint(0, 1e9)
            yield '\tnull%s [shape=point];' % r
            yield '\t%s -> null%s;' % (self.value, r)
        if self.right is not None:
            yield '\t%s -> %s;' % (self.value, self.right.value)
            for i in self.right._get_dot():
                yield i
        elif self.left is not None:
            r = randint(0, 1e9)
            yield '\tnull%s [shape=point];' % r
            yield '\t%s -> null%s;' % (self.value, r)
