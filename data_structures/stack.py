# !/usr/bin/env Python


class Node:
    """ a node in a stack """
    def __init__(self, value=None, node=None):
        self.value = value
        self.next = node

    def __str__(self):
        return str(self.value)


class Stack:
    """ a Last-In-First-Out data structure """
    def __init__(self):
        self.node = None

    def push(self, x):
        """ adds a specified node to the top of the stack """
        self.node = Node(x, self.node)

    def pop(self):
        """ removes the node at the top of the stack """
        if self.node:
            x, self.node = self.node.value, self.node.next
            return x
        raise ValueError("""You have no pancakes to pop. Now, would you please
            pass the syrup?""")
