class BinaryHeap:

    def __init__(self, Min=True, iterable=None):
        self.Heap = []
        self._cmp = (lambda p, c: p >= c) if Min else (lambda p, c: p <= c)

        for i in iterable:
            self.push(i)

    def __repr__(self):
        return str(self.Heap)

    def _parent(self, index):
        '''Get the parent index of the item at 'index'.'''
        return int((index - 1) / 2)

    def _left(self, index):
        '''Get the left child index of the item at 'index'.'''
        return 2 * index + 1

    def _right(self, index):
        '''Get the right child index of the item at 'index'.'''
        return 2 * index + 2

    def _get(self, index):
        '''Return the value of the item at 'index'.'''
        if index > -1:
            try:
                return self.Heap[index]

            except IndexError:
                pass

        raise ValueError('No such item.')

    def _swap_upward(self, c, c_val):
        '''Maintain the heap property after pushing.'''
        try:
            p = self._parent(c)
            p_val = self._get(p)

            if self._cmp(p_val, c_val):
                self.Heap[p] = c_val
                self.Heap[c] = p_val
                self._swap_upward(p, c_val)

        except ValueError:
            pass

    def _swap_downward(self, p, p_val):
        '''Maintain the heap property after popping.'''
        l, r = self._left(p), self._right(p)

        try:
            left = self._get(l)

            try:
                right = self._get(r)
                c, c_val = (l, left) if self._cmp(right, left) else (r, right)

            except ValueError:
                c, c_val = l, left

        except ValueError:
            try:
                right = self._get(r)
                c, c_val = r, right

            except ValueError:
                return

        if self._cmp(p_val, c_val):
            self.Heap[p] = c_val
            self.Heap[c] = p_val
            self._swap_downward(c, p_val)

    def push(self, val):
        '''Push 'val' in to the heap.'''
        self.Heap.append(val)
        self._swap_upward(len(self.Heap) - 1, val)

    def pop(self):
        '''Pop off and return the top value in the heap.'''
        try:
            top = self.Heap[0]
            new_top = self.Heap[-1]
            self.Heap[0] = new_top
            self.Heap = self.Heap[:-1]
            self._swap_downward(0, new_top)

            return top

        except IndexError:
            raise ValueError('Can\'t pop an empty heap!')
