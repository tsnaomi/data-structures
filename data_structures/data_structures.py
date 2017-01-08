# !/usr/bin/env Python

from random import randint

# TODO: rename arguments, clean docstrings


# a node in a singly-linked list, stack, or queue
class Node(object):
    def __init__(self, value=None, node=None):
        self.value = value
        self.next = node

    def __str__(self):
        return str(self.value)


# a singly-linked list
class LinkedList(object):  # TODO: remove() is broken

    def __init__(self):
        self.head = None

    def __str__(self):
        node = self.head
        nodes = []
        while node:
            nodes.append(str(node))
            node = node.next
        return '(%s)' % ', '.join(nodes)  # return str(tuple(nodes))

    def insert(self, x):
        '''Insert item at the head of the list.'''
        self.head = Node(x, self.head)

    def pop(self):
        '''Pop the first item off the head of the list and returns it.'''
        node = self.head
        if node:
            self.head = self.head.next
            return node.value
        raise ValueError('LinkedList is empty')

    def size(self):
        '''Return the number of items in the list.'''
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
        return count

    def search(self, x):
        '''Search for a specified item in the list and return its node.'''
        node = self.head
        while node:
            if node.value == x:
                return node
            node = node.next

    def remove(self, x):
        '''Remove a specified node from the list.'''
        node = self.head
        if node:
            if node.value == x:
                self.head = node.next
            else:
                while node:
                    if node.value == x:
                        previous.next = node.next
                        return None
                    previous = node
                    node = node.next
        raise ValueError("LinkedList is empty")

    def PRINT(self):
        '''Print a tuple literal of the nodes in the list.'''
        return self.__str__()


# a Last-In-First-Out data structure
class Stack(object):

    def __init__(self):
        self.node = None

    def push(self, x):
        '''Add a specified node to the top of the stack.'''
        self.node = Node(x, self.node)

    def pop(self):
        '''Remove the node at the top of the stack.'''
        if self.node:
            x, self.node = self.node.value, self.node.next
            return x
        raise ValueError('''You have no pancakes to pop. Now, please pass the
             syrup?''')


# a First-In-First-Out data structure
class Queue(object):

    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, x):
        '''Add an item to the queue.'''
        if self.head:
            self.tail.next = Node(x)
            self.tail = self.tail.next
        else:
            self.tail = Node(x)
            self.head = self.tail

    def dequeue(self):
        '''Remove the first-in item from the queue and returns it.'''
        if self.head:
            if self.head == self.tail:
                self.tail = self.tail.next
            node, self.head = self.head, self.head.next
            return node.value
        raise ValueError("Empty queue!")

    def size(self):
        '''Return the size of the queue.'''
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
        return count


class HashTable(LinkedList):

    def __init__(self, num=32):
        self.num = num
        LinkedList.__init__(self)
        for x in range(num):
            self.insert(LinkedList())

    def hash(self, key):
        '''Hash the provided key.'''
        if isinstance(key, str):
            count = 0
            for character in key:
                count += ord(character)
            return count % self.num
        raise TypeError('Strings only please.')

    def set(self, key, value):
        '''Store the key/value pair.'''
        container = self.head
        for num in range(self.hash(key)):
            container = container.next
        node = container.value.head
        while node:
            if node.value[0] == key:
                node.value = (key, value)
            node = node.next
        if container.value.search((key, value)) is None:
            container.value.insert((key, value))

    def get(self, key):
        '''Return the value stored with the provided key.'''
        container = self.head
        for num in range(self.hash(key)):
            container = container.next
        node = container.value.head
        while node:
            if node.value[0] == key:
                return node.value[1]
            node = node.next
        raise KeyError('My apologies, there\'s no such key in this HashTable.')


