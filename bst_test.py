#!usr/bin/env Python

import unittest

from bst import Tree


class TestTree(unittest.TestCase):

    def setUp(self):
        self.tree = Tree(4)
        self.TREE = Tree()
        self.list = [3, 12, 8, 27, 13, 28, 31, 29, 30, 33, 40, 50, 34, 35]

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
        self.assertEqual(self.tree.value, 4)  # structure hasn't changed
        self.assertEqual(self.tree.left.value, 3)  # structure hasn't changed
        self.assertEqual(self.tree.right.value, 12)  # structure hasn't changed

        # insert into an empty tree
        self.TREE.insert(4)
        self.assertEqual(self.TREE.value, 4)

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
        self.assertEqual(self.tree.depth(), 7)
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

    def test_inOrder(self):
        # in-order traversal of a non-empty tree
        expected = [3, 4, 8, 12, 13, 27, 28, 29, 30, 31, 33, 34, 35, 40, 50]
        test = []
        for x in self.list:
            self.tree.insert(x)
        for i in self.tree.in_order():
            test.append(i)
        self.assertEqual(test, expected)

        # in-order traversal of an empty tree
        test = []
        for i in self.TREE.in_order():
            test.append(i)
        self.assertEqual(test, [])

    def test_preOrder(self):
        # pre-order traversal of a non empty tree
        expected = [4, 3, 12, 8, 27, 13, 28, 31, 29, 30, 33, 40, 34, 35, 50]
        test = []
        for x in self.list:
            self.tree.insert(x)
        for i in self.tree.pre_order():
            test.append(i)
        self.assertEqual(test, expected)

        # pre-order traversal of an empty tree
        test = []
        for i in self.TREE.pre_order():
            test.append(i)
        self.assertEqual(test, [])

    def test_postOrder(self):
        # post-order traversal of a non empty tree
        expected = [3, 8, 13, 30, 29, 35, 34, 50, 40, 33, 31, 28, 27, 12, 4]
        test = []
        for x in self.list:
            self.tree.insert(x)
        for i in self.tree.post_order():
            test.append(i)
        self.assertEqual(test, expected)

        # post-order traversal of an empty tree
        test = []
        for i in self.TREE.post_order():
            test.append(i)
        self.assertEqual(test, [])

    def test_breadthFirst(self):
        # breadth-first traversal of a non-empty tree
        expected = [4, 3, 12, 8, 27, 13, 28, 31, 29, 33, 30, 40, 34, 50, 35]
        test = []
        for x in self.list:
            self.tree.insert(x)
        for i in self.tree.breadth_first():
            test.append(i)
        self.assertEqual(test, expected)

        # breadth-first traversal of an empty tree
        test = []
        for i in self.TREE.breadth_first():
            test.append(i)
        self.assertEqual(test, [])

    def test_delete(self):
        for x in self.list:
            self.tree.insert(x)

        # deleting a node with no descendants from a non-empty tree
        expected = [4, 3, 12, 8, 27, 13, 28, 31, 29, 33, 30, 40, 34, 50]
        test = []
        self.tree.delete(35)
        for i in self.tree.breadth_first():
            test.append(i)
        self.assertEqual(test, expected)

        # deleting a node with one descendant from a non-empty tree
        expected = [4, 3, 12, 8, 27, 13, 28, 31, 29, 40, 30, 34, 50]
        test = []
        self.tree.delete(33)
        for i in self.tree.breadth_first():
            test.append(i)
        self.assertEqual(test, expected)

        # deleting a node with two descendants from a non-empty tree
        expected = [4, 3, 12, 8, 27, 13, 28, 30, 29, 40, 34, 50]
        test = []
        self.tree.delete(31)
        for i in self.tree.breadth_first():
            test.append(i)
        self.assertEqual(test, expected)

        # deleting the root of a non-empty tree
        expected = [8, 3, 12, 27, 13, 28, 30, 29, 40, 34, 50]
        test = []
        self.tree.delete(4)
        for i in self.tree.breadth_first():
            test.append(i)
        self.assertEqual(test, expected)

        # deleting a nonexistent node from a non-empty tree
        expected = [8, 3, 12, 27, 13, 28, 30, 29, 40, 34, 50]
        test = []
        self.tree.delete(9)
        for i in self.tree.breadth_first():
            test.append(i)
        self.assertEqual(test, expected)

        # deleting a nonexistent node from an empty tree
        expected, test = [], []
        self.TREE.delete(29)
        for i in self.TREE.breadth_first():
            test.append(i)
        self.assertEqual(test, expected)

if __name__ == '__main__':
    unittest.main()
