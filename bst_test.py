#!usr/bin/env Python

import unittest

from bst import Tree


class TestTree(unittest.TestCase):

    def setUp(self):
        self.tree = Tree(4)
        self.TREE = Tree()
        self.list = [3, 12, 8, 27, 13, 28, 31, 24, 30, 33, 40, 50, 34, 35]

    def test_init(self):
        # init with a non-empty tree
        self.assertEqual(self.tree.value, 4)
        self.assertTrue(self.tree.left.value is None)
        self.assertTrue(self.tree.right.value is None)

        # init with an empty tree
        self.assertTrue(self.TREE.value is None)
        self.assertTrue(self.TREE.left is None)
        self.assertTrue(self.TREE.right is None)

        # init with a forbidden value
        with self.assertRaises(TypeError):
            TREE = Tree('leaves')

    def test_insert(self):
        # insert into a non-empty tree
        for x in self.list[:2]:
            self.tree.insert(x)
        self.assertEqual(self.tree.left.value, 3)
        self.assertEqual(self.tree.right.value, 12)

        # inssert an existing value into a tree
        self.tree.insert(4)

        # insert into an empty tree
        self.TREE.insert(4)
        self.assertEqual(self.tree.value, 4)  # structure hasn't changed
        self.assertEqual(self.tree.left.value, 3)  # structure hasn't changed
        self.assertEqual(self.tree.right.value, 12)  # structure hasn't changed

        # insert a forbidden value
        with self.assertRaises(TypeError):
            self.tree.insert('branches')

    def test_contains(self):
        # test contains() with a non-empty tree
        self.assertTrue(self.tree.contains(4))
        for x in self.list:
            self.assertFalse(self.tree.contains(x))
            self.tree.insert(x)
            self.assertTrue(self.tree.contains(x))

        # test contains() with an empty tree
        self.assertFalse(self.TREE.contains(4))

        # test contains() with a forbidden value
        with self.assertRaises(TypeError):
            self.tree.contains('blossoms')

    def test_size(self):
        # size of a non-empty tree
        self.assertEqual(self.tree.size(), 1)
        for x in self.list:
            self.tree.insert(x)
            self.assertTrue(self.tree.size(), self.list.index(x)+2)

        # size of an empty tree
        self.assertEqual(self.TREE.size(), 0)

    def test_depth(self):
        # depth of a non-empty tree
        for x in self.list[:5]:
            self.tree.insert(x)
        self.assertEqual(self.tree.depth(), 4)
        for x in self.list[5:10]:
            self.tree.insert(x)
        self.assertEqual(self.tree.depth(), 6)
        for x in self.list[10:]:
            self.tree.insert(x)
        self.assertEqual(self.tree.depth(), 9)

        # depth of an empty tree
        self.assertEqual(self.TREE.depth(), 0)

    def test_balance(self):
        # balance of a non-empty tree (right-heavy)
        for x in self.list[:14]:
            self.tree.insert(x)
        self.assertEqual(self.tree.balance(), 7)
        self.tree.insert(38)
        self.assertEqual(self.tree.balance(), 8)
        self.tree.insert(37)
        self.assertEqual(self.tree.balance(), 9)
        self.tree.insert(2)
        self.assertEqual(self.tree.balance(), 8)

        # balance of a non-empty tree (left-heavy)
        TREE = Tree(4)
        for x in [1, 2, 3, 5]:
            TREE.insert(x)
        self.assertEqual(TREE.balance(), -2)

        # balance of an empty tree
        self.assertEqual(self.TREE.balance(), 0)

if __name__ == '__main__':
    unittest.main()
