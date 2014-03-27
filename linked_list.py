#!/usr/bin/env Python


class Node(object):
    """ a node in a singly-linked list in Python """
    def __init__(self, value=None, node=None):
        self.value = value
        self.next = node

    def __str__(self):
        if isinstance(self.value, str):
            return "\'%s\'" % (self.value)
        else:
            return str(self.value)  # return '%s' % self.value


class LinkedList(object):
    """ a singly-linked list in Python """
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
        """ inserts item at the head of the list """
        self.head = Node(x, self.head)

    def pop(self):
        """ pops the first item off the head of the list and returns it """
        node = self.head
        if node:
            self.head = self.head.next
            return node.value
        raise ValueError("LinkedList is empty")

    def size(self):
        """ returns the number of items in the list """
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
        return count

    def search(self, x):
        """ searches for a specified item in the list and returns the node
        containing it; returns None if the item is not found """
        node = self.head
        while node:
            if node.value == x:
                return node
            node = node.next

    def remove(self, x):
        """ removes a specified node from the list """
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
        """ prints a tuple literal of the nodes in the list """
        return self.__str__()
