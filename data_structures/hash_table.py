from linked_list import LinkedList


class HashTable(LinkedList):

    def __init__(self, bins=32):
        self.bins = 32
        LinkedList.__init__(self)

        # HashTable is a linked list, where every item in the table is also
        # a linked list (i.e., a linked list of linked lists)
        for n in range(bins):
            self.insert(LinkedList())

    def hash(self, key):
        '''Hash 'key'.'''
        try:
            return sum(ord(i) for i in key) % self.bins

        except TypeError:
            raise TypeError('Keys must be strings.')

    def set(self, key, value):
        '''Store the 'key'/'value' pair in the table.'''
        node = self.List

        # find the correct bin
        for n in range(self.hash(key)):
            node = node.post

        # insert the k, v pair if it is not already in the bin
        if not node.val.contains((key, value)):
            node.val.insert((key, value))

    def get(self, key):
        '''Retrieve the value for 'key' from the table.'''
        node = self.List

        # find the correct bin
        for n in range(self.hash(key)):
            node = node.post

        node = node.val.List

        while node:
            if node.val[0] == key:
                return node.val[1]

            node = node.post

        raise KeyError('No such key.')
