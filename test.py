import re
import unittest

from algorithms import (
    insertion_sort,
    merge_sort,
    hoare_quicksort,
    lumoto_quicksort,
    radix_sort,
    )

from data_structures import (
    LinkedList,
    Stack,
    Queue,
    BinaryHeap,
    HashTable,
    Graph,
    BinarySearchTree,
    )


class TestLinkedList(unittest.TestCase):  # doubly-linked list

    def setUp(self):
        self.emptyList = LinkedList()
        self.List = LinkedList()

        # populate list with 1, 2, 3, 4
        for i in range(1, 5):
            self.List.append(i)

    def test_repr(self):
        '''Test returning the linked list as a string literal.'''
        self.assertEqual(repr(self.emptyList), str(()))
        tup = (1, 3.14, 'foo', True)

        for i in tup:
            self.emptyList.append(i)

        self.assertEqual(repr(self.emptyList), str(tup))

    def test_len_size(self):
        '''Test returning the length of the list.'''
        for i in range(100):
            self.emptyList.insert(i)

        self.assertEqual(len(self.emptyList), 100)
        self.assertEqual(self.emptyList.size(), 100)

        self.emptyList.pop()
        self.assertEqual(len(self.emptyList), 99)
        self.assertEqual(self.emptyList.size(), 99)

        self.emptyList.shift()
        self.assertEqual(len(self.emptyList), 98)
        self.assertEqual(self.emptyList.size(), 98)

        self.emptyList.remove(4)
        self.assertEqual(len(self.emptyList), 97)
        self.assertEqual(self.emptyList.size(), 97)

    def test_tuple(self):
        '''Test returning the linked list as a list literal.'''
        self.assertEqual(list(self.emptyList), [])
        li = [1, 3.14, 'foo', True]

        for i in li:
            self.emptyList.append(i)

        self.assertEqual(list(self.emptyList), li)

    def test_list(self):
        '''Test returning the linked list as a tuple literal.'''
        self.assertEqual(tuple(self.emptyList), ())
        tup = (1, 3.14, 'foo', True)

        for i in tup:
            self.emptyList.append(i)

        self.assertEqual(tuple(self.emptyList), tup)

    def test_in_contains(self):
        '''Test returning T/F for whether the list contains certain values.'''
        self.assertTrue(2 in self.List)
        self.assertFalse(10 in self.List)

        self.assertTrue(self.List.contains(2))
        self.assertFalse(self.List.contains(10))

    def test_insert(self):
        '''Test inserting values at the head of list the list.'''
        for i in range(1, 5):
            self.emptyList.insert(i)

        self.assertEqual(tuple(self.emptyList), (4, 3, 2, 1))

    def test_append(self):
        '''Test appending values at the end of the list.'''
        self.List.append(True)
        self.assertEqual(tuple(self.List), (1, 2, 3, 4, True))

    def test_pop(self):
        '''Test popping off and returning the head of the list.'''
        self.assertEqual(self.List.pop(), 1)
        self.assertEqual(tuple(self.List), (2, 3, 4))
        self.assertEqual(self.List.pop(), 2)
        self.assertEqual(self.List.pop(), 3)
        self.assertEqual(self.List.pop(), 4)
        self.assertEqual(tuple(self.List), ())

        with self.assertRaises(IndexError):
            self.emptyList.pop()

    def test_shift(self):
        '''Test removing and returning the tail of the list.'''
        self.assertEqual(self.List.shift(), 4)
        self.assertEqual(tuple(self.List), (1, 2, 3))
        self.assertEqual(self.List.shift(), 3)
        self.assertEqual(self.List.shift(), 2)
        self.assertEqual(self.List.shift(), 1)
        self.assertEqual(tuple(self.List), ())

        with self.assertRaises(IndexError):
            self.emptyList.shift()

    def test_remove(self):
        '''Testing finding and removing values from the list.'''
        for i in range(1, 5):
            self.List.append(i)

        self.List.remove(2)
        self.assertEqual(tuple(self.List), (1, 3, 4, 1, 2, 3, 4))

        with self.assertRaises(ValueError):
            self.List.remove(6)


