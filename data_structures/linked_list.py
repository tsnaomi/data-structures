class Node:

    def __init__(self, val, prev=None, post=None):
        self.val = val
        self.prev = prev
        self.post = post

    def __repr__(self):
        return str(self.val)


# doubly-linked list
class LinkedList:

    def __init__(self):
        self.List = None

    def __repr__(self):
        return str(self.tup())

    def tup(self):
        '''Return the linked list as a tuple literal.'''
        nodes = tuple()
        node = self.List

        while node:
            nodes += (node.val, )
            node = node.post

        return nodes

    def insert(self, val):
        '''Insert 'val' at the head of the list.'''
        try:
            head = Node(val)
            self.List.prev = head
            head.post = self.List
            self.List = head

        except AttributeError:
            self.List = Node(val)

    def append(self, val):
        '''Append 'val' at the end of the list.'''
        node = self.List

        while node:
            if node.post:
                node = node.post

            else:
                tail = Node(val)
                tail.prev = node
                node.post = tail
                break

        else:
            self.List = Node(val)

    def pop(self):
        '''Pop off and return the value at the head of the list.'''
        try:
            val = self.List.val
            self.List = self.List.post

            return val

        except AttributeError:
            raise IndexError('Empty lists can\'t pop. Welp.')

    def shift(self):
        '''Remove and return the value at the tail of the list.'''
        node = self.List

        while node:
            if node.post:
                node = node.post

            else:
                try:
                    node.prev.post = None

                except AttributeError:
                    self.List = None

                return node.val

        raise IndexError('Empty lists can\'t shift. Darn.')

    def remove(self, val):
        '''Remove the first instance of 'val' found in the list.'''
        node = self.List

        while node:
            if node.val == val:
                node.post.prev = node.prev
                node.prev.post = node.post
                break

            node = node.post

        else:
            raise ValueError('Can\'t delete something that ain\'t there.')

    def size(self):
        '''Return the length of the list.'''
        n = 0
        node = self.List

        while node:
            n += 1
            node = node.post

        return n

    def contains(self, val):
        '''Return True if the list contains 'val'; otherwise, False.'''
        node = self.List

        while node:
            if node.val == val:
                return True

            node = node.post

        return False