# a binary search tree
class BSTree(object):  # TODO: delete() is broken (revise tests)

    def __init__(self, value=None):
        if isinstance(value, (int, float)) or value is None:
            self.value = value
            self.left = None if self.value is None else Tree()
            self.right = None if self.value is None else Tree()
        else:
            raise TypeError('Accio interger! Accio float!')

    def insert(self, x):
        '''Insert a value (x) into the tree.'''
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
        '''Return True if the specified value (x) is in the tree.'''
        if isinstance(x, (int, float)):
            node = self
            while node.value != x and node.value is not None:
                node = node.left if node.value > x else node.right
            return node.value == x
        raise TypeError('Accio interger! Accio float!')

    def size(self):
        '''Return the number of nodes the tree contains.'''
        if self.value is None:
            return 0
        return 1 + self.left.size() + self.right.size()

    def depth(self):
        '''Return the number of levels the tree contains.'''
        if self.value is None:
            return 0
        return 1 + max(self.left.depth(), self.right.depth())

    def balance(self):
        '''Return an integer representing the balance of the tree.
        A negative number indicates a left-heavy tree.
        A positive number indicates a righ-heavy tree.
        0 indicates a lovely, perfectly balanced tree.'''
        if self.value is None:
            return 0
        return self.right.depth() - self.left.depth()

    def in_order(self):
        '''Traverse the values in the tree one at a time in order.'''
        if self.left is not None:
            for value in self.left.in_order():
                yield value
        if self.value is not None:
            yield self.value
        if self.right is not None:
            for value in self.right.in_order():
                yield value

    def pre_order(self):
        '''Traverse the values in the tree one at a time, yielding parents
        first. '''
        if self.value is not None:
            yield self.value
        if self.left is not None:
            for value in self.left.pre_order():
                yield value
        if self.right is not None:
            for value in self.right.pre_order():
                yield value

    def post_order(self):
        '''Traverse the values in the tree one at a time, yielding children
        first. '''
        if self.left is not None:
            for value in self.left.post_order():
                yield value
        if self.right is not None:
            for value in self.right.post_order():
                yield value
        if self.value is not None:
            yield self.value

    def breadth_first(self):
        '''Traverse the values in the tree beginning with the root and going
        down level by level, yielding values left to right.'''
        pqueue = [] if self.value is None else [self]  # pqueue is pseudo-queue
        while pqueue:
            node = pqueue.pop(0)
            if node.left and node.left.value is not None:
                pqueue.append(node.left)
            if node.right and node.right.value is not None:
                pqueue.append(node.right)
            yield node.value

    def delete(self, x):
        '''Delete the specified value (x) from the tree if present.'''
        if isinstance(x, (int, float)) and self.contains(x):
            node, prev = self, self
            while node.value != x:
                prev = node
                node = node.left if node.value > x else node.right
            DELETE = node
            if node.left.value is None and node.right.value is None:
                if prev.left.value == DELETE.value:
                    prev.left = Tree()
                else:
                    prev.right = Tree()
            else:
                if node.balance() <= 0:
                    if node.left.value is not None:
                        self._delete(prev, node, DELETE, "left", "right")
                    else:
                        prev.right = DELETE.right
                else:
                    if node.right.value is not None:
                        self._delete(prev, node, DELETE, "right", "left")
                    else:
                        prev.left = DELETE.left

    def _delete(self, prev, node, DELETE, l1, l2):
        '''Help delete() delete things. '''
        node = getattr(node, l1)
        if getattr(node, l2).value is not None:
            if prev != DELETE and node.balance() == 0:
                if prev.left.value == DELETE.value:
                    prev.left = node
                elif prev.right.value == DELETE.value:
                    prev.right = node
            else:
                while getattr(node, l2).value is not None:
                    prev = node
                    node = getattr(node, l2)
                DELETE.value = node.value
                setattr(prev, l2, Tree() if getattr(node, l1).value is None
                        else getattr(node, l1))
        else:
            DELETE.value, DELETE.right = node.value, node.right

    def get_dot(self):
        '''Visualize the tree with the root 'self' as a dot graph.'''
        return 'digraph G{\n%s}' % ('' if self.value is None else (
            '\t%s;\n%s\n' % (
                self.value,
                '\n'.join(self._get_dot())
            )
        ))

    def _get_dot(self):
        '''Recursively prepare a dot graph entry for a node.'''
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
