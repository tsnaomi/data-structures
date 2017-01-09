class BinarySearchTree:

    def __init__(self, root=None):
        if root is None:
            self.root, self.left, self.right = None, None, None

        else:
            self.root = root
            self.left = BinarySearchTree()
            self.right = BinarySearchTree()

    def insert(self, n):
        '''Insert node 'n' into the tree.'''
        if self.root is None:
            self.root = n
            self.left = BinarySearchTree()
            self.right = BinarySearchTree()

        elif self.root > n:
            self.left.insert(n)

        elif self.root < n:
            self.right.insert(n)

    def contains(self, n):
        '''Return True if the tree contains node 'n'; otherwise, False.'''
        node = self

        while node.root != n and node.root is not None:
            node = node.left if node.root > n else node.right

        return node.root == n

    def size(self):
        '''Return the number of nodes in the tree.'''
        if self.root is None:
            return 0

        return 1 + self.left.size() + self.right.size()

    def depth(self):
        '''Return the number of levels in the tree.'''
        if self.root is None:
            return 0

        return 1 + max(self.left.depth(), self.right.depth())

    def get_balance(self):
        '''Return an integer indicating the tree's balance.

        (0 = balanced, <0 = left-heavy, >0 = right-heavy)
        '''
        if self.root is None:
            return 0

        return self.right.depth() - self.left.depth()

    def in_order(self):
        '''Traverse and return the tree's nodes in order.'''
        if self.left is not None:
            for n in self.left.in_order():
                yield n

        if self.root is not None:
            yield self.root

        if self.right is not None:
            for n in self.right.in_order():
                yield n

    def pre_order(self):
        '''Traverse and return the tree's nodes, yielding parents first.'''
        if self.root is not None:
            yield self.root

        if self.left is not None:
            for n in self.left.pre_order():
                yield n

        if self.right is not None:
            for n in self.right.pre_order():
                yield n

    def post_order(self):
        '''Traverse and return the tree's nodes, yielding children first.'''
        if self.left is not None:
            for n in self.left.post_order():
                yield n

        if self.right is not None:
            for n in self.right.post_order():
                yield n

        if self.root is not None:
            yield self.root

    def breadth_first(self):
        '''Traverse and return the tree's nodes in level order.'''
        if self.root is not None:
            queue = [self]

            while queue:
                node = queue.pop(0)

                if node.left.root is not None:
                    queue.append(node.left)

                if node.right.root is not None:
                    queue.append(node.right)

                yield node.root

    def delete(self, n, parent=None, child=None):
        '''Delete node 'n' from the tree.'''
        if self.root is not None:

            # delete this node
            if self.root == n:

                # if the tree has 0 children, remove the tree
                if self.left.root is None and self.right.root is None:
                    return setattr(parent, child, BinarySearchTree())

                # if the tree has 1 child, replace the tree with its child
                if self.right.root is None:
                    return setattr(parent, child, self.left)

                if self.left.root is None:
                    return setattr(parent, child, self.right)

                # if the tree has 2 children, do something complicated...
                return self._delete(n, parent)

            # search down the left side of the tree
            if n < self.root:
                return self.left.delete(n, self, 'left')

            # search down the right side of the tree
            return self.right.delete(n, self, 'right')

    def _delete(self, n, parent):
        '''Replace 'n' with the leftmost child of its right child.'''
        leftmost_parent = self
        leftmost = self.right

        while leftmost.left.root is not None:
            leftmost_parent = leftmost
            leftmost = leftmost.left

        if parent and leftmost.right.root is None:
            leftmost_parent.right = leftmost.right

        else:
            leftmost_parent.left = leftmost.right

        self.root = leftmost.root

    def dot(self, filename=None):
        '''Generate a visual representation of the tree using Graphviz.'''
        if self.root:
            dot = Digraph(filename=filename, directory='./digraphs')

            for n in self.pre_order():
                dot.node(str(n))

            dot.edges(self._dot())
            dot.view()

    def _dot(self):
        '''Return an iterator of all of the edges in the tree.'''
        if self.left and self.left.root is not None:
            yield (str(self.root), str(self.left.root))

            for edge in self.left._dot():
                yield edge

        if self.right and self.right.root is not None:
            yield (str(self.root), str(self.right.root))

            for edge in self.right._dot():
                yield edge