class TestStack(unittest.TestCase):  # LIFO

    def setUp(self):
        self.emptyStack = Stack()
        self.Stack = Stack()

        for i in range(5):
            self.Stack.push(i)

    def test_repr(self):
        '''Test returning the stack as a string literal.'''
        self.assertEqual(repr(self.emptyStack), str(()))
        tup = (1, 3.14, 'foo', True)

        for i in tup:
            self.emptyStack.push(i)

        self.assertEqual(repr(self.emptyStack), str((True, 'foo', 3.14, 1)))

    def test_len_size(self):
        '''Test returning the size of the stack.'''
        for i in range(100):
            self.emptyStack.push(i)

        self.assertEqual(len(self.emptyStack), 100)
        self.assertEqual(self.emptyStack.size(), 100)

        self.emptyStack.pop()
        self.assertEqual(len(self.emptyStack), 99)
        self.assertEqual(self.emptyStack.size(), 99)

    def test_tuple(self):
        '''Test returning the stack as a tuple literal.'''
        self.assertEqual(tuple(self.emptyStack), ())
        tup = (1, 3.14, 'foo', True)

        for i in tup:
            self.emptyStack.push(i)

        self.assertEqual(tuple(self.emptyStack), (True, 'foo', 3.14, 1))

    def test_list(self):
        '''Test returning the stack as a list literal.'''
        self.assertEqual(list(self.emptyStack), [])
        li = [1, 3.14, 'foo', True]

        for i in li:
            self.emptyStack.push(i)

        self.assertEqual(list(self.emptyStack), [True, 'foo', 3.14, 1])

    def test_push(self):
        '''Test pushing items on top of the stack.'''
        self.Stack.push(True)
        self.assertEqual(tuple(self.Stack), (True, 4, 3, 2, 1, 0))

    def test_pop(self):
        '''Test popping off and returning the top of the stack.'''
        self.assertEqual(self.Stack.pop(), 4)
        self.assertEqual(tuple(self.Stack), (3, 2, 1, 0))
        self.assertEqual(self.Stack.pop(), 3)
        self.assertEqual(self.Stack.pop(), 2)
        self.assertEqual(self.Stack.pop(), 1)
        self.assertEqual(self.Stack.pop(), 0)
        self.assertEqual(tuple(self.Stack), ())

        with self.assertRaises(ValueError):
            self.Stack.pop()

    def test_peek(self):
        '''Test peeking at the top of the stack w/o modifying the stack.'''
        self.assertEqual(self.Stack.peek(), 4)

        with self.assertRaises(ValueError):
            self.emptyStack.peek()


