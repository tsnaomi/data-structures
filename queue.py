# !/usr/bin/env Python

# inspiration: Special thanks to Justin Lee (github.com/risingmoon) for helping
#              me construct the queue using a singly-linked list.


class Node:
    """ a node in queue """
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class Queue:
    """ a First-In-First-Out data structure """
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, x):  # Attribution: Justin L. (risingmoon)
        """ adds an item to the queue """
        if self.head:
            self.tail.next = Node(x)
            self.tail = self.tail.next
        else:
            self.tail = Node(x)
            self.head = self.tail

    def dequeue(self):
        """ removes the first-in item from the queue and returns it """
        if self.head:
            if self.head == self.tail:
                self.tail = self.tail.next
            node, self.head = self.head, self.head.next
            return node.value
        raise ValueError("Empty queue!")

    def size(self):
        """ returns the size of the queue """
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
        return count
