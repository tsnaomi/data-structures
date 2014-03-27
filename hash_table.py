#!/usr/bin/env Python

from linked_list import LinkedList

# Sources:  github.com/markcharyk/data-structures/
#           github.com/geekofalltrades/data-structures/


class HashTable(LinkedList):
    ''' a Hash Table in Python '''
    def __init__(self, num=32):
        self.num = num
        LinkedList.__init__(self)
        for x in range(num):
            self.insert(LinkedList())

    def hash(self, key):
        ''' hashes the key provided '''
        if isinstance(key, str):
            count = 0
            for character in key:
                count += ord(character)
            return count % self.num
        raise TypeError('Strings only please.')

    def set(self, key, value):
        ''' stores the key/value pair '''
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
        ''' returns the value stored with the provided key '''
        container = self.head
        for num in range(self.hash(key)):
            container = container.next
        node = container.value.head
        while node:
            if node.value[0] == key:
                return node.value[1]
            node = node.next
        raise KeyError('My apologies, there\'s no such key in this HashTable.')