class TestQueue(unittest.TestCase):  # FIFO

    def setUp(self):
        self.emptyQueue = Queue()
        self.Queue = Queue()

        for i in range(5):
            self.Queue.enqueue(i)

    def test_repr(self):
        '''Test returning the queue as a string literal.'''
        self.assertEqual(repr(self.emptyQueue), str(()))
        tup = (1, 3.14, 'foo', True)

        for i in tup:
            self.emptyQueue.enqueue(i)

        self.assertEqual(repr(self.emptyQueue), str(tup))

    def test_len_size(self):
        '''Test returning the size of the queue.'''
        for i in range(100):
            self.emptyQueue.enqueue(i)

        self.assertEqual(len(self.emptyQueue), 100)
        self.assertEqual(self.emptyQueue.size(), 100)

        self.emptyQueue.dequeue()
        self.assertEqual(len(self.emptyQueue), 99)
        self.assertEqual(self.emptyQueue.size(), 99)

    def test_tuple(self):
        '''Test returning the queue as a tuple literal.'''
        self.assertEqual(tuple(self.emptyQueue), ())
        tup = (1, 3.14, 'foo', True)

        for i in tup:
            self.emptyQueue.enqueue(i)

        self.assertEqual(tuple(self.emptyQueue), tup)

    def test_list(self):
        '''Test returning the queue as a list literal.'''
        self.assertEqual(list(self.emptyQueue), [])
        li = [1, 3.14, 'foo', True]

        for i in li:
            self.emptyQueue.enqueue(i)

        self.assertEqual(list(self.emptyQueue), li)

    def test_enqueue(self):
        '''Test adding items to the front of the queue.'''
        self.Queue.enqueue(True)
        self.assertEqual(tuple(self.Queue), (0, 1, 2, 3, 4, True))

    def test_dequeue(self):
        '''Test removing items from the front of the queue.'''
        self.assertEqual(self.Queue.dequeue(), 0)
        self.assertEqual(tuple(self.Queue), (1, 2, 3, 4))
        self.assertEqual(self.Queue.dequeue(), 1)
        self.assertEqual(self.Queue.dequeue(), 2)
        self.assertEqual(self.Queue.dequeue(), 3)
        self.assertEqual(self.Queue.dequeue(), 4)
        self.assertEqual(tuple(self.Queue), ())

        with self.assertRaises(ValueError):
            self.Queue.dequeue()

    def test_peek(self):
        '''Test peeking at the first enqueued item w/o modifying the queue.'''
        self.assertEqual(self.Queue.peek(), 0)

        with self.assertRaises(ValueError):
            self.emptyQueue.peek()


class TestBinaryHeap(unittest.TestCase):

    def setUp(self):
        # min heap
        self.minHeap = BinaryHeap(Min=True, iterable=[0, 2, 4, 6, 8])
        self.emptyMinHeap = BinaryHeap(Min=True)

        # max heap
        self.maxHeap = BinaryHeap(Min=False, iterable=[0, 2, 4, 6, 8])
        self.emptyMaxHeap = BinaryHeap(Min=False)

    def test_len_size(self):
        '''Test returning the size of the heap.'''
        # min heap
        self.assertEqual(len(self.minHeap), 5)
        self.assertEqual(self.minHeap.size(), 5)
        self.minHeap.pop()
        self.assertEqual(len(self.minHeap), 4)
        self.assertEqual(self.minHeap.size(), 4)

        # max heap
        self.assertEqual(len(self.maxHeap), 5)
        self.assertEqual(self.maxHeap.size(), 5)
        self.maxHeap.pop()
        self.assertEqual(len(self.maxHeap), 4)
        self.assertEqual(self.maxHeap.size(), 4)

    def test_push(self):
        '''Test pushing items into a binary heap.'''
        # min heap
        self.assertEqual(self.minHeap.Heap, [0, 2, 4, 6, 8])
        self.minHeap.push(3)
        self.assertEqual(self.minHeap.Heap, [0, 2, 3, 6, 8, 4])
        self.minHeap.push(-1)
        self.assertEqual(self.minHeap.Heap, [-1, 2, 0, 6, 8, 4, 3])
        self.minHeap.push(-1)
        self.assertEqual(self.minHeap.Heap, [-1, -1, 0, 2, 8, 4, 3, 6])

        # max heap (assuming, when instantiating a heap with an iterable, the
        # iterable's items are pushed one-by-one)
        self.assertEqual(self.maxHeap.Heap, [8, 6, 2, 0, 4])
        self.maxHeap.push(5)
        self.assertEqual(self.maxHeap.Heap, [8, 6, 5, 0, 4, 2])
        self.maxHeap.push(9)
        self.assertEqual(self.maxHeap.Heap, [9, 6, 8, 0, 4, 2, 5])
        self.maxHeap.push(8)
        self.assertEqual(self.maxHeap.Heap, [9, 8, 8, 6, 4, 2, 5, 0])

    def test_pop(self):
        '''Test popping off and returning the top items in a binary heap.'''
        # min heap
        self.assertEqual(self.minHeap.pop(), 0)
        self.assertEqual(self.minHeap.Heap, [2, 6, 4, 8])
        self.assertEqual(self.minHeap.pop(), 2)
        self.assertEqual(self.minHeap.Heap, [4, 6, 8])
        self.assertEqual(self.minHeap.pop(), 4)
        self.assertEqual(self.minHeap.Heap, [6, 8])
        self.assertEqual(self.minHeap.pop(), 6)
        self.assertEqual(self.minHeap.Heap, [8])
        self.assertEqual(self.minHeap.pop(), 8)
        self.assertEqual(self.minHeap.Heap, [])

        with self.assertRaises(ValueError):
            self.minHeap.pop()

        # max heap
        self.assertEqual(self.maxHeap.pop(), 8)
        self.assertEqual(self.maxHeap.Heap, [6, 4, 2, 0])
        self.assertEqual(self.maxHeap.pop(), 6)
        self.assertEqual(self.maxHeap.Heap, [4, 0, 2])
        self.assertEqual(self.maxHeap.pop(), 4)
        self.assertEqual(self.maxHeap.Heap, [2, 0])
        self.assertEqual(self.maxHeap.pop(), 2)
        self.assertEqual(self.maxHeap.Heap, [0])
        self.assertEqual(self.maxHeap.pop(), 0)
        self.assertEqual(self.maxHeap.Heap, [])

        with self.assertRaises(ValueError):
            self.minHeap.pop()

    def test_peek(self):
        '''Test peeking at the heap's topmost item w/o modifying the heap.'''
        # min heap
        self.assertEqual(self.minHeap.peek(), 0)

        with self.assertRaises(ValueError):
            self.emptyMinHeap.peek()

        # max heap
        self.assertEqual(self.maxHeap.peek(), 8)

        with self.assertRaises(ValueError):
            self.emptyMaxHeap.peek()


