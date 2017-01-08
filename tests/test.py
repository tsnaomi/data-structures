# !/usr/bin/env Python

import unittest

from algorithms import insert_sort, merge_sort
from data_structures import HashTable, LinkedList, Queue, Stack, BSTree
from nltk.corpus import gutenberg  # any excuse to use NLTK


# Data structure tests --------------------------------------------------------

# test singly-linked list
class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.foo = LinkedList()
        self.list1 = '(4, 3, 2, 1)'
        self.list2 = '(3, 2, 1)'
        self.list3 = '(4, 2, 1, 0)'
        self.list4 = '(bacon, 3.14, True, 4, 3, 2, 1)'

    def test_insert(self):
        for i in range(1, 5):
            self.foo.insert(i)
        self.assertEqual(self.foo.__str__(), self.list1)

    def test_pop(self):
        for i in range(1, 5):
            self.foo.insert(i)
        self.assertEqual(self.foo.pop(), 4)
        self.assertEqual(self.foo.__str__(), self.list2)

    def test_size(self):
        for i in range(10):
            self.foo.insert(i)
        self.assertEqual(self.foo.size(), 10)

    def test_search(self):
        for i in range(4):
            self.foo.insert(i)
        self.assertEqual(self.foo.search(2).value, 2)

    def test_remove(self):
        for i in range(5):
            self.foo.insert(i)
        self.foo.remove(3)
        self.assertEqual(self.foo.__str__(), self.list3)

    def test_PRINT(self):
        for i in range(1, 5):
            self.foo.insert(i)
        self.foo.insert(True)
        self.foo.insert(3.14)
        self.foo.insert('bacon')
        self.assertEqual(self.foo.PRINT(), self.list4)


class TestStack(unittest.TestCase):

    def setUp(self):
        self.breakfast = Stack()
        self.meal1 = ['pineapple juice', 'sausage', 'eggs', 'PANCAKES']
        self.meal2 = [2, 1, 0]

    def amass(self, node):
        nodes = []
        while node:
            nodes.append(node.value)
            node = node.next
        return nodes

    def test_push(self):
        self.breakfast.push('PANCAKES')
        self.breakfast.push('eggs')
        self.breakfast.push('sausage')
        self.breakfast.push('pineapple juice')
        nodes = self.amass(self.breakfast.node)
        self.assertEqual(nodes, self.meal1)

    def test_pop(self):
        for i in range(4):
            self.breakfast.push(i)
        returned = self.breakfast.pop()
        nodes = self.amass(self.breakfast.node)
        self.assertEqual(returned, 3)
        self.assertEqual(nodes, self.meal2)


class TestQueue(unittest.TestCase):

    def setUp(self):
        self.queue = Queue()
        self.list1 = [4, 3, 2, 1]
        self.list2 = [3, 2, 1]

    def amass(self, node):
        nodes = []
        while node:
            nodes.insert(0, node.value)
            node = node.next
        return nodes

    def test_enqueue(self):
        for i in range(1, 5):
            self.queue.enqueue(i)
        nodes = self.amass(self.queue.head)
        self.assertEqual(nodes, self.list1)

    def test_dequeue(self):
        for i in range(4):
            self.queue.enqueue(i)
        returned = self.queue.dequeue()
        nodes = self.amass(self.queue.head)
        self.assertEqual(returned, 0)
        self.assertEqual(nodes, self.list2)

    def test_size(self):
        for i in range(10):
            self.queue.enqueue(i)
        self.assertEqual(self.queue.size(), 10)


class TestHashTable(unittest.TestCase):

    def setUp(self):
        self.TABLE = HashTable()
        self.ALICE = list(set(gutenberg.words('carroll-alice.txt')))[:400]

    def test_hash(self):
        self.assertEqual(self.TABLE.hash('Alice in Wonderland, circa 1865'), 5)
        with self.assertRaises(TypeError):
            self.TABLE.hash(1234)

        # HashTable accurately handles whatever number of containers specified
        TABLE2 = HashTable(100)
        self.assertEqual(TABLE2.hash('Alice in Wonderland, circa 1865'), 29)

    def test_set(self):
        for word in self.ALICE:
            self.TABLE.set(word, word)
            bucket = self.TABLE.head
            for num in range(self.TABLE.hash(word)):
                bucket = bucket.next
            self.assertIsNotNone(bucket.value.search((word, word)))
        with self.assertRaises(TypeError):
            self.TABLE.set(4, 4)

    def test_get(self):
        for word in self.ALICE:
            self.TABLE.set(word, word)
            value = self.TABLE.get(word)
            self.assertEqual(value, word)
        with self.assertRaises(TypeError):
            self.TABLE.get(4)
        with self.assertRaises(KeyError):
            self.TABLE.get('Curiouser and curiouser!')

    def test_resetting_and_getting_new_values(self):
        for word in self.ALICE:
            self.TABLE.set(word, word)
        container = self.TABLE.head
        for num in range(self.TABLE.hash('Alice')):
            container = container.next
        self.assertIn(str(('ALICE', 'ALICE')), str(container.value))
        self.TABLE.set('ALICE', 'Down the Rabit-Hole')
        self.assertEqual(self.TABLE.get('ALICE'), 'Down the Rabit-Hole')
        self.assertNotIn(str(('ALICE', 'ALICE')), str(container.value))


class TestBinarySearchTree(unittest.TestCase):

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
            Tree('leaves')

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


# Algorithm tests -------------------------------------------------------------

class TestInsertionSort(unittest.TestCase):

    def setUp(self):
        self.list = [3, 1, 4, 5, 9, 2, 6]
        self.sorted = [1, 2, 3, 4, 5, 6, 9]

    def test_insertSort(self):
        self.assertEqual(insert_sort(self.list), self.sorted)

    def test_insertSort_empty(self):
        self.assertEqual(insert_sort([]), [])

    def test_insertSort_single(self):
        self.assertEqual(insert_sort([3]), [3])

    def test_insertSort_duplicates(self):
        self.list.append(4)
        expected = [1, 2, 3, 4, 4, 5, 6, 9]
        self.assertEqual(insert_sort(self.list), expected)

    def test_insertSort_sorted(self):
        self.assertEqual(insert_sort(sorted(self.list)), self.sorted)

    def test_insertSort_reversed(self):
        self.assertEqual(insert_sort(sorted(self.list)[::-1]), self.sorted)


class TestMergeSort(unittest.TestCase):

    def setUp(self):
        self.list = [3, 1, 4, 5, 9, 2, 6]
        self.sorted = [1, 2, 3, 4, 5, 6, 9]

    def test_insertSort(self):
        self.assertEqual(merge_sort(self.list), self.sorted)

    def test_insertSort_empty(self):
        self.assertEqual(merge_sort([]), [])

    def test_insertSort_single(self):
        self.assertEqual(merge_sort([3]), [3])

    def test_insertSort_duplicates(self):
        self.list.append(4)
        expected = [1, 2, 3, 4, 4, 5, 6, 9]
        self.assertEqual(merge_sort(self.list), expected)

    def test_insertSort_sorted(self):
        self.assertEqual(merge_sort(sorted(self.list)), self.sorted)

    def test_insertSort_reversed(self):
        self.assertEqual(merge_sort(sorted(self.list)[::-1]), self.sorted)

# -----------------------------------------------------------------------------

if __name__ == '__main__':
    unittest.main()
