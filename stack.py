# !/usr/bin/env Python


class Node:
    """ a pancake in a stack """
    def __init__(self, value=None, node=None):
        self.value = value
        self.next = node

    def __str__(self):
        return str(self.value)


class Stack:
    """ a virtual stack of pancakes... err... items... that
    constututes a Last-In-First-Out data structure """
    def __init__(self):
        self.pancake = None

    def push(self, x):
        """ adds a specified pancake to the top of the stack """
        next_pancake = self.pancake
        self.pancake, self.pancake.next = Node(x, self.pancake), next_pancake

    def pop(self):
        """ removes the pancake at the top of the stack """
        if self.pancake:
            x, self.pancake = self.pancake.value, self.pancake.next
            return x
        raise ValueError("""You have no pancakes to pop. Now, would you please
            pass the syrup?""")