class TestGraph(unittest.TestCase):

    def setUp(self):
        self.graph = Graph()
        self.emptyGraph = Graph()
        self.values = [3, 1, 4, 5, 9, 2, 6, 8, 7, 0]
        self.pairs = [(3, 4), (2, 9), (2, 4)]

        for n in self.values:
            self.graph.add_node(n)

        for n1, n2 in self.pairs:
            self.graph.add_edge(n1, n2)

        self.values.sort()

    def test_add_node(self):
        '''Test adding nodes to a graph.'''
        # implicitly test Graph.nodes() as well
        self.assertEqual(self.graph.nodes(), self.values)
        self.assertEqual(self.emptyGraph.nodes(), [])

        # test adding a duplicate node
        self.graph.add_node(0)
        self.assertEqual(self.graph.nodes(), self.values)

    def test_add_edge(self):
        '''Test adding edges to a graph (w/o using has_edge).'''
        test = set([])  # create a set listing edges as tuples

        for n1, edges in self.graph.Nodes.iteritems():
            for n2 in edges:
                pair = (n1, n2)
                test.add((min(pair), max(pair)))

        # ensure that setUp appropriately added edges
        self.assertEqual(test, set(self.pairs))

        # test adding an existent edge
        self.graph.add_edge(3, 4)
        self.assertTrue(3 in self.graph.Nodes[4])
        self.assertTrue(4 in self.graph.Nodes[3])

        # test adding an edge to a non-existent node
        self.graph.add_edge(3, 10)
        self.assertTrue(3 in self.graph.Nodes[10])
        self.assertTrue(10 in self.graph.Nodes[3])
        self.assertEqual(self.graph.nodes(), range(11))

        # test adding an edge to multiple non-existent nodes
        self.emptyGraph.add_edge(2, 1)
        # self.assertEqual(self.emptyGraph.edges(), [set((2, 1))])
        self.assertTrue(2 in self.emptyGraph.Nodes[1])
        self.assertTrue(1 in self.emptyGraph.Nodes[2])
        self.assertEqual(self.emptyGraph.nodes(), [1, 2])

    def test_del_node(self):
        '''Test deleting nodes from a graph.'''
        self.graph.del_node(1)
        self.graph.del_node(4)
        self.assertEqual(self.graph.nodes(), [0, 2, 3, 5, 6, 7, 8, 9])
        self.assertFalse(4 in self.graph.Nodes[2])
        self.assertFalse(4 in self.graph.Nodes[3])

        # test deleting fron an empty graph
        with self.assertRaises(ValueError):
            self.emptyGraph.del_node(0)

    def test_del_edge(self):
        '''Test deleting edges from a graph.'''
        # test deleting an existent edge
        self.graph.del_edge(3, 4)
        self.assertFalse(3 in self.graph.Nodes[4])
        self.assertFalse(4 in self.graph.Nodes[3])

        # ensure that the nodes remained intact
        self.assertEqual(self.graph.nodes(), self.values)

        # test deleting a non-existent edge between existent nodes
        with self.assertRaises(ValueError):
            self.graph.del_edge(1, 2)

        # test deleting an edge between non-existent nodes
        with self.assertRaises(ValueError):
            self.emptyGraph.del_edge(1, 2)

    def test_has_node(self):
        '''Test checking whether a graph contains certain nodes.'''
        for n in self.values:
            self.assertTrue(self.graph.has_node(n))

        self.assertFalse(self.graph.has_node(99))
        self.assertFalse(self.emptyGraph.has_node(99))

    def test_neighbors(self):
        '''Test listing the neighbors of nodes in a graph.'''
        self.assertEqual(self.graph.neighbors(0), [])
        self.assertEqual(self.graph.neighbors(3), [4])
        self.assertEqual(self.graph.neighbors(4), [2, 3])

        # test listing neighbors for non-existent nodes
        with self.assertRaises(ValueError):
            self.emptyGraph.neighbors(99)

    def test_is_adjacent(self):
        '''Test checking whether two nodes are adjacent.'''
        self.assertFalse(self.graph.is_adjacent(0, 9))
        self.assertTrue(self.graph.is_adjacent(4, 3))

        # test checking adjacency with non-existent nodes
        with self.assertRaises(ValueError):
            self.emptyGraph.is_adjacent(0, 99)


