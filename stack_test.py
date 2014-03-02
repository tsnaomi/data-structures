#!/usr/bin/enr Python

from stack import Stack
import unittest


class TestStack(unittest.TestCase):
    """ """
    def setUp(self):
        self.breakfast = Stack()
        self.meal1 = ["pineapple juice", "sausage", "eggs", "PANCAKES"]
        self.meal2 = [2, 1, 0]

    def amass(self, node):
        nodes = []
        while node:
            nodes.append(node.value)
            node = node.next
        return nodes

    def test_push(self):
        self.breakfast.push("PANCAKES")
        self.breakfast.push("eggs")
        self.breakfast.push("sausage")
        self.breakfast.push("pineapple juice")
        nodes = self.amass(self.breakfast.node)
        self.assertEqual(nodes, self.meal1)

    def test_pop(self):
        for i in range(4):
            self.breakfast.push(i)
        returned = self.breakfast.pop()
        nodes = self.amass(self.breakfast.node)
        self.assertEqual(returned, 3)
        self.assertEqual(nodes, self.meal2)

if __name__ == '__main__':
    unittest.main()
