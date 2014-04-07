#!usr/bin/env Python

import unittest

from merge_sort import merge_sort


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

if __name__ == '__main__':
    unittest.main()