class TestBinarySearchTree(unittest.TestCase):

    def setUp(self):
        self.tree = BinarySearchTree(4)
        self.emptyTree = BinarySearchTree()
        self.leaves = [3, 12, 8, 27, 13, 28, 31, 29, 30, 33, 44, 50, 34, 35]

    def test_init(self):
        '''Test initializing a binary search tree.'''
        # initializing a non-empty tree
        self.assertEqual(self.tree.root, 4)
        self.assertIsNone(self.tree.left.root)
        self.assertIsNone(self.tree.right.root)

        # initializing an empty tree
        self.assertIsNone(self.emptyTree.root)

        with self.assertRaises(AttributeError):
            self.emptyTree.left.root

    def test_insert(self):
        '''Test inserting nodes into a binary search tree.'''
        # inserting into a non-empty tree
        for n in self.leaves:
            self.tree.insert(n)

        self.assertEqual(self.tree.left.root, 3)
        self.assertEqual(self.tree.right.root, 12)
        self.assertEqual(self.tree.right.left.root, 8)
        self.assertEqual(self.tree.right.right.root, 27)

        # inserting an existing value
        self.tree.insert(4)
        self.assertEqual(self.tree.root, 4)
        self.assertEqual(self.tree.left.root, 3)
        self.assertEqual(self.tree.right.root, 12)
        self.assertEqual(self.tree.right.left.root, 8)
        self.assertEqual(self.tree.right.right.root, 27)

        # inserting into an empty tree
        self.emptyTree.insert(9)
        self.assertEqual(self.emptyTree.root, 9)

    def test_contains(self):
        '''Test checking whether a BST contains certain nodes.'''
        # contains() with a non-empty tree
        self.assertTrue(self.tree.contains(4))

        for n in self.leaves:
            self.assertFalse(self.tree.contains(n))
            self.tree.insert(n)
            self.assertTrue(self.tree.contains(n))

        # contains() with an empty tree
        self.assertFalse(self.emptyTree.contains(4))

    def test_size(self):
        '''Test returning the size of a binary search tree.'''
        # size of a non-empty tree
        self.assertEqual(self.tree.size(), 1)

        for i, n in enumerate(self.leaves, start=2):
            self.tree.insert(n)
            self.assertEqual(self.tree.size(), i)

        # size of an empty tree
        self.assertEqual(self.emptyTree.size(), 0)

    def test_depth(self):
        '''Test returning the depth of a binary search tree.'''
        # depth of a non-empty tree
        self.assertEqual(self.tree.depth(), 1)

        for n in self.leaves[:5]:
            self.tree.insert(n)

        self.assertEqual(self.tree.depth(), 4)

        for n in self.leaves[5:10]:
            self.tree.insert(n)

        self.assertEqual(self.tree.depth(), 7)

        for n in self.leaves[10:]:
            self.tree.insert(n)

        self.assertEqual(self.tree.depth(), 9)

        # depth of an empty tree
        self.assertEqual(self.emptyTree.depth(), 0)

    def test_balance(self):
        '''Test returning the balance of a binary search tree.'''
        # balance of a non-empty tree (right-heavy)
        for n in self.leaves:
            self.tree.insert(n)

        self.assertEqual(self.tree.get_balance(), 7)
        self.tree.insert(38)
        self.assertEqual(self.tree.get_balance(), 8)
        self.tree.insert(37)
        self.assertEqual(self.tree.get_balance(), 9)
        self.tree.insert(2)
        self.assertEqual(self.tree.get_balance(), 8)

        # balance of an empty tree
        self.assertEqual(self.emptyTree.get_balance(), 0)

        # blanace of a non-empty tree (left-heavy)
        for n in [4, 1, 2, 3, 5]:
            self.emptyTree.insert(n)

        self.assertEqual(self.emptyTree.get_balance(), -2)

    def test_in_order(self):
        '''Test the in-order traversal of a binary search tree.'''
        # in-order traversal of a non-empty tree
        for n in self.leaves:
            self.tree.insert(n)

        expected = [3, 4, 8, 12, 13, 27, 28, 29, 30, 31, 33, 34, 35, 44, 50]
        self.assertEqual(list(self.tree.in_order()), expected)

        # in-order traversal of an empty tree
        self.assertEqual(list(self.emptyTree.in_order()), [])

    def test_pre_order(self):
        '''Test the pre-order traversal of a binary search tree.'''
        # pre-order traversal of a non-empty tree
        for n in self.leaves:
            self.tree.insert(n)

        expected = [4, 3, 12, 8, 27, 13, 28, 31, 29, 30, 33, 44, 34, 35, 50]
        self.assertEqual(list(self.tree.pre_order()), expected)

        # pre-order traversal of an empty tree
        self.assertEqual(list(self.emptyTree.pre_order()), [])

    def test_post_order(self):
        '''Test the post-order traversal of a binary search tree.'''
        # post-order traversal of a non-empty tree
        for n in self.leaves:
            self.tree.insert(n)

        expected = [3, 8, 13, 30, 29, 35, 34, 50, 44, 33, 31, 28, 27, 12, 4]
        self.assertEqual(list(self.tree.post_order()), expected)

        # post-order traversal of an empty tree
        self.assertEqual(list(self.emptyTree.post_order()), [])

    def test_breadth_first(self):
        '''Test the breadth-first traversal of a binary search tree.'''
        # breadth-first traversal of a non-empty tree
        for n in self.leaves:
            self.tree.insert(n)

        expected = [4, 3, 12, 8, 27, 13, 28, 31, 29, 33, 30, 44, 34, 50, 35]
        self.assertEqual(list(self.tree.breadth_first()), expected)

        # breadth-first traversal of an empty tree
        self.assertEqual(list(self.emptyTree.breadth_first()), [])

    def test_delete(self):
        '''Test deleting nodes from a binary search tree.'''
        for n in self.leaves:
            self.tree.insert(n)

        # deleting a node with no descendants
        self.tree.delete(35)
        expected = [4, 3, 12, 8, 27, 13, 28, 31, 29, 33, 30, 44, 34, 50]
        self.assertEqual(list(self.tree.breadth_first()), expected)

        # deleting a node with one descendant (left)
        self.tree.delete(3)
        expected = [4, 12, 8, 27, 13, 28, 31, 29, 33, 30, 44, 34, 50]
        self.assertEqual(list(self.tree.breadth_first()), expected)

        # test insertion after the deletion of a terminal node
        self.tree.insert(3)
        expected = [4, 3, 12, 8, 27, 13, 28, 31, 29, 33, 30, 44, 34, 50]
        self.assertEqual(list(self.tree.breadth_first()), expected)

        # deleting a node with one descendant (right)
        self.tree.delete(29)
        expected = [4, 3, 12, 8, 27, 13, 28, 31, 30, 33, 44, 34, 50]
        self.assertEqual(list(self.tree.breadth_first()), expected)

        # test insertion after the deletion of a non-terminal node
        self.tree.insert(29)
        expected = [4, 3, 12, 8, 27, 13, 28, 31, 30, 33, 29, 44, 34, 50]
        self.assertEqual(list(self.tree.breadth_first()), expected)

        # deleting a node with two (left & right) descendants
        self.tree.delete(44)
        self.tree.insert(51)
        expected = [4, 3, 12, 8, 27, 13, 28, 31, 30, 33, 29, 50, 34, 51]
        self.assertEqual(list(self.tree.breadth_first()), expected)

        # deleting a node with several right-branching descendants
        self.tree.delete(28)
        expected = [4, 3, 12, 8, 27, 13, 31, 30, 33, 29, 50, 34, 51]
        self.assertEqual(list(self.tree.breadth_first()), expected)

        # deleting a node with several left- and right-branching descendants
        self.tree.insert(29.5)
        self.tree.delete(27)
        expected = [4, 3, 12, 8, 29, 13, 31, 30, 33, 29.5, 50, 34, 51]
        self.assertEqual(list(self.tree.breadth_first()), expected)

        # deleting the root
        self.tree.delete(4)
        expected = [8, 3, 12, 29, 13, 31, 30, 33, 29.5, 50, 34, 51]
        self.assertEqual(list(self.tree.breadth_first()), expected)

        # deleting from an empty tree
        self.emptyTree.delete(4)
        self.assertEqual(list(self.emptyTree.breadth_first()), [])


