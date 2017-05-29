from node import Node


# doubly-linked list
class LinkedList:

    def __init__(self):
        self.List = None
        self.end = None
        self.length = 0

    def __repr__(self):
        '''Return the list as a string literal.'''
        return str(tuple(self))

    def __len__(self):
        '''Return the length of the list.'''
        return self.length

    def __iter__(self):
        '''Return an iterator of the list's nodes.'''
        node = self.List

        while node:
            yield node.val
            node = node.post

    def __contains__(self, val):
        '''Return True if the list contains 'val'; otherwise, False.'''
        node = self.List

        while node:
            if node.val == val:
                return True

            node = node.post

        return False

    def size(self):
        '''Return the length of the list.'''
        return len(self)

    def contains(self, val):
        '''Return True if the list contains 'val'; otherwise, False.'''
        return val in self

    def insert(self, val):
        '''Insert 'val' at the head of the list.'''
        node = Node(val)

        try:
            # head = Node(val)
            self.List.prev = node
            node.post = self.List
            self.List = node

        except AttributeError:
            self.List = node
            self.end = node

        self.length += 1

    def append(self, val):
        '''Append 'val' at the end of the list.'''
        node = Node(val)

        try:
            node.prev = self.end
            self.end = node
            self.end.prev.post = node

        except AttributeError:
            self.List = node
            self.end = node

        self.length += 1

    def shift(self):
        '''Remove and return the value at the head of the list.'''
        try:
            val = self.List.val
            self.List = self.List.post
            self.length -= 1

            try:
                self.List.prev = None

            except AttributeError:
                self.end = None

            return val

        except AttributeError:
            raise IndexError('Empty lists can\'t shift. Welp.')

    def pop(self):
        '''Pop off and return the value at the tail of the list.'''
        try:
            val = self.end.val
            self.end = self.end.prev
            self.length -= 1

            try:
                self.end.post = None

            except AttributeError:
                self.List = None

            return val

        except AttributeError:
            raise IndexError('Empty lists can\'t pop. Welp.')

    def remove(self, val):
        '''Remove the first instance of 'val' found in the list.'''
        node = self.List

        while node:
            if node.val == val:
                node.post.prev = node.prev
                node.prev.post = node.post
                self.length -= 1
                break

            node = node.post

        else:
            raise ValueError('Can\'t delete something that ain\'t there.')
