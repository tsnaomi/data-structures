# coding=utf-8

# DOUBLY-LINKED LIST
#   - insert(val) will insert the value 'val' at the head of the list
#   - append(val) will append the value 'val' at the tail of the list
#   - pop() will pop the first value off the head of the list and return it
#   - shift() will remove the last value from the tail of the list and return
#     it
#   - remove(val) will remove the first instance of 'val' found in the list,
#     starting from the head. If 'val' is not present, it will raise an
#     appropriate Python exception.
#   - size() will return the length of the list
#   - search(val) will return the node containing 'val' in the list, if
#     present, else None --- CONTAINS
#   - print() will print the list represented as a Python tuple literal:
#     "(12, 'sam', 37, 'tango')"
#     bonus if you can make it so that the list appears this way on its own
#     (remember special methods).


class Node:

    def __init__(self, val, prev=None, post=None):
        self.val = val
        self.prev = prev
        self.post = post

    def __repr__(self):
        return str(self.val)


class LinkedList:

    def __init__(self):
        self.List = None

    def __repr__(self):
        #
        nodes = ''
        node = self.List

        while node:
            nodes += str(node.val) + ', '
            node = node.post

        try:
            return '[' + nodes[:-2] + ']'

        except IndexError:
            return '[]'

    def _print(self):
        #
        nodes = tuple()
        node = self.List

        while node:
            nodes += (node.val, )
            node = node.post

        return nodes

    def insert(self, val):
        #
        try:
            head = Node(val)
            self.List.prev = head
            head.post = self.List
            self.List = head

        except AttributeError:
            self.List = Node(val)

    def append(self, val):  # simplify
        #
        def _append(val, node=self.List):
            if node:
                if node.post:
                    _append(val, node.post)

                else:
                    tail = Node(val)
                    tail.prev = node
                    node.post = tail

            else:
                self.List = Node(val)

        _append(val)

    def pop(self):
        #
        try:
            val = self.List.val
            self.List = self.List.post

            return val

        except AttributeError:
            raise IndexError('Empty lists can\'t pop. Welp.')

    def shift(self):  # simplify
        #
        def _shift(node=self.List):
            if node.post:
                return _shift(node=node.post)

            else:
                val = node.val

                try:
                    node.prev.post = None

                except AttributeError:
                    self.List = None

                return val

        if self.List:
            return _shift(self.List)

        raise IndexError('Empty lists can\'t shift. Darn.')

    def remove(self, val):  # simplify
        #
        def _remove(node):
            if node.val == val:
                node.post.prev = node.prev
                node.prev.post = node.post

            elif node.post:
                _remove(node.post)

            else:
                raise ValueError('Can\'t delete something that ain\'t there.')

        if self.List:
            _remove(self.List)

        else:
            raise ValueError('Can\'t delete something that ain\'t there.')

    def size(self):
        n = 0
        node = self.List

        while node:
            n += 1
            node = node.post

        return n

    def contains(self, val):  # simplify

        def _search(node):
            if node.val != val:
                if node.post:
                    return _search(node.post)

                else:
                    return False
            else:
                return True

        if self.List:
            return _search(self.List)

        return False