class TestHashTable(unittest.TestCase):

    def setUp(self):
        self.table1 = HashTable()
        self.table2 = HashTable(100)

        # extract unique words from Jabberwocky
        with open('texts/jabberwocky.txt', 'r+') as f:
            self.strings = list(set(re.split(r'[^a-z]', f.read().lower())))

    def test_set_and_get(self):
        '''Test setting and getting key/value pairs in a hash table.'''
        for s in self.strings[1:]:
            self.table1.set(s, s.upper())
            self.table2.set(s, s.upper())

        for s in self.strings[1:]:
            self.assertEqual(self.table1.get(s), s.upper())
            self.assertEqual(self.table2.get(s), s.upper())

        # test retrieving a non-existent key/value pair
        with self.assertRaises(KeyError):
            self.table1.get('Lewis')

        with self.assertRaises(KeyError):
            self.table2.get('Carroll')

        # test hashing a non-string
        with self.assertRaises(TypeError):
            self.table1.hash(31415)

        with self.assertRaises(TypeError):
            self.table2.hash(92653)


class TestInsertionSort(unittest.TestCase):

    def setUp(self):
        self.sort = insertion_sort
        self.unsorted_list = [3, 1, 4, 5, 9, 2, 6, 5, 3, 8, 9, 7, 9]
        self.sorted_list = sorted(self.unsorted_list)
        self.reversed_list = list(reversed(self.sorted_list))

    def test_insertSort(self):
        self.assertEqual(self.sort(self.unsorted_list), self.sorted_list)

    def test_insertSort_empty(self):
        self.assertEqual(self.sort([]), [])

    def test_insertSort_singleton(self):
        self.assertEqual(self.sort([3]), [3])

    def test_insertSort_sorted(self):
        self.assertEqual(self.sort(self.sorted_list), self.sorted_list)

    def test_insertSort_reversed(self):
        self.assertEqual(self.sort(self.reversed_list), self.sorted_list)


class TestMergeSort(unittest.TestCase):

    def setUp(self):
        self.sort = merge_sort
        self.unsorted_list = [3, 1, 4, 5, 9, 2, 6, 5, 3, 8, 9, 7, 9]
        self.sorted_list = sorted(self.unsorted_list)
        self.reversed_list = list(reversed(self.sorted_list))

    def test_mergeSort(self):
        self.assertEqual(self.sort(self.unsorted_list), self.sorted_list)

    def test_mergeSort_empty(self):
        self.assertEqual(self.sort([]), [])

    def test_mergeSort_singleton(self):
        self.assertEqual(self.sort([3]), [3])

    def test_mergeSort_sorted(self):
        self.assertEqual(self.sort(self.sorted_list), self.sorted_list)

    def test_mergeSort_reversed(self):
        self.assertEqual(self.sort(self.reversed_list), self.sorted_list)


class TestQuicksort(unittest.TestCase):

    def setUp(self):
        self.hoareSort = hoare_quicksort
        self.lumotoSort = lumoto_quicksort
        self.unsorted1 = [3, 1, 4, 5, 9, 2, 6, 5, 3, 8, 9, 7, 9]
        self.unsorted2 = [3, 1, 4, 5, 9, 2, 6, 5, 3, 8, 9, 7, 9]
        self.sorted_list = sorted(self.unsorted1)
        self.reversed_list = list(reversed(self.sorted_list))

    def test_quicksort(self):
        # hoare partition
        self.assertEqual(self.hoareSort(self.unsorted1), self.sorted_list)

        # lumoto partition
        self.assertEqual(self.lumotoSort(self.unsorted2), self.sorted_list)

    def test_quicksort_empty(self):
        # hoare partition
        self.assertEqual(self.hoareSort([]), [])

        # lumoto partition
        self.assertEqual(self.lumotoSort([]), [])

    def test_quicksort_singleton(self):
        # hoare partition
        self.assertEqual(self.hoareSort([3]), [3])

        # lumoto partition
        self.assertEqual(self.lumotoSort([3]), [3])

    def test_quicksort_sorted(self):
        # hoare partition
        self.assertEqual(self.hoareSort(self.sorted_list), self.sorted_list)

        # lumoto partition
        self.assertEqual(self.lumotoSort(self.sorted_list), self.sorted_list)

    def test_quicksort_reversed(self):
        # lumoto partition
        self.assertEqual(self.hoareSort(self.reversed_list), self.sorted_list)

        # hoare partition
        self.assertEqual(self.lumotoSort(self.reversed_list), self.sorted_list)


class TestRadixSort(unittest.TestCase):

    def setUp(self):
        self.sort = radix_sort
        self.unsorted_list = [3, 1, 4, 5, 9, 2, 6, 5, 3, 8, 9, 2400, 24, 240]
        self.sorted_list = sorted(self.unsorted_list)
        self.reversed_list = list(reversed(self.sorted_list))

    def test_mergeSort(self):
        self.assertEqual(self.sort(self.unsorted_list), self.sorted_list)

    def test_mergeSort_empty(self):
        self.assertEqual(self.sort([]), [])

    def test_mergeSort_singleton(self):
        self.assertEqual(self.sort([3]), [3])

    def test_mergeSort_sorted(self):
        self.assertEqual(self.sort(self.sorted_list), self.sorted_list)

    def test_mergeSort_reversed(self):
        self.assertEqual(self.sort(self.reversed_list), self.sorted_list)


if __name__ == '__main__':
    unittest.main()
